import streamlit as st
import os
import requests
from io import BytesIO

# Attempt to import SerpApi; failure indicates missing requirements.txt entry
try:
    from serpapi import GoogleSearch
except ImportError:
    st.error("Missing Library: Please add 'google-search-results' to your requirements.txt file.")

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. STATE MANAGEMENT & THEME
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

translations = {
    "English": {
        "instruction": "drag drop the image for scanning",
        "ready": "Item Identified",
        "toggle_light": "☕ Dark Roast",
        "toggle_dark": "🥛 Light Latte",
        "watermark": "PRANPIXL",
        "buy": "Buy Now",
        "reset": "Scan another"
    }
}

# 3. DYNAMIC THEME COLORS (Prevents NameError)
if st.session_state.theme == 'light':
    bg_color, text_color, box_bg, border_color = "#D7CCC8", "#3E2723", "rgba(255, 255, 255, 0.4)", "#3E2723"
    watermark_opacity = "0.2"
else:
    bg_color, text_color, box_bg, border_color = "#1B1411", "#D7CCC8", "rgba(62, 39, 35, 0.6)", "#D7CCC8"
    watermark_opacity = "0.15"

# 4. API INTEGRATION LOGIC
def fetch_live_prices(query):
    """Fetches real prices from Indian retailers via Google Shopping."""
    api_key = "YOUR_SERPAPI_KEY" # Replace with your SerpApi key
    
    params = {
        "engine": "google_shopping",
        "q": query,
        "gl": "in", # Target India
        "hl": "en",
        "api_key": api_key
    }
    
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        shopping_results = results.get("shopping_results", [])
        
        # Format results for the 4 specific cards in your UI
        formatted_apps = []
        platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
        
        for platform in platforms:
            # Filter API results for the specific platform
            match = next((item for item in shopping_results if platform.lower() in item.get("source", "").lower()), None)
            if match:
                formatted_apps.append({
                    "name": platform,
                    "price": match.get("price", "N/A"),
                    "link": match.get("link", "#")
                })
            else:
                formatted_apps.append({"name": platform, "price": "Check Site", "link": f"https://www.{platform.lower()}.com"})
        
        return formatted_apps
    except Exception:
        return None

# 5. GLOBAL STYLING (CSS)
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {bg_color} !important; }}
    .watermark-container {{
        position: fixed; top: 55%; left: 50%; transform: translate(-50%, -50%); z-index: 0; pointer-events: none;
    }}
    .watermark-text {{
        font-size: 14vw; font-weight: 900; font-style: italic; color: {text_color};
        opacity: {watermark_opacity}; font-family: sans-serif; white-space: nowrap;
    }}
    .central-workspace {{ position: relative; z-index: 5; width: 95%; margin: auto; padding-top: 10px; }}
    
    /* Result Card Styling matching your reference */
    .result-card {{
        background-color: #E5DDD9; border: 3px solid #3E2723;
        border-radius: 60px; padding: 40px 20px; text-align: center;
        min-height: 480px; margin-bottom: 10px;
    }}
    .card-title {{ font-size: 2.5rem; font-weight: bold; color: #3E2723; margin-bottom: 15px; }}
    .card-price {{ font-size: 1.8rem; color: #2E7D32; font-weight: bold; margin-bottom: 15px; }}
    .card-details {{ text-align: left; color: #3E2723; font-size: 0.9rem; margin-bottom: 20px; }}

    /* Buy Now Button */
    div.stButton > button {{
        background-color: #12161D !important; color: white !important;
        border-radius: 8px !important; border: none !important;
        height: 55px !important; width: 100% !important; font-weight: bold !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 6. HEADER SECTION
h_col1, h_col2 = st.columns([2, 1.2])
with h_col1:
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; padding-left: 5%; padding-top: 15px;">
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; color: black; font-weight: bold;">logo</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: {text_color};">PranPixl</div>
        </div>
    """, unsafe_allow_html=True)

with h_col2:
    st.markdown('<div style="padding-top: 15px;">', unsafe_allow_html=True)
    btn_col1, btn_col2 = st.columns([1, 1])
    with btn_col2:
        lang = st.selectbox("Language", list(translations.keys()), label_visibility="collapsed")
        ui = translations[lang]
    with btn_col1:
        theme_btn = ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"]
        if st.button(theme_btn, use_container_width=True):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"<div style='border-bottom: 3px solid {border_color}; width: 100%; margin-top: 10px;'></div>", unsafe_allow_html=True)

# 7. WATERMARK
st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 8. MAIN CONTENT LOGIC
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    # LANDING VIEW
    st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-top: 10vh;'>{ui['instruction']}</h3>", unsafe_allow_html=True)
else:
    # RESULTS VIEW
    # Note: In a production environment, you would use an Image Recognition API (like Google Lens) 
    # to identify the product name from the image bytes.
    product_query = "Nike Air Max Sneakers" # Placeholder for identified item
    
    with st.spinner("Fetching live prices from Indian stores..."):
        apps_data = fetch_live_prices(product_query)
        if not apps_data: # Fallback if API key is missing/failed
            apps_data = [
                {"name": "Amazon", "price": "₹4,299", "link": "#"},
                {"name": "Flipkart", "price": "₹3,999", "link": "#"},
                {"name": "Myntra", "price": "₹4,500", "link": "#"},
                {"name": "Ajio", "price": "₹4,100", "link": "#"}
            ]

    # Product Overview
    res_col1, res_col2 = st.columns([1, 2])
    with res_col1:
        st.image(uploaded_file, width=280)
    with res_col2:
        st.markdown(f"<h1 style='color: {text_color};'>{product_query}</h1>", unsafe_allow_html=True)
        st.success(ui["ready"])
        if st.button(ui["reset"]): st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # SHOPPING CARTS GRID
    cols = st.columns(4)
    for i, app in enumerate(apps_data):
        with cols[i]:
            st.markdown(f"""
                <div class="result-card">
                    <div class="card-title">{app['name']}</div>
                    <div class="card-price">{app['price']}</div>
                    <div class="card-details">
                        <b>Includes:</b><br>
                        - Description<br>
                        - Product Info<br>
                        - Reviews
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(ui["buy"], app['link'], use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
