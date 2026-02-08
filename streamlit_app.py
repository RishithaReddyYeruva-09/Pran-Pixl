import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time

# --- 1. PAGE CONFIG & FULL-WIDTH ALIGNMENT ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;600;800&display=swap');

    /* Force Full Page Alignment and Remove Streamlit Padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }
    
    .stApp { background: #080a0f; color: white; font-family: 'Inter', sans-serif; }

    /* Header: Edge-to-Edge Alignment */
    .header-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        width: 100%;
        margin-bottom: 40px;
    }
    .brand-group { display: flex; flex-direction: column; align-items: flex-start; }
    .logo-row { display: flex; align-items: center; gap: 12px; }
    .logo-img { width: 32px; height: 32px; background: #00ffcc; border-radius: 8px; }
    .brand-name { font-family: 'Syncopate', sans-serif; font-size: 22px; letter-spacing: 3px; color: white; }
    .tagline { opacity: 0.5; font-size: 10px; margin-top: 5px; letter-spacing: 1px; }

    /* Green Box Dropdown - Perfectly Aligned Right */
    div[data-baseweb="select"] {
        border: 1.5px solid #00ffcc !important;
        border-radius: 10px !important;
        background-color: rgba(0, 255, 204, 0.05) !important;
        width: 130px !important;
    }
    
    /* Central Upload Box Styling */
    .stFileUploader {
        max-width: 900px;
        margin: 0 auto !important;
        border: 2px dashed rgba(255, 255, 255, 0.1) !important;
        border-radius: 30px !important;
        background: rgba(255, 255, 255, 0.02);
    }

    /* Result Header: 1/16th Scale Layout */
    .scan-header {
        display: flex;
        align-items: center;
        background: rgba(255,255,255,0.03);
        padding: 20px;
        border-radius: 20px;
        border-left: 4px solid #00ffcc;
        margin-top: 50px;
    }

    /* Horizontal Swipe Cards */
    .marketplace-row {
        display: flex;
        overflow-x: auto;
        gap: 25px;
        padding: 30px 5px;
        scrollbar-width: none;
    }
    .marketplace-row::-webkit-scrollbar { display: none; }

    .product-card {
        min-width: 340px;
        background: rgba(255, 255, 255, 0.04);
        border-radius: 28px;
        padding: 30px;
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
        right: 25px;
        background: #00ffcc;
        color: #000;
        font-size: 10px;
        font-weight: 900;
        padding: 6px 14px;
        border-radius: 50px;
        z-index: 10;
    }

    /* Floating Feedback Button */
    .floating-query {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: #000 !important;
        padding: 18px 35px;
        border-radius: 100px;
        font-weight: 800;
        text-decoration: none;
        box-shadow: 0 10px 30px rgba(0, 255, 204, 0.4);
        z-index: 9999;
    }

    .price-val { font-size: 2.4rem; font-weight: 800; color: #fff; margin: 15px 0; }
    .buy-btn {
        display: block; width: 100%; text-align: center; background: #fff;
        color: #000 !important; padding: 14px; border-radius: 12px;
        font-weight: 800; text-decoration: none; text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CORE LOGIC ---
LANGS = {"English": "Buy Now", "తెలుగు": "కొనండి", "Hindi": "खरीदें"}

@st.cache_resource
def get_model():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

def main():
    # HEADER: BRAND (LEFT) | DROPDOWN (RIGHT)
    col_l, col_r = st.columns([4, 1])
    with col_l:
        st.markdown("""
            <div class="brand-group">
                <div class="logo-row">
                    <div class="logo-img"></div>
                    <div class="brand-name">PRANPIXL</div>
                </div>
                <div class="tagline">ADVANCED VISUAL INTELLIGENCE</div>
            </div>
        """, unsafe_allow_html=True)
    with col_r:
        # Perfectly placed in the green-box style
        lang = st.selectbox("", list(LANGS.keys()), label_visibility="collapsed")
        buy_txt = LANGS[lang]

    # BODY: Centered Upload
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if not uploaded_file:
        st.markdown("<p style='text-align:center; opacity:0.3; margin-top:20px; font-size:14px;'>Drop your luxury item photo here to analyze</p>", unsafe_allow_html=True)

    if uploaded_file:
        model = get_model()
        img = Image.open(uploaded_file)
        
        with st.spinner("Analyzing Pixels..."):
            img_in = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_in))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # RESULT SECTION: 1/16th Page View
        st.markdown('<div class="scan-header">', unsafe_allow_html=True)
        # Using 1:15 ratio to simulate 1/16th scale accurately
        c_thumb, c_name = st.columns([1, 15]) 
        with c_thumb:
            st.image(img, use_container_width=True)
        with c_name:
            st.markdown(f"<h1 style='margin:0; padding-left:10px;'>{label}</h1><p style='color:#00ffcc; margin:0; padding-left:10px;'>IDENTITY VERIFIED</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # MARKETPLACE SCROLL
        st.markdown("<p style='margin: 30px 0 10px 5px; opacity:0.5; font-size:12px; font-weight:bold;'>SWIPE FOR MARKET COMPARISON</p>", unsafe_allow_html=True)
        
        deals = [
            {"app": "Amazon", "price": 12499, "desc": "Official Store. Same-day delivery."},
            {"app": "Flipkart", "price": 11800, "desc": "Bank Offers. Stock in Hyderabad."},
            {"app": "Tata CLiQ", "price": 13200, "desc": "Authenticity Certified. Luxury Pack."},
            {"app": "Reliance Digital", "price": 12900, "desc": "Official Warranty Support."}
        ]
        
        min_p = min(d['price'] for d in deals)
        
        html_row = '<div class="marketplace-row">'
        for d in deals:
            is_best = d['price'] == min_p
            style_cls = "product-card glossy-best" if is_best else "product-card"
            badge = '<div class="deal-badge">BEST VALUE</div>' if is_best else ""
            
            html_row += f"""
            <div class="{style_cls}">
                {badge}
                <p style="color:#00ffcc; font-size:0.75rem; font-weight:800; letter-spacing:1px;">{d['app'].upper()}</p>
                <h3 style="margin:10px 0; color:white;">{label}</h3>
                <div class="price-val">₹{d['price']:,}</div>
                <p style="font-size:0.8rem; color:#888; margin-bottom:20px; line-height:1.4;">{d['desc']}</p>
                <a href="#" class="buy-btn">{buy_txt}</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLOATING FEEDBACK (Bottom Right)
    st.markdown(f'<a href="mailto:support@pranpixl.com" class="floating-query">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
