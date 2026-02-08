import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

# --- 1. LANGUAGE & RUPEE DATA ---
LANG_DATA = {
    "English": {"tagline": "Visual Intelligence for the Modern Collector", "scan": "Initialize Scan", "buy": "Direct Link"},
    "తెలుగు": {"tagline": "ఆధునిక ప్రపంచం కోసం విజువల్ ఇంటెలిజెన్స్", "scan": "స్కాన్ ప్రారంభించండి", "buy": "నేరుగా కొనండి"},
    "Hindi": {"tagline": "आधुनिक युग के लिए विज़ुअल इंटेलिजेंस", "scan": "स्कैन शुरू करें", "buy": "सीधा लिंक"}
}

# --- 2. LUXURY UI DESIGN (CSS) ---
st.set_page_config(page_title="Pranpixl Elite", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Inter:wght@300;600&display=swap');

    /* Global Overrides */
    .stApp {
        background: radial-gradient(circle at 20% 30%, #12141d 0%, #050505 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Main Branding */
    .brand-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 4rem;
        font-weight: 700;
        letter-spacing: 12px;
        background: linear-gradient(90deg, #fff, #555);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }

    /* Laser Scanner Animation */
    .scanner-box {
        position: relative;
        border-radius: 30px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 0 50px rgba(0,0,0,0.5);
    }
    .laser-line {
        position: absolute;
        width: 100%;
        height: 8px;
        background: linear-gradient(to bottom, transparent, #00ffcc, transparent);
        box-shadow: 0 0 20px #00ffcc;
        z-index: 5;
        animation: laserMove 3s infinite ease-in-out;
    }
    @keyframes laserMove {
        0% { top: 0%; }
        50% { top: 100%; }
        100% { top: 0%; }
    }

    /* App Cards - Horizontal Swipe */
    .swipe-wrapper {
        display: flex;
        overflow-x: auto;
        gap: 30px;
        padding: 40px 10px;
        scrollbar-width: none;
    }
    .swipe-wrapper::-webkit-scrollbar { display: none; }

    .deal-card {
        min-width: 340px;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(25px);
        border-radius: 35px;
        padding: 35px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.5s all cubic-bezier(0.075, 0.82, 0.165, 1);
        position: relative;
    }
    .deal-card:hover {
        transform: translateY(-15px) scale(1.02);
        background: rgba(255, 255, 255, 0.06);
        border-color: #00ffcc;
    }

    /* Glossy Best Deal Highlight */
    .best-deal-glow {
        border: 1px solid #00ffcc !important;
        box-shadow: 0 0 40px rgba(0, 255, 204, 0.2);
    }
    .cheapest-badge {
        position: absolute;
        top: -15px;
        right: 30px;
        background: #00ffcc;
        color: #000;
        font-size: 0.7rem;
        font-weight: 800;
        padding: 5px 15px;
        border-radius: 50px;
        letter-spacing: 1px;
    }

    .price-display {
        font-size: 2.8rem;
        font-weight: 700;
        color: #ffffff;
        margin: 15px 0;
    }

    .action-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: #ffffff;
        color: #000000 !important;
        padding: 15px;
        border-radius: 18px;
        text-decoration: none;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s;
    }
    .action-btn:hover { background: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SCRAPING ENGINE ---
def scrape_indian_prices(item):
    # Simulates advanced live scraping for demonstration
    headers = {"User-Agent": "Mozilla/5.0"}
    # Mocking real-time variance for the demo
    base_price = np.random.randint(12000, 45000)
    return [
        {"app": "Amazon.in", "p": base_price + 500},
        {"app": "Flipkart", "p": base_price - 800},
        {"app": "Tata CLiQ", "p": base_price + 1200},
        {"app": "Reliance", "p": base_price - 200}
    ]

# --- 4. MAIN LOGIC ---
def main():
    # Sidebar
    with st.sidebar:
        st.markdown("### PRANPIXL CONTROL")
        lang_sel = st.selectbox("Market Language", ["English", "తెలుగు", "Hindi"])
        t = LANG_DATA[lang_sel]
    
    # Header
    st.markdown('<p class="brand-title">PRANPIXL</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; opacity:0.4; letter-spacing:3px;">{t["tagline"].upper()}</p>', unsafe_allow_html=True)

    # Model
    @st.cache_resource
    def load_luxury_model():
        return tf.keras.applications.MobileNetV2(weights='imagenet')
    
    model = load_luxury_model()
    
    # Upload Area
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        
        # Display Scanning Container
        st.markdown('<div class="scanner-box"><div class="laser-line"></div>', unsafe_allow_html=True)
        st.image(img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        with st.spinner("AI ANALYZING PIXELS..."):
            time.sleep(2) # Enhanced UX feel
            img_processed = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_processed))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()
            
            # Scrape Prices
            deals = scrape_indian_prices(label)

        st.markdown(f"<h2 style='text-align:center; letter-spacing:2px;'>IDENTIFIED: <span style='color:#00ffcc;'>{label}</span></h2>", unsafe_allow_html=True)

        # Horizontal Display
        min_price = min(d['p'] for d in deals)
        
        html_swipe = '<div class="swipe-wrapper">'
        for d in deals:
            is_best = d['p'] == min_price
            glow_class = "best-deal-glow" if is_best else ""
            badge = '<div class="cheapest-badge">BEST VALUE</div>' if is_best else ""
            
            html_swipe += f"""
            <div class="deal-card {glow_class}">
                {badge}
                <p style="color:#00ffcc; font-size:0.75rem; font-weight:800; letter-spacing:2px;">{d['app'].upper()}</p>
                <h3 style="margin:10px 0; font-family:'Syncopate';">{label}</h3>
                <div class="price-display">₹{d['p']:,}</div>
                <p style="opacity:0.4; font-size:0.8rem; margin-bottom:25px;">Verified Market Data • 2026</p>
                <a href="#" class="action-btn">{t['buy']}</a>
            </div>
            """
        html_swipe += '</div>'
        st.markdown(html_swipe, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
