import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Strict CSS for No-Scroll and Watermark
st.markdown("""
    <style>
    /* 1. COMPLETELY DISABLE SCROLLING */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"] {
        overflow: hidden !important;
        height: 100vh !important;
        background-color: #D7CCC8 !important; /* Classic Latte */
    }

    /* 2. ENHANCED BROWN WATERMARK */
    .watermark-container {
        position: fixed;
        top: 50%;
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
        color: #5D4037; /* Strong Coffee Brown */
        opacity: 0.2; 
        font-family: 'Arial Black', sans-serif;
        white-space: nowrap;
        letter-spacing: -5px;
    }

    /* 3. HEADER STYLING */
    .logo-container {
        border: 3px solid #000;
        padding: 5px 15px;
        background: white;
        font-weight: bold;
        text-align: center;
        width: fit-content;
    }
    
    .header-divider {
        border-bottom: 4px solid #3E2723;
        width: 100%;
        margin-top: 10px;
    }

    /* 4. CENTERED AND ENLARGED UPLOAD BOX */
    .main-ui-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 75vh; /* Takes up the middle of the screen */
        width: 100%;
        position: relative;
        z-index: 10;
    }

    /* Styling the actual Streamlit File Uploader widget */
    [data-testid="stFileUploader"] {
        width: 700px !important;
    }

    [data-testid="stFileUploader"] section {
        padding: 100px 50px !important;
        background-color: rgba(255, 255, 255, 0.2) !important;
        border: 3px dashed #3E2723 !important;
        border-radius: 30px !important;
    }

    /* Hide the 'Limit 200MB' and other tiny text if desired to keep it clean */
    [data-testid="stFileUploader"] small {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Background Watermark
st.markdown('<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Top Header
h1, h2, h3 = st.columns([1, 4, 1])
with h1:
    st.markdown('<div class="logo-container">logo</div>', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:bold; color:#3E2723; margin: 2px 0 0 0;'>PranPixl</p>", unsafe_allow_html=True)

with h3:
    st.selectbox("lang", ["English", "Arabic", "French"], label_visibility="collapsed")

st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)

# 5. Centered UI Layout
st.markdown('<div class="main-ui-container">', unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #3E2723; font-family: sans-serif; margin-bottom: 30px;'>drang drop the image for scanning</h2>", unsafe_allow_html=True)

# The large uploader
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if uploaded_file:
    st.image(uploaded_file, width=300)
    st.success("Ready to scan!")

st.markdown('</div>', unsafe_allow_html=True)
