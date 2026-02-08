import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. THE "NUCLEAR" CSS RESET ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700;900&display=swap');

    /* 1. FORCE FULL WIDTH & REMOVE ALL PADDING */
    [data-testid="stHeader"] {display:none !important;} /* Hide the top Streamlit bar */
    .block-container {
        padding: 2rem 4rem !important;
        max-width: 100% !important;
    }
    .stApp { background: #080a0f !important; color: white !important; font-family: 'Inter', sans-serif; }

    /* 2. HEADER ALIGNMENT (FAR LEFT & FAR RIGHT) */
    .custom-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        margin-bottom: 3rem;
    }
    .logo-box { width: 35px; height: 35px; background: #00ffcc; border-radius: 8px; }
    .title-text { font-family: 'Syncopate', sans-serif; font-size: 24px; letter-spacing: 3px; color: white; }

    /* 3. THE GREEN BOX DROPDOWN */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 10px !important;
        background: rgba(0, 255, 204, 0.05) !important;
        min-width: 150px !important;
    }

    /* 4. FIXING THE UPLOAD BOX (CLEAN RECTANGLE) */
    [data-testid="stFileUploader"] {
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        background: #0d1117 !important;
        padding: 40px !important;
        max-width: 900px;
        margin: 4rem auto !important;
    }
    /* Kills the ugly inner dashed box and default icons */
    [data-testid="stFileUploaderDropzone"] {
        border: none !important;
        background: transparent !important;
    }
    [data-testid="stFileUploaderDropzone"] > div { display: none !important; }

    /* 5. PAGE 2: RESULT STRIP (1/16th THUMBNAIL) */
    .result-strip {
        display: flex;
        align-items: center;
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 15px;
        border-left: 6px solid #00ffcc;
        margin-bottom: 30px;
    }

    /* 6. MARKETPLACE SCROLL */
    .market-row {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding-bottom: 20px;
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

    /* Glossy Effect */
    .glossy {
        border: 1.5px solid #00ffcc !important;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.2);
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

    /* 7. FLYING FEEDBACK BUTTON */
    .floating-btn {
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
        z-index: 99999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AI CORE ---
@st.cache_resource
def load_ai():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

def main():
    # HEADER SECTION
    st.markdown("""
        <div class="custom-header">
            <div style="display:flex; align-items:center; gap:12px;">
                <div class="logo-box"></div>
                <div class="title-text">PRANPIXL</div>
            </div>
            <div id="lang-anchor"></div>
        </div>
    """, unsafe_allow_html=True)
    
    # We use a trick to place the selectbox in the right-side header
    with st.container():
        c_space, c_lang = st.columns([10, 1])
        with c_lang:
            lang = st.selectbox("", ["English", "తెలుగు", "Hindi"], label_visibility="collapsed")

    # HOME PAGE: UPLOAD
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

    if not uploaded_file:
        st.markdown("<p style='text-align:center; opacity:0.3; margin-top:20px;'>Upload a luxury item image to analyze</p>", unsafe_allow_html=True)
    else:
        # RESULT PAGE
        model = load_ai()
        img = Image.open(uploaded_file)
        
        with st.spinner("Analyzing..."):
            img_p = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # 1/16th Thumbnail Result Strip
        st.markdown('<div class="result-strip">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 15]) 
        with col1:
            st.image(img, use_container_width=True)
        with col2:
            st.markdown(f"<h2 style='margin:0; padding-left:20px;'>{label} <span style='color:#00ffcc; font-size:14px;'>• Verified</span></h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Marketplace Columns
        platforms = [
            {"name": "Amazon", "price": 12999, "desc": "Official Store Warranty."},
            {"name": "Flipkart", "price": 11450, "desc": "Bank Offers available."},
            {"name": "Reliance", "price": 13200, "desc": "Genuine Product Support."}
        ]
        
        min_p = min(p['price'] for p in platforms)
        
        html_row = '<div class="market-row">'
        for p in platforms:
            is_best = p['price'] == min_p
            style = "site-card glossy" if is_best else "site-card"
            badge = '<div class="deal-tag">BEST VALUE</div>' if is_best else ""
            
            html_row += f"""
            <div class="{style}">
                {badge}
                <p style="color:#00ffcc; font-size:0.7rem; font-weight:800;">{p['name'].upper()}</p>
                <h3>{label}</h3>
                <div style="font-size:2rem; font-weight:900; margin:10px 0;">₹{p['price']:,}</div>
                <p style="font-size:0.8rem; opacity:0.6; margin-bottom:15px;">{p['desc']}</p>
                <a href="#" style="display:block; background:white; color:black; text-align:center; padding:12px; border-radius:12px; font-weight:bold; text-decoration:none;">GET DEAL</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLYING FEEDBACK BUTTON
    st.markdown('<a href="mailto:queries@pranpixl.com" class="floating-btn">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
