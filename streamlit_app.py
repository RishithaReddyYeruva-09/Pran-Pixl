import streamlit as st

# 1. Page Configuration - Locked to single screen
st.set_page_config(page_title="PranPixl", layout="wide")

# Initialize theme state
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Theme & Responsive CSS
if st.session_state.theme == 'light':
    bg_color = "#D7CCC8"      # Latte Cream
    text_color = "#3E2723"    # Deep Espresso
    box_bg = "rgba(255, 255, 255, 0.4)"
    border_color = "#3E2723"
    watermark_opacity = "0.2"
else:
    bg_color = "#1B1411"      # Black Coffee
    text_color = "#D7CCC8"    # Latte Cream text
    box_bg = "rgba(62, 39, 35, 0.6)"
    border_color = "#D7CCC8"
    watermark_opacity = "0.15"

st.markdown(f"""
    <style>
    /* 1. PREVENT SCROLLING */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main .block-container {{
        overflow: hidden !important;
        height: 100vh !important;
        background-color: {bg_color} !important;
        margin: 0 !important;
        padding: 0 !important;
    }}

    /* 2. WATERMARK - Layer 0 */
    .watermark-container {{
        position: fixed;
        top: 55%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 0; 
        pointer-events: none;
    }}
    .watermark-text {{
        font-size: 16vw; 
        font-weight: 900;
        font-style: italic;
        color: {text_color};
        opacity: {watermark_opacity}; 
        font-family: 'Arial Black', sans-serif;
        white-space: nowrap;
    }}

    /* 3. HEADER - Top Layer */
    .custom-header {{
        height: 100px;
        padding: 10px 5%;
        border-bottom: 3px solid {border_color};
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: {bg_color};
        z-index: 10;
        position: relative;
    }}

    /* 4. OVERLAY UPLOAD BOX */
    .central-workspace {{
        position: absolute;
        top: 120px;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 5;
    }}

    [data-testid="stFileUploader"] section {{
        padding: 5vh 2vw !important;
        background-color: {box_bg} !important; 
        border: 3px dashed {border_color} !important;
        border-radius: 30px !important;
        backdrop-filter: blur(4px);
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. Layer 0: Background Watermark
st.markdown(f'<div class="watermark-container"><div class="watermark-text">PRANPIXL</div></div>', unsafe_allow_html=True)

# 4. Header with Buttons Side-by-Side
h_left, h_right = st.columns([1, 1])

with h_left:
    st.markdown(f"""
        <div style="padding-left: 5%;">
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; color: black; font-weight: bold; width: fit-content;">logo</div>
            <div style="font-weight:bold; color:{text_color}; margin-top: 5px;">PranPixl</div>
        </div>
    """, unsafe_allow_html=True)

with h_right:
    # Nested columns to put buttons side-by-side
    btn_col1, btn_col2 = st.columns([1, 1])
    
    with btn_col1:
        # Theme Toggle Button
        theme_label = "☕ Dark Roast" if st.session_state.theme == 'light' else "🥛 Light Latte"
        if st.button(theme_label, use_container_width=True):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()

    with btn_col2:
        # Language Selector
        st.selectbox("lang", ["English", "Arabic", "French"], label_visibility="collapsed")

# Divider
st.markdown(f"<div style='border-bottom: 3px solid {border_color}; width: 100%;'></div>", unsafe_allow_html=True)

# 5. Central Workspace Overlay
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)

st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-bottom: 2vh; font-size: clamp(1rem, 3vw, 2rem);'>drang drop the image for scanning</h3>", unsafe_allow_html=True)

# Responsive uploader width
_, uploader_col, _ = st.columns([1, 3, 1])
with uploader_col:
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    
    if uploaded_file:
        st.image(uploaded_file, width=200)
        st.success("Ready!")

st.markdown('</div>', unsafe_allow_html=True)
