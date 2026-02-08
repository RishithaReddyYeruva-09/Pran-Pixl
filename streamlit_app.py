import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Session State & Theme Initialization (Defined at the TOP)
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 3. Translation & Theme Variables (Prevents NameError)
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

# Initial variable setup to avoid errors
ui = translations["English"]

if st.session_state.theme == 'light':
    bg_color, text_color, box_bg, border_color = "#D7CCC8", "#3E2723", "rgba(255, 255, 255, 0.4)", "#3E2723"
    watermark_opacity = "0.2"
else:
    bg_color, text_color, box_bg, border_color = "#1B1411", "#D7CCC8", "rgba(62, 39, 35, 0.6)", "#D7CCC8"
    watermark_opacity = "0.15"

# 4. Live API Helper
def get_live_prices(query):
    try:
        from serpapi import GoogleSearch
        params = {
            "engine": "google_shopping",
            "q": query,
            "gl": "in", # Target India
            "hl": "en",
            "api_key": "YOUR_SERP_API_KEY" # <--- ADD YOUR KEY HERE
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        return results.get("shopping_results", [])[:4] # Top 4 results
    except Exception:
        return None

# 5. Dynamic CSS
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
    .result-card {{
        background-color: #E5DDD9; border: 3px solid #3E2723;
        border-radius: 60px; padding: 40px 20px; text-align: center;
        min-height: 520px; margin-bottom: 10px;
    }}
    div.stButton > button {{
        background-color: #12161D !important; color: white !important;
        border-radius: 8px !important; height: 50px !important; width: 100% !important; font-weight: bold !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 6. Header
h_col1, h_col2 = st.columns([2, 1.2])
with h_col1:
    st.markdown(f'<div style="color:{text_color}; font-weight:bold; font-size:1.5rem; padding-top:15px;">PranPixl</div>', unsafe_allow_html=True)
with h_col2:
    lang_choice = st.selectbox("Lang", list(translations.keys()), label_visibility="collapsed")
    ui = translations[lang_choice]
    if st.button(ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"]):
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
        st.rerun()

st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 7. Main Workspace
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-top: 10vh;'>{ui['instruction']}</h3>", unsafe_allow_html=True)
else:
    # Identified Item (In production, this would come from an Image Analysis API)
    product_name = "Premium Sneakers"
    
    with st.spinner("Fetching live prices..."):
        prices = get_live_prices(product_name)

    # Layout for Results
    t_col1, t_col2 = st.columns([1, 2])
    with t_col1: st.image(uploaded_file, width=280)
    with t_col2: 
        st.markdown(f"<h1 style='color:{text_color};'>{product_name}</h1>", unsafe_allow_html=True)
        if st.button(ui["reset"]): st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Shop Cards
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    cols = st.columns(4)
    
    for i, platform in enumerate(platforms):
        # Find matching price from API or use placeholder
        price_val = "₹1,499" # Default
        if prices and i < len(prices):
            price_val = prices[i].get("price", "Check Price")

        with cols[i]:
            st.markdown(f"""
                <div class="result-card">
                    <h1 style="color:#3E2723; font-size:2.5rem;">{platform}</h1>
                    <h2 style="color:#2E7D32;">{price_val}</h2>
                    <div style="text-align:left; color:#3E2723; margin-top:30px; font-size:0.9rem;">
                        <b>Includes:</b><br>- Description<br>- Product Info<br>- Reviews
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.button(ui["buy"], key=f"buy_{platform}")

st.markdown('</div>', unsafe_allow_html=True)
