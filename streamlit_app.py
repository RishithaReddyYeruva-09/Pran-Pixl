import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. THE STABLE VINTAGE RESET ---
st.set_page_config(page_title="Pranpixl Vintage", page_icon="☕", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;700&display=swap');

    /* Global Fixes */
    [data-testid="stHeader"] {display:none !important;}
    .block-container { padding: 0 !important; max-width: 100% !important; }
    .stApp { background-color: #fdfaf5 !important; color: #3e2723 !important; font-family: 'Inter', sans-serif; }

    /* TOP NAV */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 3rem;
        background: #efebe9;
        border-bottom: 2px solid #3e2723;
        width: 100%;
    }
    .brand-text { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 900; color: #3e2723; }

    /* DROPDOWN BOX */
    div[data-baseweb="select"] {
        border: 2px solid #3e2723 !important;
        border-radius: 4px !important;
        background: white !important;
        min-width: 120px !important;
    }

    /* MAIN SPLIT */
    .stHorizontalBlock { gap: 0 !important; }

    /* LEFT SIDEBAR (UPLOAD) */
    [data-testid="column"]:nth-child(1) {
        background: #2b1b17 !important;
        padding: 40px 20px !important;
        min-height: 100vh;
        border-right: 3px double #3e2723;
    }

    /* FIXING THE UPLOAD BOX (No double box) */
    [data-testid="stFileUploader"] {
        background: #3e2723 !important;
        border: 1px dashed #efebe9 !important;
        border-radius: 8px !important;
        padding: 30px !important;
    }
    [data-testid="stFileUploaderDropzone"] > div { display: none !important; }
    [data-testid="stFileUploaderDropzone"] { border: none !important; }

    /* RIGHT SIDE (RESULTS) */
    [data-testid="column"]:nth-child(2) {
        padding: 50px 70px !important;
        background: #fdfaf5 !important;
    }

    /* 1/16th RESULT STRIP */
    .result-strip {
        display: flex;
        align-items: center;
        background: #efebe9;
        padding: 15px;
        border-radius: 4px;
        border-left: 8px solid #3e2723;
        margin-bottom: 40px;
        box-shadow: 4px 4px 0px #d7ccc8;
    }

    /* MARKETPLACE CARDS */
    .market-card {
        min-width: 300px;
        background: white;
        border: 1px solid #d7ccc8;
        padding: 25px;
        border-radius: 2px;
        box-shadow: 5px 5px 0px #3e2723;
        color: #3e2723;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIC ---
@st.cache_resource
def load_ai():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

# --- 3. THE LAYOUT ---

# Top Nav
st.markdown("""
    <div class="top-nav">
        <div class="brand-text">PRANPIXL</div>
        <div id="dropdown"></div>
    </div>
""", unsafe_allow_html=True)

# Split Screen
col_side, col_main = st.columns([1, 3.5])

with col_side:
    st.markdown("<h2 style='color:#efebe9; font-family:Playfair Display;'>The Ledger</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#d7ccc8; font-size:14px;'>Place your item here for appraisal</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

with col_main:
    if not uploaded_file:
        st.markdown("<h1 style='opacity:0.05; font-size:100px; text-align:center; margin-top:150px;'>PRANPIXL</h1>", unsafe_allow_html=True)
    else:
        model = load_ai()
        img = Image.open(uploaded_file)
        
        # Identification
        img_p = img.convert('RGB').resize((224, 224))
        arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
        preds = model.predict(np.expand_dims(arr, axis=0))
        label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        st.markdown("<h1 style='font-family:Playfair Display;'>Appraisal Report</h1>", unsafe_allow_html=True)
        
        # 1/16th Thumb Strip
        st.markdown('<div class="result-strip">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 15])
        with c1:
            st.image(img, use_container_width=True)
        with c2:
            st.markdown(f"<h3 style='margin:0; padding-left:15px; font-family:Playfair Display;'>{label}</h3>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Marketplace
        st.markdown("### Market Listings")
        platforms = [
            {"name": "Antique Amazon", "price": 12999, "best": False},
            {"name": "Heritage Flipkart", "price": 11450, "best": True},
            {"name": "Boutique Tata", "price": 13200, "best": False}
        ]

        # Horizontal Scroll
        st.markdown("""
            <style>
            .stHorizontalBlock { overflow-x: auto; gap: 20px; }
            </style>
        """, unsafe_allow_html=True)
        
        m_cols = st.columns(len(platforms))
        for i, p in enumerate(platforms):
            with m_cols[i]:
                st.markdown(f"""
                    <div class="market-card">
                        <p style="font-size:10px; font-weight:bold; letter-spacing:1px;">{p['name'].upper()}</p>
                        <h2 style="font-family:Playfair Display; margin:10px 0;">₹{p['price']:,}</h2>
                        <a href="#" style="color:#3e2723; font-weight:bold; text-decoration:none; font-size:12px;">ACQUIRE ITEM →</a>
                    </div>
                """, unsafe_allow_html=True)

# Fixed Language Select in Sidebar
with st.sidebar:
    lang = st.selectbox("Language", ["English", "తెలుగు", "Hindi"])
    
