import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Enhanced Coffee Brown & Visible Watermark CSS
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #D7CCC8; 
    }

    /* THE WATERMARK - Adjusted for high visibility */
    .watermark-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 0; /* Sits just above the background but below widgets */
        pointer-events: none;
        user-select: none;
    }

    .watermark-text {
        font-size: 15vw;
        font-weight: 900;
        font-style: italic;
        color: #5D4037; /* Rich Coffee Brown */
        opacity: 0.25; /* Adjusted so it's visible but doesn't block text */
        font-family: 'Arial Black', sans-serif;
        transform: rotate(-5deg); /* Slight tilt for that 'mark' look */
    }

    /* Bring the main content to the front */
    [data-testid="column"] {
        z-index: 10 !important;
    }

    /* Sidebar Divider Styling */
    [data-testid="column"]:nth-child(1) {
        border-right: 3px solid #3C2A21 !important;
        min-height: 90vh;
    }

    /* Header Styling */
    .logo-box {
        border: 3px solid #000;
        padding: 10px 20px;
        background: white;
        font-weight: bold;
        display: inline-block;
    }

    .header-divider {
        border-bottom: 4px solid #3C2A21;
        width: 100%;
        margin: 10px 0px 20px 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Inject Watermark into the background layer
st.markdown('<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Top Header
h1, h2, h3 = st.columns([1, 4, 1])
with h1:
    st.markdown('<div class="logo-box">logo</div>', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:bold; color:#3C2A21; margin-top:5px;'>PranPixl</p>", unsafe_allow_html=True)

with h3:
    st.selectbox("language", ["English", "Arabic", "French"], label_visibility="collapsed")

st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)

# 5. Fixed Main Grid (No-Toggle Sidebar)
col_left, col_right = st.columns([1, 3.5])

with col_left:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #3C2A21; font-weight: bold;'>drang drop the image for scanning</p>", unsafe_allow_html=True)
    
    # Drag and Drop interaction
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        st.success("Ready for Scan")

with col_right:
    # This remains empty so the watermark shows through the background
    pass
