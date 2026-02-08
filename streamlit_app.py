import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="PRANPIXL", page_icon="🖼️")

# 2. THE TOTAL OVERRIDE CSS
# This forces the header and sidebar to stay locked regardless of Streamlit's grid.
st.markdown("""
<style>
    /* Kill all default Streamlit margins and headers */
    [data-testid="stHeader"] {display: none;}
    .reportview-container .main .block-container {padding: 0 !important;}
    .stApp {margin: 0; padding: 0;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    :root {
        --header-h: 50px;
        --sidebar-w: 30vw;
        --accent: #00ffcc;
        --dark-bg: #0b0b0b;
        --side-bg: #1a1612;
        --paper-bg: #ece0d1;
    }

    /* THE LOCKED HEADER */
    .fixed-header {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: var(--header-h);
        background-color: var(--dark-bg);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 25px;
        z-index: 999999;
        border-bottom: 1px solid #222;
        font-family: sans-serif;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo-sq {
        width: 22px; height: 22px;
        background-color: var(--accent);
        border-radius: 4px;
    }

    .brand-txt {
        color: white;
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
    }

    /* THE LOCKED BODY */
    .app-viewport {
        display: flex;
        margin-top: var(--header-h);
        height: calc(100vh - var(--header-h));
        width: 100vw;
        position: fixed;
    }

    .side-panel {
        width: var(--sidebar-w);
        background-color: var(--side-bg);
        border-right: 1px solid #222;
        padding: 40px 30px;
        color: #d1c4b9;
    }

    .main-panel {
        flex: 1;
        background-color: var(--paper-bg);
        padding: 50px;
        overflow-y: auto;
        color: #251e18;
    }

    /* FIXING THE LANGUAGE SELECTOR POSITION */
    .stPopover {
        position: fixed !important;
        top: 8px !important;
        right: 25px !important;
        z-index: 1000000 !important;
    }

    .stPopover > button {
        background-color: #1a1a1a !important;
        color: #ddd !important;
        border: 1px solid #333 !important;
        height: 32px !important;
        font-size: 0.8rem !important;
        border-radius: 4px !important;
    }
</style>

<div class="fixed-header">
    <div class="brand">
        <div class="logo-sq"></div>
        <div class="brand-txt">PRANPIXL</div>
    </div>
    <div></div> </div>
""", unsafe_allow_html=True)

# 3. INTERACTIVE WIDGETS
# This popover is now pinned to the top-right via the CSS above
with st.popover("English ▾"):
    lang_choice = st.radio("Language", ["English", "Hindi", "French"], label_visibility="collapsed")

# 4. MAIN LAYOUT CONTENT
st.markdown(f"""
<div class="app-viewport">
    <div class="side-panel">
        <h2 style="color: #c0a080; font-family: 'Georgia', serif; margin-top: 0;">The Blend</h2>
        <p style="font-size: 0.9rem; opacity: 0.8;">Controls and uploads go here.</p>
        <p style="margin-top: 20px; color: var(--accent);">Active: {lang_choice}</p>
    </div>
    <div class="main-panel">
        <h1 style="font-family: 'Georgia', serif; border-bottom: 2px solid #3d2b1f; padding-bottom: 15px; margin-top: 0;">
            Workspace
        </h1>
        <p style="margin-top: 30px; line-height: 1.6;">
            The layout is now <b>Hard-Locked</b>. By using a 100vw fixed viewport and pinning the 
            Streamlit popover with <i>!important</i> CSS tags, the "abnormal" jumping should stop.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
