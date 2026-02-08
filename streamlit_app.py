import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Flexible & Layered CSS
st.markdown("""
    <style>
    /* 1. RESPONSIVE LOCK SCREEN */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main .block-container {
        overflow: hidden !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: #D7CCC8 !important;
    }

    /* 2. FLEXIBLE WATERMARK (Layer 0) */
    .watermark-container {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 0; 
        pointer-events: none;
        text-align: center;
        width: 100%;
    }
    .watermark-text {
        /* font-size adjusts based on screen width */
        font-size: 18vw; 
        font-weight: 900;
        font-style: italic;
        color: #3E2723;
        opacity: 0.25; 
        font-family: 'Arial Black', sans-serif;
        white-space: nowrap;
    }

    /* 3. RESPONSIVE WORKSPACE (Layer 5) */
    .central-workspace {
        position: absolute;
        top: 120px;
        bottom: 20px;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 5;
        padding: 0 5%;
    }

    /* 4. FLEXIBLE UPLOAD BOX */
    [data-testid="stFileUploader"] {
        width: 100% !important;
        max-width: 650px !important; /* Cap width for desktop */
    }
    [data-testid="stFileUploader"] section {
        padding: 5vh 2vw !important; /* Padding scales with screen height/width */
        background-color: rgba(215, 204, 200, 0.6) !important; 
        border: 3px dashed #3E2723 !important;
        border-radius: 25px !important;
        backdrop-filter: blur(3px);
    }

    /* 5. MOBILE ADJUSTMENTS (Media Query) */
    @media (max-width: 768px) {
        .watermark-text { font-size: 22vw; } /* Bigger text for vertical screens */
        [data-testid="stFileUploader"] section { padding: 3vh 2vw !important; }
        .logo-text { font-size: 14px !important; }
    }

    /* 6. HEADER (Top Layer) */
    .custom-header {
        height: 100px;
        padding: 10px 5%;
        border-bottom: 3px solid #3E2723;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #D7CCC8;
        z-index: 10;
        position: relative;
    }
    
    [data-testid="stFileUploader"] small { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. Layer 0: Background Watermark
st.markdown('<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Layer 10: Fixed Responsive Header
st.markdown("""
    <div class="custom-header">
        <div>
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; font-weight: bold; width: fit-content; font-size: 1rem;">logo</div>
            <div class="logo-text" style="font-weight:bold; color:#3E2723; margin-top: 5px; font-family: sans-serif;">PranPixl</div>
        </div>
        <div style="background: white; border-radius: 15px; padding: 5px 12px; border: 2px solid #3E2723;">
            <span style="color: #3E2723; font-weight: bold; font-size: 0.9rem;">English ▾</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Layer 5: Centralized Flexible Workspace
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #3E2723; font-family: sans-serif; margin-bottom: 2vh; font-size: clamp(1.2rem, 3vw, 2rem);'>drang drop the image for scanning</h3>", unsafe_allow_html=True)

# File Uploader
# Using a fluid column width
_, uploader_col, _ = st.columns([1, 6, 1]) if st.session_state.get('mobile', False) else st.columns([1, 2, 1])

with uploader_col:
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        # Image preview also scales based on height to prevent scrolling
        st.image(uploaded_file, use_container_width=False, width=200)
        st.success("Loaded")

st.markdown('</div>', unsafe_allow_html=True)
