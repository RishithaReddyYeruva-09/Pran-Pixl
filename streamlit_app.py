import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# 2. "Locked Screen" CSS - No Scroll, Centered UI
st.markdown("""
    <style>
    /* 1. Nuke all scrollbars and force absolute height */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main .block-container {
        overflow: hidden !important;
        height: 100vh !important;
        max-height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: #D7CCC8 !important;
    }

    /* 2. THE BROWN WATERMARK - Centered and Solid */
    .watermark-container {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 0;
        pointer-events: none;
    }
    .watermark-text {
        font-size: 15vw;
        font-weight: 900;
        font-style: italic;
        color: #5D4037; 
        opacity: 0.2; 
        font-family: 'Arial Black', sans-serif;
        white-space: nowrap;
    }

    /* 3. FIXED TOP HEADER (Height-controlled) */
    .custom-header {
        height: 120px;
        padding: 20px 40px;
        border-bottom: 4px solid #3E2723;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        z-index: 100;
        position: relative;
    }

    /* 4. MAIN CENTRAL INTERFACE (Uses Flexbox to stay in view) */
    .central-workspace {
        height: calc(100vh - 150px); /* Total height minus header */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
        position: relative;
    }

    /* 5. ENLARGED UPLOAD AREA */
    [data-testid="stFileUploader"] {
        width: 650px !important;
    }
    [data-testid="stFileUploader"] section {
        padding: 60px !important; /* Slightly smaller to ensure fit on smaller screens */
        background-color: rgba(255, 255, 255, 0.2) !important;
        border: 3px dashed #3E2723 !important;
        border-radius: 30px !important;
    }
    
    /* Hide extra Streamlit info text to save space */
    [data-testid="stFileUploader"] small { display: none; }
    div.stSuccess { position: absolute; bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Watermark Layer
st.markdown('<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Manual Header Construction
st.markdown(f"""
    <div class="custom-header">
        <div>
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; font-weight: bold; width: fit-content;">logo</div>
            <div style="font-weight:bold; color:#3E2723; margin-top: 5px; font-family: sans-serif;">PranPixl</div>
        </div>
        <div style="background: white; border-radius: 20px; padding: 5px 15px; border: 2px solid #3E2723;">
            <span style="color: #3E2723; font-weight: bold;">English ▾</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. The Locked Workspace
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #3E2723; font-family: sans-serif; margin-bottom: 20px;'>drang drop the image for scanning</h2>", unsafe_allow_html=True)

# Using columns just to keep the uploader width in check
_, uploader_col, _ = st.columns([1, 2, 1])
with uploader_col:
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        # Resize image preview so it doesn't break the "no scroll" rule
        st.image(uploaded_file, width=280)
        st.success("File Ready")

st.markdown('</div>', unsafe_allow_html=True)
