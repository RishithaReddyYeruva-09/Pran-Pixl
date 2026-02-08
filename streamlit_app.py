import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide", initial_sidebar_state="expanded")

# 2. Coffee Brown Style & No-Toggle Sidebar CSS
st.markdown("""
    <style>
    /* 1. Force Sidebar to stay open and hide the toggle button */
    [data-testid="sidebar-button"] {
        display: none !important;
    }
    section[data-testid="stSidebar"] {
        width: 350px !important;
        background-color: #3C2A21; /* Deep Espresso */
        border-right: 3px solid #2A1B15;
    }
    
    /* 2. Main Page Background */
    .stApp {
        background-color: #EDE0D4; /* Light Latte / Cream */
    }
    
    /* 3. Header Styling */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        border-bottom: 3px solid #3C2A21;
        background-color: #EDE0D4;
    }
    
    /* 4. Main Title (PRANPIXL) */
    .main-title {
        font-size: 110px !important;
        font-weight: 900;
        font-style: italic;
        text-align: center;
        color: #3C2A21;
        margin-top: 15vh;
        letter-spacing: -2px;
    }
    
    /* 5. Custom Sidebar Text */
    .sidebar-text {
        color: #EDE0D4 !important;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }

    /* File Uploader styling */
    .stFileUploader {
        padding: 20px;
        background-color: #4E3629;
        border-radius: 15px;
        border: 1px dashed #EDE0D4;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Top Header Section
# Creating a custom header to match the sketch precisely
header_col1, header_col2, header_col3 = st.columns([1, 4, 1])

with header_col1:
    # Logo Box
    st.markdown("""
        <div style="border: 3px solid #3C2A21; padding: 10px; text-align: center; width: 120px; background: white;">
            <b style="color: black;">logo</b>
        </div>
        <div style="color: #3C2A21; font-weight: bold; padding-top: 5px;">PranPixl</div>
    """, unsafe_allow_html=True)

with header_col3:
    # Language Oval (using a styled selectbox)
    st.markdown('<div style="text-align: right;">', unsafe_allow_html=True)
    st.selectbox("language", ["English", "Arabic", "French"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# Divider line
st.markdown("<hr style='border: 1.5px solid #3C2A21; margin-top: 0;'>", unsafe_allow_html=True)

# 4. Sidebar Content (Fixed and Non-Togglable)
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-text'>drang drop the image for scanning</div>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        st.markdown("---")
        st.image(uploaded_file, caption="Image Loaded", use_container_width=True)

# 5. Main Content Area
st.markdown('<h1 class="main-title">PRANPIXL</h1>', unsafe_allow_html=True)

# Optional footer or status
if not uploaded_file:
    st.markdown("<p style='text-align: center; color: #8B5E3C;'>Waiting for image input...</p>", unsafe_allow_html=True)
