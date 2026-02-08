import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. Coffee Brown & Watermark CSS
st.markdown("""
    <style>
    /* Main Background - Classic Coffee Cream */
    .stApp {
        background-color: #D7CCC8; 
    }

    /* WATERMARK EFFECT */
    .watermark {
        position: fixed;
        top: 55%;
        left: 60%;
        transform: translate(-50%, -50%);
        font-size: 12vw; /* Responsive large text */
        font-weight: 900;
        font-style: italic;
        color: rgba(60, 42, 33, 0.1); /* Very faint espresso brown */
        z-index: -1; /* Pushes it behind all other elements */
        user-select: none;
        pointer-events: none;
        white-space: nowrap;
        font-family: 'Arial Black', sans-serif;
    }

    /* REMOVE PADDING */
    .block-container {
        padding: 0rem;
        max-width: 100%;
    }

    /* HEADER AREA */
    .header-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 40px;
        border-bottom: 3px solid #3C2A21;
        background-color: #D7CCC8;
    }

    /* LOGO BOX */
    .logo-box {
        border: 3px solid #000;
        padding: 15px 30px;
        background: white;
        font-weight: bold;
        text-align: center;
    }

    /* PERMANENT SIDEBAR COLUMN (STILL NO TOGGLE) */
    [data-testid="column"]:nth-child(1) {
        border-right: 3px solid #3C2A21;
        min-height: 90vh;
        padding: 40px !important;
        background-color: rgba(60, 42, 33, 0.05); /* Slight tint for sidebar */
    }

    /* LANGUAGE SELECTOR OVAL */
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 30px !important;
        border: 2px solid #3C2A21 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Watermark (Placed first so it stays in the background)
st.markdown('<div class="watermark">PRANPIXL</div>', unsafe_allow_html=True)

# 4. Top Header
h_left, h_mid, h_right = st.columns([1, 3, 1])
with h_left:
    st.markdown('<div style="padding-left: 20px;"><div class="logo-box">logo</div><div style="font-weight:bold; color:#3C2A21; margin-top:5px;">PranPixl</div></div>', unsafe_allow_html=True)

with h_right:
    st.markdown('<div style="padding-right: 20px; padding-top:10px;">', unsafe_allow_html=True)
    st.selectbox("lang", ["English", "Arabic", "French"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# Horizontal line divider
st.markdown("<div style='border-bottom: 3px solid #3C2A21; width: 100%;'></div>", unsafe_allow_html=True)

# 5. Fixed Main Layout
# col_sidebar is the left panel, col_main is the workspace
col_sidebar, col_main = st.columns([1, 3])

with col_sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #3C2A21;'>drang drop the image for scanning</p>", unsafe_allow_html=True)
    
    # The Uploader
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        st.success("Loaded")

with col_main:
    # This column is empty but holds the space over the watermark.
    # You can add results or buttons here later.
    pass
