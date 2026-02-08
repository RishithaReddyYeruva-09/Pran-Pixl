import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="PRANPIXL", page_icon="🖼️")

# 2. Refined CSS with Vintage-Specific Font Colors
st.markdown("""
<style>
    /* Hide default Streamlit overhead */
    header { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    /* THEME VARIABLES */
    :root {
        --espresso: #251e18;      /* Deep dark brown for main text */
        --mocha: #3d2b1f;         /* Medium brown for headers */
        --latte: #c0a080;         /* Golden tan for sidebar headers */
        --cream: #f5f5dc;         /* Off-white for sidebar body text */
        --paper: #ece0d1;         /* Light background color */
        --accent: #00ffcc;        /* Branding Cyan */
    }

    /* THE TOP HEADER */
    .nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 60px;
        background-color: #111; 
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 30px;
        z-index: 9999;
        border-bottom: 1px solid #333;
    }

    .brand-name {
        color: #FFFFFF; /* Bright white for brand visibility */
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        letter-spacing: 1px;
    }

    /* THE MAIN WRAPPER */
    .main-wrapper {
        display: flex;
        margin-top: 60px; 
        height: calc(100vh - 60px);
        width: 100vw;
    }

    /* SIDEBAR FONT COLORS (Dark background -> Light text) */
    .left-sidebar {
        flex: 1;
        background-color: var(--espresso);
        padding: 40px;
        border-right: 1px solid #444;
        color: var(--cream); /* Default body text color */
    }

    .left-sidebar h2 {
        color: var(--latte) !important; /* Sidebar headers */
        font-family: 'Georgia', serif;
        border-bottom: 1px solid var(--mocha);
        padding-bottom: 10px;
    }

    /* MAIN CONTENT FONT COLORS (Light background -> Dark text) */
    .right-content {
        flex: 2;
        background-color: var(--paper);
        padding: 40px;
        overflow-y: auto;
        color: var(--espresso); /* Main section body text */
    }

    .right-content h1 {
        color: var(--mocha) !important; /* Main page header */
        font-family: 'Georgia', serif;
        border-bottom: 2px solid var(--mocha);
        padding-bottom: 15px;
    }

    /* Streamlit Widget Text Color Correction */
    .stRadio label, .stMarkdown p {
        color: inherit !important;
    }

    /* Popover Button Text */
    div[data-testid="stPopover"] > button {
        background-color: #222 !important;
        color: white !important;
        border: 1px solid #444 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. RENDER HEADER (Logo + Language)
with st.container():
    c1, c2, c3 = st.columns([1, 4, 0.5])
    with c1:
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
                <div style="width: 24px; height: 24px; background-color: var(--accent); border-radius: 4px;"></div>
                <div class="brand-name">PRANPIXL</div>
            </div>
        """, unsafe_allow_html=True)
    
    with c3:
        st.markdown('<div style="margin-top: 12px;">', unsafe_allow_html=True)
        with st.popover("English ▾"):
            lang = st.radio("Language", ["English", "Hindi", "French"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

# 4. RENDER BODY CONTENT
st.markdown(f"""
<div class="nav-bar"></div>
<div class="main-wrapper">
    <div class="left-sidebar">
        <h2>The Blend</h2>
        <p>This text is now in <b>Cream</b> to stand out against the Espresso background.</p>
        <p style="font-style: italic; opacity: 0.8;">Active Language: {lang}</p>
    </div>
    <div class="right-content">
        <h1>Vintage Workspace</h1>
        <p>This text is in <b>Espresso</b> for high readability on the Paper background.</p>
        <p>The font styles are now separated: <b>Georgia Serif</b> for headers and <b>Sans-Serif/System</b> for UI elements to match your reference image.</p>
    </div>
</div>
""", unsafe_allow_html=True)
