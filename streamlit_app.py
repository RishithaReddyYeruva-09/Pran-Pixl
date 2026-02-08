import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. THE BULLETPROOF VINTAGE CSS ---
st.set_page_config(page_title="Pranpixl Vintage", page_icon="☕", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;700&display=swap');

    /* Reset all Streamlit garbage */
    [data-testid="stHeader"] {display:none !important;}
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    /* Background: Clean Parchment */
    .stApp { background-color: #fdfaf5 !important; color: #2b1b17 !important; font-family: 'Inter', sans-serif; }

    /* TOP NAV: Espresso Bar */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 3rem;
        background: #2b1b17;
        color: #fdfaf5;
        border-bottom: 3px solid #00ffcc;
        width: 100%;
    }
    .brand-name { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 900; letter-spacing: 2px; }

    /* Green Box Language Select */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 8px !important;
        background: white !important;
        min-width: 140px !important;
    }

    /* MAIN LAYOUT SPLIT */
    .stHorizontalBlock { gap: 0 !important; }

    /* LEFT SIDEBAR (UPLOAD) */
    [data-testid="column"]:nth-child(1) {
        background: #3e2723 !important;
        padding: 40px 25px !important;
        min-height: 100vh;
        border-right: 2px solid #2b1b17;
    }

    /* FIX: The Single Upload Box (Kills the double box glitch) */
    [data-testid="stFileUploader"] {
        background: #2b1b17 !important;
        border: 1px dashed #00ffcc !important;
        border-radius: 15px !important;
        padding: 30px !important;
    }
    /* This line kills the inner Streamlit 'Drag and Drop' box */
    [data-testid="stFileUploaderDropzone"] { border: none !important; background: transparent !important; }
    [data-testid="stFileUploaderDropzone"] > div { display: none !important; }

    /* RIGHT SIDE (RESULTS) */
    [data-testid="column"]:nth-child(2) {
        padding: 60px 80px !important;
        background: #fdfaf5 !important;
    }

    /* 1/16th RESULT STRIP */
    .result-strip {
        display: flex;
        align-items: center;
        background: white;
        padding: 20px;
        border-radius: 12px;
        border-left: 8px solid #3e2723;
        margin-bottom: 40px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }

    /* MARKETPLACE CARDS */
    .market-card {
        min-width: 320px;
        background: white;
        border: 1px solid #d7ccc8;
        padding: 30px;
        border-radius: 15px;
        color: #3e2723;
        transition: 0.3s;
    }
    .best-deal { border: 2px solid #00ffcc !important; box-shadow: 0 10px 30px rgba(0,255,204,0.1); }
    
    /* FLYING FEEDBACK */
    .feedback-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: #000 !important;
        padding: 16px 32px;
        border-radius: 100px;
        font-weight: 800;
        text-decoration: none;
        box-shadow: 0 10px 30px rgba(0,255,204,0.3);
        z-index: 10000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIC ---
@st.cache_resource
def load_model():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

# --- 3. PAGE STRUCTURE ---

# Top Navigation
st.markdown("""
    <div class="top-nav">
        <div class="brand-name">PRANPIXL</div>
        <div id="dropdown-space"></div>
    </div>
""", unsafe_allow_html=True)

# Split Screen Columns
col_side, col_main = st.columns([1, 3.5])

with col_side:
    st.markdown("<h2 style='color:#fdfaf5; font-family:Playfair Display;'>The Appraisal</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00ffcc; font-size:14px;'>Drop item here to begin scan</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

with col_main:
    if not uploaded_file:
        st.markdown("<h1 style='opacity:0.03; font-size:120px; text-align:center; margin-top:150px;'>PRANPIXL</h1>", unsafe_allow_html=True)
    else:
        model = load_model()
        img = Image.open(uploaded_file)
        
        with st.spinner("Analyzing Pixels..."):
            img_p = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        st.markdown("<h1 style='font-family:Playfair Display;'>Market Analysis</h1>", unsafe_allow_html=True)
        
        # 1/16th Result Strip
        st.markdown('<div class="result-strip">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 15]) 
        with c1:
            st.image(img, use_container_width=True)
        with c2:
            st.markdown(f"<h3 style='margin:0; padding-left:15px; color:#2b1b17;'>{label} <span style='color:#00ffcc; font-size:14px;'>• Identity Confirmed</span></h3>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Marketplace Comparison
        platforms = [
            {"name": "Antique Amazon", "price": 12999, "best": False},
            {"name": "Heritage Flipkart", "price": 11450, "best": True},
            {"name": "Boutique Myntra", "price": 13200, "best": False}
        ]

        st.markdown("<div style='display:flex; overflow-x:auto; gap:20px; padding-bottom:20px;'>", unsafe_allow_html=True)
        m_cols = st.columns(len(platforms))
        for i, p in enumerate(platforms):
            with m_cols[i]:
                best_style = "best-deal" if p['best'] else ""
                st.markdown(f"""
                    <div class="market-card {best_style}">
                        <p style="font-size:10px; font-weight:800; color:#3e2723; opacity:0.6;">{p['name'].upper()}</p>
                        <h2 style="font-family:Playfair Display; margin:10px 0;">₹{p['price']:,}</h2>
                        <hr style="border:0.5px solid #d7ccc8; margin:15px 0;">
                        <a href="#" style="background:#2b1b17; color:white; display:block; text-align:center; padding:10px; border-radius:8px; text-decoration:none; font-weight:bold;">ACQUIRE ITEM</a>
                    </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Language Toggle in Sidebar
with st.sidebar:
    lang = st.selectbox("Language", ["English", "తెలుగు", "Hindi"])

# Feedback Button
st.markdown('<a href="#" class="feedback-btn">🚀 SEND DISPATCH</a>', unsafe_allow_html=True)
