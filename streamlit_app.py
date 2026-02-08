import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time

# --- 1. PAGE CONFIG & DESIGN ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;600;800&display=swap');

    .stApp { background: #080a0f; color: white; font-family: 'Inter', sans-serif; }
    
    /* Header: Logo Left, Dropdown Right */
    .header-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
    }
    .logo-container {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .logo-text {
        font-family: 'Syncopate', sans-serif;
        font-size: 22px;
        letter-spacing: 4px;
        color: #ffffff;
    }

    /* Unique Language Dropdown in Green Box */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 12px !important;
        background-color: rgba(0, 255, 204, 0.05) !important;
        min-width: 150px;
    }
    
    /* Upload Box Section */
    .upload-container {
        border: 2px dashed rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 60px;
        text-align: center;
        background: rgba(255, 255, 255, 0.02);
        margin: 20px 0;
    }

    /* Result Section: 1/16th thumbnail */
    .scan-header {
        display: flex;
        align-items: center;
        background: rgba(255,255,255,0.03);
        padding: 15px;
        border-radius: 20px;
        border-left: 5px solid #00ffcc;
        margin-bottom: 30px;
    }
    .thumbnail-box {
        width: 6.25%; /* Exactly 1/16th */
        border-radius: 10px;
        overflow: hidden;
        margin-right: 20px;
    }

    /* Horizontal Marketplace Scroll */
    .marketplace-row {
        display: flex;
        overflow-x: auto;
        gap: 25px;
        padding-bottom: 20px;
        scrollbar-width: none;
    }
    .marketplace-row::-webkit-scrollbar { display: none; }

    .product-card {
        min-width: 350px;
        background: rgba(255, 255, 255, 0.04);
        border-radius: 30px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }

    /* Glossy Best Price Effect */
    .glossy-highlight {
        border: 2px solid #00ffcc !important;
        background: linear-gradient(145deg, rgba(0,255,204,0.15) 0%, rgba(0,0,0,0) 100%);
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.2);
    }
    .best-deal-tag {
        position: absolute;
        top: 20px;
        right: 20px;
        background: #00ffcc;
        color: #000;
        font-size: 10px;
        font-weight: 900;
        padding: 5px 12px;
        border-radius: 50px;
        box-shadow: 0 4px 10px rgba(0, 255, 204, 0.4);
    }

    /* Floating Feedback Button */
    .floating-feedback {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: #000 !important;
        padding: 18px 30px;
        border-radius: 100px;
        font-weight: 800;
        text-decoration: none;
        z-index: 1000;
        box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3);
        font-size: 14px;
        transition: 0.3s;
    }
    .floating-feedback:hover { transform: scale(1.05); }

    .price-val { font-size: 2.2rem; font-weight: 800; color: #fff; margin: 15px 0; }
    .buy-button {
        display: block; width: 100%; text-align: center; background: #fff;
        color: #000 !important; padding: 14px; border-radius: 15px;
        font-weight: bold; text-decoration: none; margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA & AI ---
LANGS = {"English": "Buy Now", "తెలుగు": "కొనండి", "Hindi": "अभी खरीदें"}

@st.cache_resource
def load_ai():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

# --- 3. THE APP ---
def main():
    # HEADER: Name Left | Lang Dropdown Right
    header_col1, header_col2 = st.columns([1, 1])
    with header_col1:
        st.markdown('<div class="logo-container"><span style="font-size:30px;">🔮</span><span class="logo-text">PRANPIXL</span></div>', unsafe_allow_html=True)
    with header_col2:
        # Styled inside the green box via CSS above
        selected_lang = st.selectbox("", list(LANGS.keys()), label_visibility="collapsed")
        buy_text = LANGS[selected_lang]

    # BODY: Upload Section
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    if not uploaded_file:
        st.markdown("<h2 style='opacity:0.6;'>Drop your photo here</h2>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file:
        model = load_ai()
        img = Image.open(uploaded_file)
        
        with st.spinner("Decoding Pixels..."):
            # AI Logic
            img_input = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_input))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # RESULT HEADER: Image at 1/16th
        st.markdown('<div class="scan-header">', unsafe_allow_html=True)
        col_img, col_info = st.columns([1, 15]) # 1:15 ratio = 1/16th
        with col_img:
            st.image(img, use_container_width=True)
        with col_info:
            st.markdown(f"<h1>{label}</h1><p style='color:#00ffcc; letter-spacing:1px;'>AUTHENTICATED SCAN COMPLETE</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # MARKETPLACE SCROLL
        st.subheader("Marketplace Comparison")
        platforms = [
            {"name": "Amazon India", "price": 12999, "desc": "Official Brand Warranty, 7-day replacement policy.", "rev": "4.8/5 (2k+)"},
            {"name": "Flipkart", "price": 11450, "desc": "Bank Offers available. Fast delivery in your city.", "rev": "4.5/5 (1.5k+)"},
            {"name": "Myntra", "price": 13200, "desc": "Luxury Authenticity and Premium Packaging.", "rev": "4.9/5 (500+)"},
            {"name": "Tata CLiQ", "price": 14000, "desc": "Exclusive Luxury Collection Partner.", "rev": "4.7/5 (800+)"}
        ]
        
        min_p = min(p['price'] for p in platforms)
        
        html_row = '<div class="marketplace-row">'
        for p in platforms:
            is_best = p['price'] == min_p
            best_css = "glossy-highlight" if is_best else ""
            badge = '<div class="best-deal-tag">BEST VALUE</div>' if is_best else ""
            
            html_row += f"""
            <div class="product-card {best_css}">
                {badge}
                <p style="color:#00ffcc; font-size:0.7rem; font-weight:800; letter-spacing:1px;">{p['name'].upper()}</p>
                <h3 style="margin:10px 0;">{label}</h3>
                <div class="price-val">₹{p['price']:,}</div>
                <p style="font-size:0.85rem; color:#888; margin-bottom:15px;">{p['desc']}</p>
                <p style="font-size:0.8rem; color:#f1c40f; margin-bottom:20px;">⭐ {p['rev']}</p>
                <a href="#" class="buy-button">{buy_text}</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLOATING ACTION BUTTON (Fixed Bottom Right)
    st.markdown(f'<a href="mailto:feedback@pranpixl.com" class="floating-feedback">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
