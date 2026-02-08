import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. "Layered Overlay" CSS
st.markdown("""
    <style>
    /* 1. LOCK SCREEN (Strict No-Scroll) */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main .block-container {
        overflow: hidden !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: #D7CCC8 !important; /* Classic Latte */
    }

    /* 2. THE WATERMARK - Layer 0 (Bottom) */
    .watermark-container {
        position: fixed;
        top: 55%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 0; 
        pointer-events: none;
        user-select: none;
    }
    .watermark-text {
        font-size: 16vw;
        font-weight: 900;
        font-style: italic;
        color: #3E2723; /* Dark Espresso */
        opacity: 0.4; /* Stronger base opacity */
        font-family: 'Arial Black', sans-serif;
        white-space: nowrap;
    }

    /* 3. THE UPLOAD OVERLAY - Layer 1 (Middle) */
    .central-workspace {
        position: absolute;
        top: 150px; /* Below Header */
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 5; /* Above Watermark */
    }

    /* 4. ENLARGED UPLOAD BOX with Partial Transparency */
    [data-testid="stFileUploader"] {
        width: 750px !important;
    }
    [data-testid="stFileUploader"] section {
        padding: 80px !important;
        /* Semi-transparent white allows watermark to show through partially */
        background-color: rgba(215, 204, 200, 0.7) !important; 
        border: 4px dashed #3E2723 !important;
        border-radius: 40px !important;
        backdrop-filter: blur(2px); /* Optional: adds a slight glass effect */
    }

    /* 5. HEADER (Top Layer) */
    .custom-header {
        height: 120px;
        padding: 20px 40px;
        border-bottom: 4px solid #3E2723;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        background-color: #D7CCC8;
        z-index: 10;
        position: relative;
    }
    
    [data-testid="stFileUploader"] small { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. Layer 0: Background Watermark
st.markdown('<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Layer 10: Fixed Header
st.markdown("""
    <div class="custom-header">
        <div>
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; font-weight: bold; width: fit-content;">logo</div>
            <div style="font-weight:bold; color:#3E2723; margin-top: 5px; font-family: sans-serif;">PranPixl</div>
        </div>
        <div style="background: white; border-radius: 20px; padding: 5px 15px; border: 2px solid #3E2723; cursor: pointer;">
            <span style="color: #3E2723; font-weight: bold;">English ▾</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Layer 5: Centralized Overlay Workspace
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #3E2723; font-family: sans-serif; margin-bottom: 20px; text-shadow: 1px 1px 2px white;'>drang drop the image for scanning</h2>", unsafe_allow_html=True)

# Centered Uploader
_, uploader_col, _ = st.columns([1, 3, 1])
with uploader_col:
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.image(uploaded_file, width=300)
        st.success("File Ready for Scan")

st.markdown('</div>', unsafe_allow_html=True)
