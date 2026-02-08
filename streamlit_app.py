import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time

# --- 1. PAGE CONFIG & ELITE UI ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;600;800&display=swap');

    .stApp { background: #080a0f; color: white; font-family: 'Inter', sans-serif; }
    
    /* Header: Logo Left, Green Box Dropdown Right */
    .header-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
    }
    .brand-group { display: flex; align-items: center; gap: 12px; }
    .logo-img { width: 40px; height: 40px; border-radius: 8px; }
    .brand-name { font-family: 'Syncopate', sans-serif; font-size: 20px; letter-spacing: 2px; }

    /* Custom Language Select in Green Box */
    div[data-baseweb="select"] {
        border: 1px solid #00ffcc !important;
        border-radius: 8px !important;
        background-color: rgba(0, 255, 204, 0.05) !important;
        width: 120px !important;
    }

    /* Fixed Rectangular Upload Box (Matching your Screenshot) */
    .stFileUploader {
        max-width: 800px;
        margin: 50px auto !important;
        border: 2px dashed rgba(255, 255, 255, 0.1) !important;
        border-radius: 30px !important;
        padding: 80px 20px !important;
        background: rgba(255, 255, 255, 0.02);
    }
    .stFileUploader section { padding: 0 !important; }
    
    /* Result Section: 1/16th Scale */
    .scan-header {
        display: flex;
        align-items: center;
        background: rgba(255,255,255,0.03);
        padding: 15px;
        border-radius: 20px;
        border-left: 5px solid #00ffcc;
        margin: 30px auto;
        max-width: 1200px;
    }

    /* Horizontal Swipe Cards */
    .marketplace-row {
        display: flex;
        overflow-x: auto;
        gap: 25px;
        padding: 30px 10px;
        scrollbar-width: none;
    }
    .marketplace-row::-webkit-scrollbar { display: none; }

    .product-card {
        min-width: 320px;
        background: rgba(255, 255, 255, 0.04);
        border-radius: 28px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }

    /* Glossy Best Deal Highlight */
    .glossy-best {
        border: 1px solid #00ffcc !important;
        background: linear-gradient(145deg, rgba(0,255,204,0.1) 0%, rgba(0,0,0,0) 100%);
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.2);
    }
    .deal-badge {
        position: absolute;
        top: -12px;
        right: 20px;
        background: #00ffcc;
        color: #000;
        font-size: 10px;
        font-weight: 900;
        padding: 5px 12px;
        border-radius: 50px;
        z-index: 100;
    }

    /* Floating Feedback Button */
    .floating-query {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: #000 !important;
        padding: 15px 30px;
        border-radius: 100px;
        font-weight: 800;
        text-decoration: none;
        box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3);
        z-index: 1000;
    }

    .price-val { font-size: 2rem; font-weight: 800; color: #fff; margin: 10px 0; }
    .buy-btn {
        display: block; width: 100%; text-align: center; background: #fff;
        color: #000 !important; padding: 12px; border-radius: 10px;
        font-weight: bold; text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIC ---
LANGS = {"English": "Buy Now", "తెలుగు": "కొనండి", "Hindi": "खरीदें"}

@st.cache_resource
def get_model():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

def main():
    # HEADER: Brand Left | Green Box Select Right
    h_left, h_right = st.columns([2, 1])
    with h_left:
        st.markdown("""
            <div class="brand-group">
                <img src="https://i.imgur.com/GscX6yN.png" class="logo-img">
                <div class="brand-name">PRANPIXL</div>
            </div>
            <p style="opacity:0.4; font-size:10px; margin-left:55px;">ADVANCED VISUAL INTELLIGENCE</p>
        """, unsafe_allow_html=True)
    with h_right:
        lang = st.selectbox("", list(LANGS.keys()), label_visibility="collapsed")
        buy_txt = LANGS[lang]

    # BODY: Single Centered Upload Box
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if not uploaded_file:
        st.markdown("<p style='text-align:center; opacity:0.3; font-size:14px;'>Drop your luxury item photo here to analyze</p>", unsafe_allow_html=True)

    if uploaded_file:
        model = get_model()
        img = Image.open(uploaded_file)
        
        with st.spinner("Processing..."):
            img_in = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_in))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # RESULT HEADER: Image at 1/16th
        st.markdown('<div class="scan-header">', unsafe_allow_html=True)
        c_thumb, c_text = st.columns([1, 15]) 
        with c_thumb:
            st.image(img, use_container_width=True)
        with c_text:
            st.markdown(f"<h2 style='margin:0;'>{label}</h2><p style='color:#00ffcc; margin:0;'>IDENTITY VERIFIED</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # MARKETPLACE SCROLL
        st.markdown("<p style='margin-left:10px; opacity:0.5;'>SWIPE TO COMPARE DEALS</p>", unsafe_allow_html=True)
        
        deals = [
            {"app": "Amazon", "price": 12499, "desc": "Official Store, Next-day delivery."},
            {"app": "Flipkart", "price": 11800, "desc": "Bank Offer Available, Local Stock."},
            {"app": "Myntra", "price": 13200, "desc": "Authenticity Certified, Premium Pack."}
        ]
        
        min_p = min(d['price'] for d in deals)
        
        html_row = '<div class="marketplace-row">'
        for d in deals:
            is_best = d['price'] == min_p
            best_css = "glossy-best" if is_best else ""
            badge = '<div class="deal-badge">BEST VALUE</div>' if is_best else ""
            
            html_row += f"""
            <div class="product-card {best_css}">
                {badge}
                <p style="color:#00ffcc; font-size:0.7rem; font-weight:800; letter-spacing:1px;">{d['app'].upper()}</p>
                <h4 style="margin:5px 0;">{label}</h4>
                <div class="price-val">₹{d['price']:,}</div>
                <p style="font-size:0.8rem; color:#888; margin-bottom:15px;">{d['desc']}</p>
                <a href="#" class="buy-btn">{buy_txt}</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLOATING ACTION BUTTON
    st.markdown(f'<a href="mailto:queries@pranpixl.com" class="floating-query">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
