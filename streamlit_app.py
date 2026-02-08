import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. VINTAGE COFFEE STYLE CSS ---
st.set_page_config(page_title="Pranpixl Vintage", page_icon="☕", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Lora:ital,wght@0,400;0,700;1,400&display=swap');

    /* Global Aesthetic: Coffee & Cream */
    [data-testid="stHeader"] {display:none !important;}
    .block-container { padding: 0 !important; max-width: 100% !important; }
    
    .stApp { 
        background-color: #f4ece1 !important; 
        color: #3e2723 !important; 
        font-family: 'Lora', serif; 
    }

    /* TOP BAR: Vintage Ivory */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 3rem;
        background: #efebe9;
        border-bottom: 2px solid #d7ccc8;
        width: 100%;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .nav-logo { 
        display: flex; 
        align-items: center; 
        gap: 12px; 
        font-family: 'Playfair Display', serif; 
        font-size: 26px; 
        font-weight: 900;
        color: #3e2723; 
        letter-spacing: 1px;
    }
    .logo-seal { 
        width: 35px; height: 35px; 
        background: #5d4037; 
        border-radius: 50%; 
        border: 2px double #d7ccc8;
    }

    /* Coffee-Box Language Dropdown */
    div[data-baseweb="select"] {
        border: 2px solid #5d4037 !important;
        border-radius: 4px !important;
        background: #fdfbf9 !important;
        min-width: 130px !important;
    }

    /* MAIN SPLIT LAYOUT */
    .main-container { display: flex; height: calc(100vh - 80px); }

    /* LEFT SIDE: UPLOAD ZONE (Deep Espresso) */
    .upload-sidebar {
        width: 380px;
        background: #2b1b17;
        padding: 40px 25px;
        color: #d7ccc8;
        display: flex;
        flex-direction: column;
        border-right: 4px double #5d4037;
    }

    /* Customizing the Uploader for the Vintage Look */
    [data-testid="stFileUploader"] {
        background: #3e2723 !important;
        border: 1px dashed #d7ccc8 !important;
        border-radius: 8px !important;
        padding: 25px !important;
    }
    [data-testid="stFileUploaderDropzone"] > div { display: none !important; }

    /* RIGHT SIDE: RESULTS (Parchment) */
    .results-area {
        flex-grow: 1;
        padding: 50px 70px;
        background: #fdfbf9;
        overflow-y: auto;
    }

    /* 1/16th RESULT STRIP (Aged Leather Style) */
    .result-strip {
        display: flex;
        align-items: center;
        background: #efebe9;
        padding: 20px;
        border-radius: 4px;
        border: 1px solid #d7ccc8;
        border-left: 8px solid #5d4037;
        margin-bottom: 45px;
    }

    /* MARKETPLACE CARDS (Vintage Label Style) */
    .market-grid {
        display: flex;
        overflow-x: auto;
        gap: 25px;
        padding-bottom: 30px;
        scrollbar-width: thin;
        scrollbar-color: #d7ccc8 transparent;
    }

    .market-card {
        min-width: 300px;
        background: #fdfbf9;
        color: #3e2723;
        border: 1px solid #d7ccc8;
        border-radius: 2px;
        padding: 30px;
        position: relative;
        box-shadow: 5px 5px 0px #d7ccc8;
    }
    .best-deal { 
        border: 2px solid #5d4037 !important; 
        background: #efebe9 !important;
        box-shadow: 8px 8px 0px #5d4037; 
    }
    
    /* FEEDBACK BUTTON (Wax Seal Style) */
    .feedback-btn {
        position: fixed;
        bottom: 40px;
        right: 40px;
        background: #795548;
        color: #f4ece1 !important;
        padding: 18px 35px;
        border-radius: 4px;
        font-weight: 700;
        font-family: 'Playfair Display', serif;
        text-decoration: none;
        z-index: 1000;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
        border: 1px solid #5d4037;
    }

    .price-tag { font-size: 2.4rem; font-family: 'Playfair Display', serif; font-weight: 900; color: #2b1b17; margin: 15px 0; }
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
            <div class="logo-seal"></div> PRANPIXL
        </div>
        <div id="dropdown-anchor"></div>
    </div>
""", unsafe_allow_html=True)

# Main Dashboard Layout
col_side, col_main = st.columns([1, 3.2])

with col_side:
    st.markdown('<div class="upload-sidebar">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family:Playfair Display; color:#efebe9;'>The Ledger</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px; opacity:0.7;'>Place your item here for appraisal</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    st.markdown("<hr style='border: 0.5px solid #5d4037; opacity:0.3; margin-top:30px;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-style:italic; font-size:12px; opacity:0.5;'>Vintage AI Processing Engine v2.0</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_main:
    if not uploaded_file:
        st.markdown("""
            <div style="text-align:center; margin-top:120px; color:#d7ccc8;">
                <h1 style="font-family:'Playfair Display'; font-size:60px; opacity:0.1;">PRANPIXL</h1>
                <p style="font-family:'Lora'; font-style:italic; letter-spacing:2px; opacity:0.3;">ESTABLISHED 2026</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        # RESULTS PAGE
        model = load_engine()
        img = Image.open(uploaded_file)
        
        with st.spinner("Appraising your item..."):
            img_p = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        st.markdown("<h1 style='font-family:Playfair Display;'>Appraisal Report</h1>", unsafe_allow_html=True)
        
        # 1/16th Thumb Strip
        st.markdown('<div class="result-strip">', unsafe_allow_html=True)
        c_thumb, c_name = st.columns([1, 15])
        with c_thumb:
            st.image(img, use_container_width=True)
        with c_name:
            st.markdown(f"<h3 style='margin:0; color:#2b1b17; font-family:Playfair Display;'>{label}</h3><p style='color:#5d4037; font-style:italic; margin:0;'>Authenticated Discovery</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Marketplace
        st.markdown("<h4 style='font-family:Playfair Display; border-bottom:1px solid #d7ccc8; padding-bottom:10px;'>Current Market Listings</h4>", unsafe_allow_html=True)
        platforms = [
            {"name": "Antique Amazon", "price": 12999, "is_best": False},
            {"name": "Heritage Flipkart", "price": 11450, "is_best": True},
            {"name": "Boutique Tata", "price": 13200, "is_best": False}
        ]

        html_market = '<div class="market-grid">'
        for p in platforms:
            cls = "market-card best-deal" if p['is_best'] else "market-card"
            badge = '<div style="position:absolute; top:-10px; right:15px; background:#5d4037; color:#f4ece1; font-size:10px; font-weight:bold; padding:4px 12px; border-radius:2px; letter-spacing:1px;">FINEST VALUE</div>' if p['is_best'] else ""
            html_market += f"""
            <div class="{cls}">
                {badge}
                <p style="color:#5d4037; font-size:11px; font-weight:bold; letter-spacing:2px; text-transform:uppercase;">{p['name']}</p>
                <div class="price-tag">₹{p['price']:,}</div>
                <hr style="border:0.5px solid #d7ccc8; margin:20px 0;">
                <p style="font-size:12px; font-style:italic; opacity:0.7;">Listing Verified • Global Archive</p>
                <a href="#" style="display:inline-block; margin-top:15px; color:#5d4037; font-weight:bold; text-decoration:underline;">ACQUIRE ITEM</a>
            </div>
            """
        html_market += '</div>'
        st.markdown(html_market, unsafe_allow_html=True)

# Language Selectbox in hidden sidebar
with st.sidebar:
    lang = st.selectbox("Language", ["English", "తెలుగు", "Hindi"])

# FEEDBACK wax-seal button
st.markdown('<a href="#" class="feedback-btn">SEND DISPATCH</a>', unsafe_allow_html=True)
