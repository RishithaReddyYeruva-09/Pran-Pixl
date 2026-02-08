import streamlit as st
import time
import random
import os

# 1. Page Configuration
st.set_page_config(page_title="PranPixl | Smart Shopping", layout="wide")

# Initialize Session States
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Translation Dictionary
translations = {
    "English": {
        "instruction": "drag drop the image for scanning",
        "ready": "Image Received",
        "toggle_light": "☕ Dark Roast",
        "toggle_dark": "🥛 Light Latte",
        "watermark": "PRANPIXL",
        "buy": "Buy Now",
        "best_deal": "BEST VALUE"
    },
    "हिन्दी": {
        "instruction": "स्कैनिंग के लिए छवि को यहाँ खींचें और छोड़ें",
        "ready": "छवि प्राप्त हुई",
        "toggle_light": "☕ डार्क रोस्ट",
        "toggle_dark": "🥛 लाइट लैट्टे",
        "watermark": "प्राणपिक्सेल",
        "buy": "अभी खरीदें",
        "best_deal": "सबसे अच्छा सौदा"
    }
}

# 3. MOCK API LOGIC (To show "Working" Data during Review)
def get_live_market_data(item_name):
    """
    Simulates fetching real-time data from Amazon, Flipkart, Myntra, and Ajio.
    In a real app, this would use requests.get() to an API.
    """
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    data = {}
    base_price = random.randint(1500, 5000)
    
    for p in platforms:
        # Create slight price variations to show comparison logic
        price = base_price + random.randint(-200, 500)
        data[p] = {
            "price": f"₹{price:,}",
            "numeric_price": price,
            "rating": round(random.uniform(3.8, 4.9), 1),
            "reviews": f"{random.randint(500, 5000)}+",
            "delivery": f"{random.randint(1, 4)} Days"
        }
    return data

# 4. Theme & CSS
if st.session_state.theme == 'light':
    bg_color, text_color, box_bg, border_color = "#D7CCC8", "#3E2723", "rgba(255, 255, 255, 0.5)", "#3E2723"
    accent_color = "#5D4037"
    watermark_opacity = "0.15"
else:
    bg_color, text_color, box_bg, border_color = "#1B1411", "#D7CCC8", "rgba(62, 39, 35, 0.7)", "#D7CCC8"
    accent_color = "#BCAAA4"
    watermark_opacity = "0.1"

st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {bg_color} !important; }}
    .watermark-container {{ position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 0; pointer-events: none; }}
    .watermark-text {{ font-size: 14vw; font-weight: 900; color: {text_color}; opacity: {watermark_opacity}; font-family: sans-serif; }}
    
    .result-card {{
        background-color: {box_bg}; border: 2px solid {border_color};
        border-radius: 20px; padding: 18px; text-align: left;
        min-height: 220px; backdrop-filter: blur(8px);
        transition: transform 0.3s ease; margin-bottom: 12px;
    }}
    .price-tag {{ font-size: 1.6rem; font-weight: 800; color: {text_color}; margin: 10px 0; }}
    .best-badge {{
        background-color: #4CAF50; color: white; padding: 5px 12px;
        border-radius: 20px; font-size: 0.75rem; font-weight: bold; display: inline-block; margin-bottom: 10px;
    }}
    .rating-tag {{ color: #FFA000; font-weight: bold; font-size: 1.05rem; }}
    .app-header-row {{ display:flex; align-items:center; gap:12px; }}
    .app-logo {{ width:48px; height:48px; object-fit:contain; border-radius:8px; }}
    </style>
    """, unsafe_allow_html=True)

# 5. Header Section (with logo on the left)
h_col1, h_col2 = st.columns([2, 1.2])

with h_col1:
    # split into logo + title
    logo_col, title_col = st.columns([0.12, 0.88])
    with logo_col:
        # Option A: use a local file named 'logo.png' placed in the app folder
        if os.path.exists("logo.png"):
            st.image("logo.png", width=64)
        else:
            # Fallback: small styled box or emoji if no file is present
            st.markdown(
                f"""<div style="width:64px;height:64px;border-radius:12px;
                           background:{accent_color};display:flex;align-items:center;
                           justify-content:center;color:{text_color};font-weight:800;">
                           🅿
                       </div>""",
                unsafe_allow_html=True,
            )

    with title_col:
        st.markdown(f'<h1 style="color:{text_color}; padding-left: 10px; margin: 0;">PranPixl</h1>', unsafe_allow_html=True)

with h_col2:
    lang = st.selectbox("Language", list(translations.keys()), label_visibility="collapsed")
    ui = translations[lang]
    if st.button(ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"], use_container_width=True):
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
        st.rerun()

st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 6. Main Logic
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-top: 10vh;'>{ui['instruction']}</h3>", unsafe_allow_html=True)
else:
    with st.spinner('Analyzing Image & Fetching Live Prices...'):
        time.sleep(1.5) # Simulate AI Processing
        item_name = "Premium Sneakers" # Simulated AI Object Detection Result
        market_data = get_live_market_data(item_name)
        
        # Determine the cheapest platform
        cheapest_platform = min(market_data, key=lambda x: market_data[x]['numeric_price'])

    # Show Scanned Result
    r_col1, r_col2 = st.columns([1, 2])
    with r_col1:
        st.image(uploaded_file, width=250)
    with r_col2:
        st.markdown(f"<h2 style='color: {text_color}; margin-bottom:6px;'>{item_name}</h2>", unsafe_allow_html=True)
        st.info(f"Scan Status: {ui['ready']}")

    st.divider()

    # App Cards Section (with logos)
    apps = [
        {"name": "Amazon", "desc": "Global marketplace.", "logo": "amazon.png", "emoji": "🛒"},
        {"name": "Flipkart", "desc": "India's favorites.", "logo": "flipkart.png", "emoji": "📦"},
        {"name": "Myntra", "desc": "Premium lifestyle.", "logo": "myntra.png", "emoji": "👟"},
        {"name": "Ajio", "desc": "Artisanal fashion.", "logo": "ajio.png", "emoji": "🧵"}
    ]

    cols = st.columns(len(apps))
    
    for i, app in enumerate(apps):
        name = app['name']
        details = market_data[name]
        logo_path = app.get("logo", "")
        emoji_fallback = app.get("emoji", "🏷️")

        # Prepare logo HTML: use local file if exists, otherwise emoji box
        if logo_path and os.path.exists(logo_path):
            logo_html = f'<img src="{logo_path}" class="app-logo" alt="{name} logo">'
        else:
            # simple colored box with emoji fallback
            logo_html = f'''
                <div style="width:48px;height:48px;border-radius:8px;background:{accent_color};
                            display:flex;align-items:center;justify-content:center;color:{text_color};font-weight:700;">
                    {emoji_fallback}
                </div>
            '''

        with cols[i]:
            # Show "Best Deal" badge if it's the lowest price
            badge_html = f'<div class="best-badge">{ui["best_deal"]}</div>' if name == cheapest_platform else '<div style="height:28px;"></div>'
            
            # Card HTML: logo on left, title + price on right
            card_html = f"""
                <div class="result-card">
                    {badge_html}
                    <div style="display:flex; align-items:center; gap:12px;">
                        {logo_html}
                        <div style="flex:1;">
                            <div style="display:flex; align-items:center; justify-content:space-between;">
                                <h3 style="color: {text_color}; margin:0;">{name}</h3>
                                <div style="text-align:right;">
                                    <div class="price-tag" style="margin:0;">{details['price']}</div>
                                </div>
                            </div>
                            <div style="margin-top:6px;">
                                <span class="rating-tag">⭐ {details['rating']}</span>
                                <span style="color:{text_color}; opacity:0.7; margin-left:8px;">{details['reviews']} Reviews</span>
                            </div>
                            <hr style="border: 0.5px solid {border_color}; opacity: 0.3; margin-top:10px;">
                            <p style="color: {text_color}; opacity: 0.85; font-size: 0.9rem; margin:6px 0 0 0;">
                                • {details['delivery']} Delivery &nbsp; • Easy Returns &nbsp; • Secure Payment
                            </p>
                        </div>
                    </div>
                </div>
            """

            st.markdown(card_html, unsafe_allow_html=True)
            
            if st.button(f"{ui['buy']} @ {name}", key=f"btn_{name}", use_container_width=True):
                st.success(f"Redirecting to {name}...")

st.markdown("""<div style="position: fixed; bottom: 20px; right: 20px; width: 40px; height: 40px; background: white; border: 2px solid black; border-radius: 8px;"></div>""", unsafe_allow_html=True)
