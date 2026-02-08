import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- 1. THE ARCHITECTURAL CSS ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700;900&display=swap');

    /* Remove Streamlit padding and Header bar */
    [data-testid="stHeader"] {display:none !important;}
    .block-container {
        padding: 2rem 4rem !important;
        max-width: 100% !important;
    }
    .stApp { background: #080a0f !important; color: white !important; font-family: 'Inter', sans-serif; }

    /* HEADER: Left-Aligned Logo & Right-Aligned Green Dropdown */
    .header-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        margin-bottom: 4rem;
    }
    .brand-id { display: flex; align-items: center; gap: 12px; }
    .brand-logo { width: 32px; height: 32px; background: #00ffcc; border-radius: 8px; }
    .brand-name { font-family: 'Syncopate', sans-serif; font-size: 22px; letter-spacing: 2px; }

    /* The "Green Box" Language Dropdown */
    div[data-baseweb="select"] {
        border: 2px solid #00ffcc !important;
        border-radius: 8px !important;
        background: rgba(0, 255, 204, 0.05) !important;
        min-width: 130px !important;
    }

    /* THE BODY: Single Large Upload Rect with Corner Brackets */
    [data-testid="stFileUploader"] {
        max-width: 800px;
        margin: 5rem auto !important;
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 30px !important;
        padding: 80px 20px !important;
        position: relative;
    }

    /* Decorative Corner Lines (The Brackets) */
    [data-testid="stFileUploader"]::before, [data-testid="stFileUploader"]::after {
        content: "";
        position: absolute;
        width: 40px;
        height: 40px;
        border: 3px solid #00ffcc;
        z-index: 5;
    }

    /* Top Left Bracket */
    [data-testid="stFileUploader"]::before {
        top: -10px;
        left: -10px;
        border-right: none;
        border-bottom: none;
        border-radius: 15px 0 0 0;
    }

    /* Bottom Right Bracket (Simulated via Container shadow/pseudo) */
    /* Note: Streamlit limits multiple pseudos, so we use a shadow-glow to mimic the bottom line */
    [data-testid="stFileUploader"] {
        box-shadow: 10px 10px 0px -5px rgba(0, 255, 204, 0.1);
    }

    [data-testid="stFileUploader"]:hover { border-color: #00ffcc !important; }
    
    /* Hiding the clumsy default elements inside the uploader */
    [data-testid="stFileUploaderDropzone"] > div { display: none !important; }
    [data-testid="stFileUploaderDropzone"] { border: none !important; background: transparent !important; }
    .st-emotion-cache-16ids93 { display: none !important; }

    /* PAGE 2: RESULT (1/16th Scale) */
    .scan-confirmed {
        display: flex;
        align-items: center;
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #00ffcc;
        margin: 40px 0;
    }

    /* HORIZONTAL SCROLL DEALS */
    .deal-container {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 20px 0;
        scrollbar-width: none;
    }
    .deal-container::-webkit-scrollbar { display: none; }

    .deal-card {
        min-width: 330px;
        background: #0d1117;
        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        position: relative;
    }

    /* Glossy Best Deal Highlight */
    .glossy-deal {
        border: 1px solid #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }
    .deal-badge {
        position: absolute;
        top: -10px;
        right: 20px;
        background: #00ffcc;
        color: black;
        font-size: 10px;
        font-weight: 900;
        padding: 4px 12px;
        border-radius: 50px;
    }

    /* FLYING FEEDBACK */
    .float-feedback {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: black !important;
        padding: 16px 32px;
        border-radius: 100px;
        font-weight: 800;
        text-decoration: none;
        box-shadow: 0 10px 30px rgba(0, 255, 204, 0.4);
        z-index: 10000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE APP LOGIC ---
@st.cache_resource
def load_ai():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

def main():
    # HEADER
    col_l, col_r = st.columns([4, 1])
    with col_l:
        st.markdown("""
            <div class="brand-id">
                <div class="brand-logo"></div>
                <div class="brand-name">PRANPIXL</div>
            </div>
            <p style="opacity:0.4; font-size:10px; letter-spacing:1px; margin-top:5px;">ADVANCED VISUAL INTELLIGENCE</p>
        """, unsafe_allow_html=True)
    with col_r:
        lang = st.selectbox("", ["English", "తెలుగు", "Hindi"], label_visibility="collapsed")

    # HOME PAGE: THE SINGLE RECTANGLE UPLOADER
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if not uploaded_file:
        st.markdown("<p style='text-align:center; opacity:0.3; margin-top:20px;'>Drop your image here or click to browse</p>", unsafe_allow_html=True)
    else:
        # RESULTS PAGE
        model = load_ai()
        img = Image.open(uploaded_file)
        
        with st.spinner("Analyzing..."):
            img_p = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # 1/16th THUMBNAIL VIEW
        st.markdown('<div class="scan-confirmed">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 15]) 
        with c1:
            st.image(img, use_container_width=True)
        with c2:
            st.markdown(f"<h2 style='margin:0; padding-left:15px;'>{label} <span style='color:#00ffcc; font-size:14px;'>• Verified</span></h2>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # MARKETPLACE COMPARISON
        platforms = [
            {"name": "Amazon", "price": 12999, "desc": "Next-day delivery available. 4.8/5 Rated."},
            {"name": "Flipkart", "price": 11450, "desc": "Bank Offers active. Fastest shipping."},
            {"name": "Myntra", "price": 13200, "desc": "Premium Authenticity Guarantee."}
        ]
        
        min_p = min(p['price'] for p in platforms)
        
        html_row = '<div class="deal-container">'
        for p in platforms:
            is_best = p['price'] == min_p
            style = "deal-card glossy-deal" if is_best else "deal-card"
            badge = '<div class="deal-badge">BEST DEAL</div>' if is_best else ""
            
            html_row += f"""
            <div class="{style}">
                {badge}
                <p style="color:#00ffcc; font-size:0.75rem; font-weight:800;">{p['name'].upper()}</p>
                <h3 style="margin:10px 0;">{label}</h3>
                <div style="font-size:2.2rem; font-weight:900; margin:10px 0;">₹{p['price']:,}</div>
                <p style="font-size:0.8rem; opacity:0.5; margin-bottom:20px;">{p['desc']}</p>
                <a href="#" style="display:block; background:white; color:black; text-align:center; padding:12px; border-radius:12px; font-weight:bold; text-decoration:none;">GET DEAL</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLYING FEEDBACK BUTTON
    st.markdown('<a href="mailto:support@pranpixl.com" class="float-feedback">🚀 Feedback & Queries</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
