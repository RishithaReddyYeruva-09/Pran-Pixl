import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time

# --- 1. THE "ULTIMATE" CSS RESET ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700;900&display=swap');

    /* 1. Global Layout & Edge-to-Edge Fix */
    [data-testid="stHeader"] {display:none !important;}
    .block-container {
        padding: 1.5rem 3rem !important;
        max-width: 100% !important;
    }
    .stApp { background: #080a0f !important; color: white !important; font-family: 'Inter', sans-serif; }

    /* 2. Header: Logo (Left) | Green Box (Right) */
    .header-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        margin-bottom: 3rem;
    }
    .brand-id { display: flex; align-items: center; gap: 12px; }
    .brand-logo { width: 32px; height: 32px; background: #00ffcc; border-radius: 8px; }
    .brand-name { font-family: 'Syncopate', sans-serif; font-size: 22px; letter-spacing: 2px; color: white; }

    /* The Language Box (Green Border) */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 8px !important;
        background: rgba(0, 255, 204, 0.05) !important;
        width: 140px !important;
    }

    /* 3. THE DROP ZONE: Clean Rectangle with Corner Lines */
    [data-testid="stFileUploader"] {
        max-width: 800px;
        margin: 5rem auto !important;
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        padding: 80px 20px !important;
        position: relative;
    }

    /* Decorative Corner Brackets (Top Left) */
    [data-testid="stFileUploader"]::before {
        content: "";
        position: absolute;
        top: -6px;
        left: -6px;
        width: 45px;
        height: 45px;
        border-top: 3px solid #00ffcc;
        border-left: 3px solid #00ffcc;
        border-radius: 12px 0 0 0;
        z-index: 10;
    }

    /* Decorative Corner Brackets (Bottom Right) */
    [data-testid="stFileUploader"]::after {
        content: "";
        position: absolute;
        bottom: -6px;
        right: -6px;
        width: 45px;
        height: 45px;
        border-bottom: 3px solid #00ffcc;
        border-right: 3px solid #00ffcc;
        border-radius: 0 0 12px 0;
        z-index: 10;
    }

    /* Hiding the 'Clumsy' Streamlit Uploader Elements */
    [data-testid="stFileUploaderDropzone"] { border: none !important; background: transparent !important; }
    [data-testid="stFileUploaderDropzone"] > div { display: none !important; }
    .st-emotion-cache-16ids93 { display: none !important; }

    /* 4. RESULT STRIP: 1/16th Thumbnail */
    .scan-confirmed {
        display: flex;
        align-items: center;
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #00ffcc;
        margin: 40px 0;
    }

    /* 5. HORIZONTAL MARKETPLACE */
    .market-scroll {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 20px 0;
        scrollbar-width: none;
    }
    .market-scroll::-webkit-scrollbar { display: none; }

    .site-card {
        min-width: 330px;
        background: #0d1117;
        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }

    /* Glossy Best Deal Highlight */
    .glossy-deal {
        border: 1.5px solid #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }
    .deal-tag {
        position: absolute;
        top: -10px;
        right: 25px;
        background: #00ffcc;
        color: black;
        font-size: 9px;
        font-weight: 900;
        padding: 5px 15px;
        border-radius: 50px;
    }

    /* 6. FLYING FEEDBACK BUTTON */
    .feedback-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: black !important;
        padding: 16px 32px;
        border-radius: 100px;
        font-weight: 800;
        text-decoration: none;
        box-shadow: 0 10px 20px rgba(0, 255, 204, 0.4);
        z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AI & LOGIC ---
@st.cache_resource
def load_ai():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

def main():
    # HEADER: BRAND (LEFT) | DROPDOWN (RIGHT)
    col_l, col_r = st.columns([5, 1])
    with col_l:
        st.markdown("""
            <div class="brand-id">
                <div class="brand-logo"></div>
                <div class="brand-name">PRANPIXL</div>
            </div>
            <p style="opacity:0.4; font-size:10px; letter-spacing:1px; margin-top:5px; margin-left:45px;">ADVANCED VISUAL INTELLIGENCE</p>
        """, unsafe_allow_html=True)
    with col_r:
        lang = st.selectbox("", ["English", "తెలుగు", "Hindi"], label_visibility="collapsed")

    # HOME PAGE: UPLOAD RECTANGLE
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if not uploaded_file:
        st.markdown("<p style='text-align:center; opacity:0.3; margin-top:20px; font-size:14px;'>Drop your luxury item photo here to begin</p>", unsafe_allow_html=True)
    else:
        # RESULTS PAGE: INFERENCE
        model = load_ai()
        img = Image.open(uploaded_file)
        
        with st.spinner("Analyzing Pixels..."):
            img_p = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # 1/16th THUMBNAIL View
        st.markdown('<div class="scan-confirmed">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 15]) # Precise 1/16th ratio
        with c1:
            st.image(img, use_container_width=True)
        with c2:
            st.markdown(f"<h2 style='margin:0; padding-left:15px;'>{label} <span style='color:#00ffcc; font-size:14px;'>• Identity Verified</span></h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # MARKETPLACE: Horizontal Swipe
        st.markdown("<p style='opacity:0.5; font-size:12px; margin-left:5px;'>MARKETPLACE COMPARISON</p>", unsafe_allow_html=True)
        platforms = [
            {"name": "Amazon India", "price": 14999, "desc": "Official Store. Next-day delivery."},
            {"name": "Flipkart", "price": 13450, "desc": "Bank Offers active. Fastest shipping."},
            {"name": "Myntra", "price": 15200, "desc": "Authenticity Guarantee & Premium Pack."}
        ]
        
        min_p = min(p['price'] for p in platforms)
        
        html_row = '<div class="market-scroll">'
        for p in platforms:
            is_best = p['price'] == min_p
            best_cls = "site-card glossy-deal" if is_best else "site-card"
            tag = '<div class="deal-tag">BEST VALUE</div>' if is_best else ""
            
            html_row += f"""
            <div class="{best_cls}">
                {tag}
                <p style="color:#00ffcc; font-size:0.7rem; font-weight:800; letter-spacing:1px;">{p['name'].upper()}</p>
                <h3 style="margin:5px 0;">{label}</h3>
                <div style="font-size:2.2rem; font-weight:900; margin:10px 0;">₹{p['price']:,}</div>
                <p style="font-size:0.8rem; opacity:0.6; margin-bottom:20px;">{p['desc']}</p>
                <a href="#" style="display:block; background:white; color:black; text-align:center; padding:12px; border-radius:12px; font-weight:bold; text-decoration:none;">GET DEAL</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLYING FEEDBACK BUTTON
    st.markdown('<a href="mailto:support@pranpixl.com" class="feedback-btn">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
