import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    /* Main branding text styling */
    .main-title {
        font-size: 80px !important;
        font-weight: bold;
        font-style: italic;
        text-align: center;
        margin-top: 150px;
        color: #1E1E1E;
    }
    
    /* Header styling */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        border-bottom: 2px solid #000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section (Logo and Language)
col_logo, col_empty, col_lang = st.columns([1, 4, 1])

with col_logo:
    # Placeholder for your logo box
    st.image("https://via.placeholder.com/100x50?text=LOGO", width=120)
    st.write("**PranPixl**")

with col_lang:
    # Language dropdown styled as a pill/button
    st.selectbox("", ["English", "Spanish", "French"], label_visibility="collapsed")

st.markdown("---") # Horizontal line from your drawing

# 4. Sidebar (Drag and Drop Area)
with st.sidebar:
    st.header("Upload Zone")
    uploaded_file = st.file_uploader(
        "drag drop the image for scanning", 
        type=["png", "jpg", "jpeg"]
    )
    
    if uploaded_file:
        st.success("Image uploaded successfully!")
        st.image(uploaded_file, caption="Preview", use_container_width=True)

# 5. Main Body Content
st.markdown('<h1 class="main-title">PRANPIXL</h1>', unsafe_allow_html=True)

# Optional: Add logic for what happens after scanning
if uploaded_file:
    st.info("System ready to scan...")
