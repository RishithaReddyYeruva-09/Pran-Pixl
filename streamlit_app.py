import streamlit as st

# 1. Page Config
st.set_page_config(page_title="PranPixl", layout="wide", initial_sidebar_state="expanded")

# 2. Hard CSS Overrides for Fixed Sidebar and Coffee Theme
st.markdown("""
    <style>
    /* HIDE SIDEBAR TOGGLE BUTTON COMPLETELY */
    [data-testid="sidebar-button"] {
        display: none !important;
    }
    
    /* FORCE SIDEBAR TO STAY OPEN */
    section[data-testid="stSidebar"] {
        min-width: 320px !important;
        max-width: 320px !important;
        background-color: #3C2A21 !important; /* Espresso Brown */
        border-right: 4px solid #2A1B15;
    }

    /* MAIN PAGE BACKGROUND */
    .stApp {
        background-color: #D7CCC8; /* Classic Coffee Cream */
    }

    /* HEADER AREA */
    .header-box {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        padding: 10px 0px;
    }

    /* LOGO BOX */
    .logo-container {
        border: 3px solid #3C2A21;
        padding: 20px;
        background-color: white;
        text-align: center;
        width: 150px;
    }

    /* PRANPIXL MAIN TEXT */
    .main-hero-text {
        font-size: 120px !important;
        font-weight: 900;
        font-style: italic;
        color: #3C2A21;
        text-align: center;
        margin-top: 15vh;
        letter-spacing: -2px;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* LANGUAGE OVAL */
    div[data-baseweb="select"] {
        border-radius: 50px !important;
        border: 2px solid #3C2A21 !important;
    }

    /* SIDEBAR TEXT */
    .sidebar-label {
        color: #D7CCC8 !important;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Top Header Section (Logo and Language)
t1, t2, t3 = st.columns([1, 3, 1])

with t1:
    st.markdown('<div class="logo-container">logo</div>', unsafe_allow_html=True)
    st.markdown("<b style='color:#3C2A21'>PranPixl</b>", unsafe_allow_html=True)

with t3:
    # Styled language selector
    st.selectbox("language", ["English", "French", "Arabic"], label_visibility="collapsed")

# The horizontal line from your sketch
st.markdown("<hr style='border: 2px solid #3C2A21; margin-top: 5px;'>", unsafe_allow_html=True)

# 4. Permanent Sidebar (No Toggle)
with st.sidebar:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">drang drop the image for scanning</div>', unsafe_allow_html=True)
    
    # Drag and Drop Box
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.markdown("<br>", unsafe_allow_html=True)
        st.image(uploaded_file, use_container_width=True)
        st.success("Image Loaded")

# 5. Main Body Text
st.markdown('<h1 class="main-hero-text">PRANPIXL</h1>', unsafe_allow_html=True)
