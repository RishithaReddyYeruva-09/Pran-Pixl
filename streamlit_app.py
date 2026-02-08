import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Coffee Brown Theme CSS
st.markdown("""
    <style>
    /* Main Background and Text */
    .stApp {
        background-color: #F5F5DC; /* Cream/Beige background */
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #3C2A21; /* Dark Espresso */
        border-right: 2px solid #6F4E37;
    }
    
    /* Change sidebar text to light cream */
    section[data-testid="stSidebar"] .stText, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h2 {
        color: #F5F5DC !important;
    }

    /* Main Title Styling */
    .main-title {
        font-size: 100px !important;
        font-weight: 800;
        font-style: italic;
        text-align: center;
        margin-top: 120px;
        color: #3C2A21; /* Espresso Brown */
        letter-spacing: 5px;
        text-shadow: 2px 2px #D2B48C;
    }
    
    /* Header styling */
    .header-line {
        border-bottom: 3px solid #3C2A21;
        margin-bottom: 20px;
    }

    /* File Uploader Box Customization */
    section[data-testid="stFileUploader"] {
        background-color: #4E3629;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
col_logo, col_empty, col_lang = st.columns([1, 4, 1])

with col_logo:
    # Small logo placeholder
    st.markdown("<div style='border: 2px solid #3C2A21; padding: 5px; text-align: center; font-weight: bold;'>LOGO</div>", unsafe_allow_html=True)
    st.markdown("<p style='color: #3C2A21; font-weight: bold; margin-top: 5px;'>PranPixl</p>", unsafe_allow_html=True)

with col_lang:
    st.selectbox("Language", ["English", "Spanish", "French"], label_visibility="collapsed")

st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)

# 4. Sidebar (Upload Area)
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>UPLOAD</h2>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "drang drop the image for scanning", 
        type=["png", "jpg", "jpeg"]
    )
    
    if uploaded_file:
        st.image(uploaded_file, caption="Selected Image", use_container_width=True)

# 5. Main Body
st.markdown('<h1 class="main-title">PRANPIXL</h1>', unsafe_allow_html=True)

# 6. Bottom scan feedback
if uploaded_file:
    st.markdown("<p style='text-align: center; color: #6F4E37;'><i>Ready to scan the pixels...</i></p>", unsafe_allow_html=True)
    
