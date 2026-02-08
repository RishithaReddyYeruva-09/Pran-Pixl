import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. CSS for Centralized Large Uploader & Strong Brown Watermark
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #D7CCC8; 
    }

    /* THE WATERMARK - Deep Brown and Centered */
    .watermark-container {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 0;
        pointer-events: none;
        user-select: none;
        text-align: center;
    }

    .watermark-text {
        font-size: 12vw;
        font-weight: 900;
        font-style: italic;
        color: #4E3629; /* Solid Coffee Brown */
        opacity: 0.3; /* Adjusted for clear visibility */
        font-family: 'Arial Black', sans-serif;
        letter-spacing: 10px;
    }

    /* Header styling */
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
        margin: 10px 0px 40px 0px;
    }

    /* ENLARGED FILE UPLOADER */
    [data-testid="stFileUploader"] {
        width: 600px !important;
        margin: 0 auto;
        padding: 50px !important;
        background-color: rgba(255, 255, 255, 0.2);
        border: 3px dashed #3C2A21 !important;
        border-radius: 20px;
    }
    
    /* Make sure the text inside the uploader is visible */
    [data-testid="stFileUploader"] section {
        padding: 40px !important;
    }

    /* Permanent Sidebar Line (Empty but visual) */
    .vertical-divider {
        border-right: 4px solid #3C2A21;
        height: 80vh;
        position: fixed;
        left: 20%;
        top: 15%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Inject Watermark
st.markdown('<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Header Section
h1, h2, h3 = st.columns([1, 4, 1])
with h1:
    st.markdown('<div class="logo-box">logo</div>', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:bold; color:#3C2A21; margin-top:5px;'>PranPixl</p>", unsafe_allow_html=True)

with h3:
    st.selectbox("language", ["English", "Arabic", "French"], label_visibility="collapsed")

st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)

# 5. Main Layout
# We create the vertical line for the "sidebar" area as a visual element
st.markdown('<div class="vertical-divider"></div>', unsafe_allow_html=True)

# Create a central container for the upload area
_, center_col, _ = st.columns([1, 2, 1])

with center_col:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #3C2A21;'>drang drop the image for scanning</h2>", unsafe_allow_html=True)
    
    # Large, Centered File Uploader
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.markdown("<br>", unsafe_allow_html=True)
        st.image(uploaded_file, caption="Selected Image", use_container_width=True)
        st.success("File Uploaded Successfully")
