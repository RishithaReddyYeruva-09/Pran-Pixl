import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. THE DASHBOARD CSS ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700;900&display=swap');

    /* Global Reset */
    [data-testid="stHeader"] {display:none !important;}
    .block-container { padding: 0 !important; max-width: 100% !important; }
    .stApp { background: #f0f2f5 !important; color: #1e1e1e !important; font-family: 'Inter', sans-serif; }

    /* TOP BAR: Logo Left, Green Dropdown Right */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 3rem;
        background: white;
        border-bottom: 1px solid #e0e0e0;
        width: 100%;
    }
    .nav-logo { display: flex; align-items: center; gap: 10px; font-family: 'Syncopate', sans-serif; font-size: 18px; color: #000; }
    .logo-square { width: 30px; height: 30px; background: #00ffcc; border-radius: 6px; }

    /* Green Box Language Dropdown */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 8px !important;
        background: white !important;
        min-width: 120px !important;
    }

    /* MAIN SPLIT LAYOUT */
    .main-container { display: flex; height: calc(100vh - 70px); }

    /* LEFT SIDE: UPLOAD ZONE (DARK) */
    .upload-sidebar {
        width: 350px;
        background: #12141d;
        padding: 30px 20px;
        color: white;
        display: flex;
        flex-direction: column;
    }

    [data-testid="stFileUploader"] {
        background: #1c1f26 !important;
        border: 2px dashed #00ffcc44 !important;
        border-radius: 15px !important;
        padding: 20px !important;
    }
    [data-testid="stFileUploaderDropzone"] > div { display: none !important; }

    /* RIGHT SIDE: RESULTS (LIGHT) */
    .results-area {
        flex-grow: 1;
        padding: 40px 60px;
        overflow-y: auto;
    }

    /* 1/16th RESULT STRIP */
    .result-strip {
        display: flex;
        align-items: center;
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 6px solid #00ffcc;
        margin-bottom: 40px;
    }

    /* MARKETPLACE CARDS */
    .market-grid {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding-bottom: 20px;
        scrollbar-width: none;
    }
    .market-grid::-webkit-scrollbar { display: none; }

    .market-card {
        min-width: 280px;
        background: #1c1f26;
        color: white;
        border-radius: 20px;
        padding: 25px;
        position: relative;
    }
    .best-deal { border: 2px solid #00ffcc !important; box-shadow: 0 10px 30px rgba(0,255,204,0.1); }
    
    /* FEEDBACK BUTTON */
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
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIC ---
@st.cache_resource
def load_engine():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

# --- 3. STRUCTURE ---
# TOP NAV
st.markdown("""
    <div class="top-nav">
        <div class="nav-logo">
            <div class="logo-square"></div> PRANPIXL
        </div>
        <div id="dropdown-anchor"></div>
    </div>
""", unsafe_allow_html=True)

# Main Dashboard Columns
col_side, col_main = st.columns([1, 3.5])

with col_side:
    st.markdown('<div class="upload-sidebar">', unsafe_allow_html=True)
    st.markdown("### UPLOAD ZONE")
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    st.markdown("<p style='font-size:12px; opacity:0.5; margin-top:20px;'>Supports JPG, PNG (Max 200MB)</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_main:
    if not uploaded_file:
        st.markdown("""
            <div style="text-align:center; margin-top:150px; opacity:0.2;">
                <h1 style="font-family:'Syncopate';">PRANPIXL HOME</h1>
                <p>Drop an image in the left panel to begin analysis</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        # PAGE 2 CONTENT
        model = load_engine()
        img = Image.open(uploaded_file)
        
        # AI Inference
        img_p = img.convert('RGB').resize((224, 224))
        arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
        preds = model.predict(np.expand_dims(arr, axis=0))
        label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        st.markdown("## RESULTS")
        
        # 1/16th Thumb Strip
        st.markdown('<div class="result-strip">', unsafe_allow_html=True)
        c_thumb, c_name = st.columns([1, 15])
        with c_thumb:
            st.image(img, use_container_width=True)
        with c_name:
            st.markdown(f"<h3 style='margin:0; color:black;'>{label}</h3><p style='color:#00ffcc; margin:0;'>AI Verified Identity</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Marketplace
        st.markdown("### MARKETPLACE")
        platforms = [
            {"name": "Amazon", "price": 12999, "is_best": False},
            {"name": "Flipkart", "price": 11450, "is_best": True},
            {"name": "Tata CLiQ", "price": 13200, "is_best": False}
        ]

        html_market = '<div class="market-grid">'
        for p in platforms:
            cls = "market-card best-deal" if p['is_best'] else "market-card"
            badge = '<div style="position:absolute; top:15px; right:15px; background:#00ffcc; color:black; font-size:10px; font-weight:bold; padding:2px 8px; border-radius:10px;">BEST</div>' if p['is_best'] else ""
            html_market += f"""
            <div class="{cls}">
                {badge}
                <p style="color:#00ffcc; font-size:10px; font-weight:bold;">{p['name'].upper()}</p>
                <div style="font-size:1.8rem; font-weight:900;">₹{p['price']:,}</div>
                <hr style="opacity:0.1; margin:15px 0;">
                <p style="font-size:11px; opacity:0.6;">Verified Store • 2026</p>
            </div>
            """
        html_market += '</div>'
        st.markdown(html_market, unsafe_allow_html=True)

# Language Dropdown in Nav (via floating logic)
with st.sidebar:
    st.markdown("### SETTINGS")
    lang = st.selectbox("Language", ["English", "తెలుగు", "Hindi"], label_visibility="collapsed")

# FEEDBACK
st.markdown('<a href="#" class="feedback-btn">FEEDBACK BUTTON</a>', unsafe_allow_html=True)
