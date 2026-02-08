import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. PAGE CONFIG & AGGRESSIVE CSS ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700;900&display=swap');

    .block-container { padding: 1rem 3rem !important; max-width: 100% !important; }
    .stApp { background: #080a0f !important; color: white !important; font-family: 'Inter', sans-serif; }

    /* HEADER: Forced far-left and far-right */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        margin-bottom: 3rem;
    }
    .brand-section { display: flex; align-items: center; gap: 12px; }
    .logo-square { width: 35px; height: 35px; background: #00ffcc; border-radius: 8px; }
    .brand-name { font-family: 'Syncopate', sans-serif; font-size: 22px; letter-spacing: 2px; color: white; }

    /* Green Box Language Select */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 10px !important;
        background: rgba(0, 255, 204, 0.05) !important;
        min-width: 140px !important;
    }

    /* PAGE 1: RECTANGULAR UPLOAD BOX */
    .stFileUploader {
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        background: #0d1117 !important;
        max-width: 850px;
        margin: 4rem auto !important;
        padding: 60px !important;
    }
    .stFileUploader > section { border: none !important; padding: 0 !important; }

    /* PAGE 2: RESULT STRIP (1/16th Thumbnail) */
    .result-strip {
        display: flex;
        align-items: center;
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #00ffcc;
        margin: 40px 0;
    }

    /* PAGE 2: MARKETPLACE HORIZONTAL COLUMNS */
    .market-row {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 20px 0;
        scrollbar-width: none;
    }
    .market-row::-webkit-scrollbar { display: none; }

    .site-card {
        min-width: 320px;
        background: #0d1117;
        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }

    /* Glossy Best Deal Effect */
    .glossy-best {
        border: 1.5px solid #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }
    .deal-tag {
        position: absolute;
        top: -12px;
        right: 25px;
        background: #00ffcc;
        color: #000;
        font-size: 10px;
        font-weight: 900;
        padding: 5px 15px;
        border-radius: 50px;
    }

    /* FLYING FEEDBACK BUTTON (Bottom Right) */
    .feedback-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: black !important;
        padding: 16px 32px;
        border-radius: 100px;
        font-weight: 900;
        text-decoration: none;
        box-shadow: 0 10px 30px rgba(0, 255, 204, 0.4);
        z-index: 9999;
    }
    
    .price-txt { font-size: 2.2rem; font-weight: 900; color: #fff; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CORE AI ---
@st.cache_resource
def load_model():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

def main():
    # HEADER SECTION
    h_left, h_right = st.columns([4, 1])
    with h_left:
        st.markdown("""
            <div class="brand-section">
                <div class="logo-square"></div>
                <div class="brand-name">PRANPIXL</div>
            </div>
        """, unsafe_allow_html=True)
    with h_right:
        lang = st.selectbox("", ["English", "తెలుగు", "Hindi"], label_visibility="collapsed")

    # UPLOAD SECTION (HOME PAGE)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

    if not uploaded_file:
        # Static Home Page State
        st.markdown("<p style='text-align:center; opacity:0.3; margin-top:20px;'>Upload an image to start the analysis</p>", unsafe_allow_html=True)
    else:
        # RESULTS PAGE STATE
        model = load_model()
        img = Image.open(uploaded_file)
        
        with st.spinner("Processing..."):
            img_prep = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_prep))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # 1/16th Thumbnail Strip
        st.markdown('<div class="result-strip">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 15]) # 1:15 ratio creates the 1/16th thumbnail look
        with c1:
            st.image(img, use_container_width=True)
        with c2:
            st.markdown(f"<h2 style='margin:0; padding-left:15px;'>{label} <span style='color:#00ffcc; font-size:14px;'>• Identity Confirmed</span></h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Marketplace Horizontal Grid
        st.write("---")
        deals = [
            {"name": "Amazon", "price": 12999, "desc": "Official Store. Next-day delivery."},
            {"name": "Flipkart", "price": 11450, "desc": "Bank Offer Available. Fast shipping."},
            {"name": "Reliance", "price": 13200, "desc": "Official Brand Warranty Support."}
        ]
        
        min_p = min(p['price'] for p in deals)
        
        html_row = '<div class="market-row">'
        for p in deals:
            is_best = p['price'] == min_p
            card_css = "site-card glossy-best" if is_best else "site-card"
            tag = '<div class="deal-tag">BEST VALUE</div>' if is_best else ""
            
            html_row += f"""
            <div class="{card_css}">
                {tag}
                <p style="color:#00ffcc; font-size:0.7rem; font-weight:800; letter-spacing:1px;">{p['name'].upper()}</p>
                <h3 style="margin:5px 0;">{label}</h3>
                <div class="price-txt">₹{p['price']:,}</div>
                <p style="font-size:0.8rem; opacity:0.6; margin-bottom:15px; line-height:1.4;">{p['desc']}</p>
                <a href="#" style="display:block; background:white; color:black; text-align:center; padding:12px; border-radius:10px; font-weight:bold; text-decoration:none;">GET DEAL</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLYING FEEDBACK BUTTON
    st.markdown('<a href="mailto:support@pranpixl.com" class="feedback-btn">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
