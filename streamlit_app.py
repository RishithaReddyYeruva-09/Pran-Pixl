
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. SETTINGS & PAGE WIDTH ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700&display=swap');

    /* Remove Streamlit's default padding to fix alignment */
    .block-container {
        padding-top: 1.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }
    
    .stApp { background: #080a0f; color: white; font-family: 'Inter', sans-serif; }

    /* HEADER: Logo (Left) | Dropdown (Right) */
    .header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        margin-bottom: 50px;
    }
    .brand-left { display: flex; align-items: center; gap: 12px; }
    .brand-logo { width: 35px; height: 35px; background: #00ffcc; border-radius: 8px; }
    .brand-name { font-family: 'Syncopate', sans-serif; font-size: 22px; letter-spacing: 2px; }

    /* The Language Box (Green Border) */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 10px !important;
        background: rgba(0, 255, 204, 0.05) !important;
        width: 140px !important;
    }

    /* UPLOAD BOX: Simple & Rounded */
    .stFileUploader {
        max-width: 800px;
        margin: 0 auto !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        background: #0d1117;
    }

    /* SCAN RESULT: 1/16th Scale Thumbnail */
    .result-strip {
        display: flex;
        align-items: center;
        background: rgba(255, 255, 255, 0.02);
        padding: 15px;
        border-radius: 15px;
        margin-top: 40px;
        border-left: 4px solid #00ffcc;
    }

    /* HORIZONTAL MARKETPLACE */
    .market-scroll {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 20px 0;
        scrollbar-width: none;
    }
    .market-scroll::-webkit-scrollbar { display: none; }

    .site-card {
        min-width: 320px;
        background: #0d1117;
        border-radius: 25px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }

    /* Glossy Best Deal */
    .glossy-deal {
        border: 1.5px solid #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }
    .deal-tag {
        position: absolute;
        top: -10px;
        right: 20px;
        background: #00ffcc;
        color: black;
        font-size: 9px;
        font-weight: 900;
        padding: 4px 12px;
        border-radius: 50px;
    }

    /* FLYING FEEDBACK BUTTON */
    .feedback-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: black !important;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: 800;
        text-decoration: none;
        box-shadow: 0 10px 20px rgba(0, 255, 204, 0.3);
        z-index: 1000;
    }

    .price { font-size: 2rem; font-weight: 800; color: #fff; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIC ---
@st.cache_resource
def load_ai():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

def main():
    # HEADER
    col_logo, col_space, col_lang = st.columns([1, 2, 0.4])
    with col_logo:
        st.markdown("""
            <div class="brand-left">
                <div class="brand-logo"></div>
                <div class="brand-name">PRANPIXL</div>
            </div>
        """, unsafe_allow_html=True)
    with col_lang:
        lang = st.selectbox("", ["English", "తెలుగు", "Hindi"], label_visibility="collapsed")

    # UPLOAD
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

    if uploaded_file:
        model = load_ai()
        img = Image.open(uploaded_file)
        
        # Identification
        img_res = img.convert('RGB').resize((224, 224))
        arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_res))
        preds = model.predict(np.expand_dims(arr, axis=0))
        label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # RESULT: 1/16th Image
        st.markdown('<div class="result-strip">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 15]) # 1/16th ratio
        with c1:
            st.image(img, use_container_width=True)
        with c2:
            st.markdown(f"<h2 style='margin:0; padding-left:15px;'>{label}</h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # DEALS
        st.write("---")
        platforms = [
            {"name": "Amazon", "price": 12999, "desc": "Fast delivery. Brand Warranty."},
            {"name": "Flipkart", "price": 11450, "desc": "Bank Offers. Local Delivery."},
            {"name": "Myntra", "price": 13200, "desc": "Premium Packaging."}
        ]
        
        min_p = min(p['price'] for p in platforms)
        
        html_row = '<div class="market-scroll">'
        for p in platforms:
            is_best = p['price'] == min_p
            best_cls = "site-card glossy-deal" if is_best else "site-card"
            tag = '<div class="deal-tag">BEST PRICE</div>' if is_best else ""
            
            html_row += f"""
            <div class="{best_cls}">
                {tag}
                <p style="color:#00ffcc; font-size:0.7rem; font-weight:800;">{p['name'].upper()}</p>
                <div class="price">₹{p['price']:,}</div>
                <p style="font-size:0.8rem; opacity:0.6;">{p['desc']}</p>
                <a href="#" style="display:block; background:white; color:black; text-align:center; padding:10px; border-radius:10px; font-weight:bold; margin-top:15px; text-decoration:none;">BUY NOW</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLYING BUTTON
    st.markdown('<a href="mailto:feedback@pranpixl.com" class="feedback-btn">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
