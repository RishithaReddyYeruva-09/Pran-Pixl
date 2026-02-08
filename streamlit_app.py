import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. CSS for No-Scroll, Centralized Layout & Brown Watermark
st.markdown("""
    <style>
    /* 1. LOCK SCREEN (No Scrolling) */
    html, body, [data-testid="stAppViewContainer"] {
        overflow: hidden;
        height: 100vh;
        background-color: #D7CCC8; /* Classic Latte */
    }

    /* 2. THE WATERMARK - Rich Coffee Brown */
    .watermark-container {
        position: fixed;
        top: 55%;
        left: 55%;
        transform: translate(-50%, -50%);
        z-index: 0;
        pointer-events: none;
        user-select: none;
    }
    .watermark-text {
        font-size: 14vw;
        font-weight: 900;
        font-style: italic;
        color: #3E2723; /* Darker Chocolate Brown */
        opacity: 0.25; 
        font-family: 'Arial Black', sans-serif;
        white-space: nowrap;
    }

    /* 3. PERMANENT SIDEBAR LINE */
    .vertical-line {
        position: fixed;
        left: 250px; /* Matches your sketch's sidebar width */
        top: 110px;
        bottom: 0;
        border-right: 3px solid #3C2A21;
        z-index: 5;
    }

    /* 4. HEADER STYLING */
    .header-box {
        padding: 20px;
        border-bottom: 3px solid #3C2A21;
        background-color: #D7CCC8;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10;
        position: relative;
    }
    .logo-container {
        border: 3px solid #000;
        padding: 10px 20px;
        background: white;
        font-weight: bold;
        text-align: center;
    }

    /* 5. ENLARGED DROPZONE */
    .stFileUploader {
        width: 100% !important;
        max-width: 500px;
        margin: auto;
    }
    
    /* Make the uploader box taller to fill space without scrolling */
    [data-testid="stFileUploader"] section {
        padding: 80px 20px !important;
        background-color: rgba(255, 255, 255, 0.3);
        border: 2px dashed #3C2A21 !important;
    }

    /* 6. CENTER THE CONTENT */
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        z-index: 10;
        position: relative;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Background Watermark
st.markdown('<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Top Header Layout
h_left, h_mid, h_right = st.columns([1, 4, 1])

with h_left:
    st.markdown('<div class="logo-container">logo</div>', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:bold; color:#3C2A21; margin: 5px 0 0 5px;'>PranPixl</p>", unsafe_allow_html=True)

with h_right:
    st.selectbox("language", ["English", "Arabic", "French"], label_visibility="collapsed")

# Horizontal divider
st.markdown("<div style='border-bottom: 3px solid #3C2A21; width: 100%; margin-top: 10px;'></div>", unsafe_allow_html=True)

# 5. Permanent Grid Line (Sidebar divider)
st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

# 6. Centralized Work Area
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Create a layout where the uploader is prominent
_, center_ui, _ = st.columns([1.5, 2, 1.5])

with center_ui:
    st.markdown("<h3 style='text-align: center; color: #3C2A21; margin-bottom: 20px;'>drang drop the image for scanning</h3>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        # If file is uploaded, show a smaller preview to avoid making the page scroll
        st.image(uploaded_file, width=250)
        st.success("Ready!")

st.markdown('</div>', unsafe_allow_html=True)
