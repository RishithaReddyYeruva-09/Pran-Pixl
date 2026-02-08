import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Coffee Brown & Fixed Watermark CSS
st.markdown("""
    <style>
    /* Main Background - Latte Cream */
    .stApp {
        background-color: #D7CCC8; 
    }

    /* THE WATERMARK - Adjusted to a clearer Brown */
    .watermark {
        position: fixed;
        top: 60%;
        left: 60%;
        transform: translate(-50%, -50%);
        font-size: 10vw; 
        font-weight: 900;
        font-style: italic;
        /* Using a solid Coffee Brown with slight opacity */
        color: rgba(60, 42, 33, 0.4); 
        z-index: -1; 
        user-select: none;
        pointer-events: none;
        white-space: nowrap;
        font-family: 'Arial Black', Gadget, sans-serif;
        text-transform: uppercase;
    }

    /* Force the first column to look like a permanent sidebar */
    [data-testid="column"]:nth-child(1) {
        border-right: 4px solid #3C2A21 !important;
        min-height: 100vh;
        padding-right: 25px !important;
    }

    /* Header styling to match the drawing */
    .logo-box {
        border: 3px solid #000;
        padding: 10px 20px;
        background: white;
        font-weight: bold;
        display: inline-block;
        color: #000;
    }

    .header-divider {
        border-bottom: 4px solid #3C2A21;
        width: 100%;
        margin-bottom: 20px;
    }

    /* Styling for the File Uploader area */
    .stFileUploader {
        border: 2px dashed #3C2A21;
        border-radius: 10px;
        background-color: rgba(60, 42, 33, 0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Watermark
st.markdown('<div class="watermark">PRANPIXL</div>', unsafe_allow_html=True)

# 4. Header (Logo on Left, Language on Right)
h1, h2, h3 = st.columns([1, 4, 1])
with h1:
    st.markdown('<div class="logo-box">logo</div>', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:bold; color:#3C2A21; margin-top:5px;'>PranPixl</p>", unsafe_allow_html=True)

with h3:
    # Language selector (styled oval)
    st.selectbox("lang", ["English", "Arabic", "French"], label_visibility="collapsed")

st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)

# 5. Fixed Grid (Left Sidebar + Main Area)
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
    # This remains empty so the watermark is fully visible
    pass
