import streamlit as st

# 1. Page Config
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Coffee Brown Custom CSS
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #D7CCC8; /* Coffee Cream */
    }

    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }

    /* Left Panel (The 'Sidebar' area) */
    .left-panel {
        border-right: 3px solid #3C2A21;
        height: 100vh;
        padding-right: 20px;
    }

    /* Logo Box from Sketch */
    .logo-box {
        border: 3px solid #000000;
        width: 120px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: white;
        font-weight: bold;
    }

    /* Large PRANPIXL Text */
    .hero-text {
        font-size: clamp(50px, 10vw, 150px);
        font-weight: 800;
        font-style: italic;
        color: #3C2A21;
        text-align: center;
        margin-top: 20vh;
        font-family: 'Arial Black', Gadget, sans-serif;
    }

    /* Drag and Drop Box Area */
    .upload-box {
        border: 2px solid #3C2A21;
        padding: 40px 10px;
        text-align: center;
        margin-top: 50px;
        background-color: #EFEBE9;
    }

    /* Header Divider Line */
    .header-line {
        border-bottom: 3px solid #000000;
        margin-bottom: 0px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Top Header (Logo and Language)
h_col1, h_col2, h_col3 = st.columns([1, 4, 1])

with h_col1:
    st.markdown('<div class="logo-box">logo</div>', unsafe_allow_html=True)
    st.markdown("<p style='margin-top:5px; font-weight:bold;'>PranPixl</p>", unsafe_allow_html=True)

with h_col3:
    # Language Selector (Oval style)
    st.selectbox("language", ["English", "French", "Arabic"], label_visibility="collapsed")

# Horizontal Line across the whole top
st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)

# 4. Main Content Layout (Left Column = Fixed Sidebar, Right Column = Main Page)
# This creates a vertical line that is PERMANENT.
col_left, col_right = st.columns([1, 3])

with col_left:
    # This acts as your sidebar
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; color: #3C2A21; font-weight: 500;'>
            drang drop the image for scanning
        </div>
    """, unsafe_allow_html=True)
    
    # The actual file uploader
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        st.markdown("<p style='text-align:center;'>Image ready.</p>", unsafe_allow_html=True)
    
    # Styling for the vertical divider
    st.markdown("""
        <style>
            [data-testid="column"]:nth-child(1) {
                border-right: 3px solid #3C2A21;
                min-height: 80vh;
            }
        </style>
    """, unsafe_allow_html=True)

with col_right:
    # The big brand name
    st.markdown('<h1 class="hero-text">PRANPIXL</h1>', unsafe_allow_html=True)
