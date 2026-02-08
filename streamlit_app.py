import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="PRANPIXL", page_icon="🖼️")

# 2. Precision CSS - Locking the Header and Elements
st.markdown("""
<style>
    header { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    :root {
        --header-height: 48px;
        --accent: #00ffcc;
        --sidebar-bg: #15120f;
        --main-bg: #ece0d1;
    }

    /* THE BLACK BAR - FIXED & Z-INDEXED */
    .nav-bar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: var(--header-height);
        background-color: #0b0b0b;
        z-index: 99999;
        border-bottom: 1px solid #222;
    }

    /* POSITIONING THE LOGO (ABSOLUTE) */
    .logo-container {
        position: fixed;
        top: 13px; /* Centered in 48px height */
        left: 25px;
        display: flex;
        align-items: center;
        gap: 10px;
        z-index: 100000;
        pointer-events: none; /* Allows clicks to pass through if needed */
    }

    .brand-name {
        color: white;
        font-family: sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 0.5px;
    }

    /* THE MAIN WRAPPER */
    .app-body {
        display: flex;
        margin-top: var(--header-height);
        height: calc(100vh - var(--header-height));
        width: 100vw;
    }

    .sidebar {
        flex: 1;
        background-color: var(--sidebar-bg);
        color: #d1c4b9;
        padding: 40px 25px;
    }

    .workspace {
        flex: 2.5;
        background-color: var(--main-bg);
        padding: 40px;
        color: #251e18;
    }

    /* PINNING THE STREAMLIT WIDGET TO THE RIGHT */
    div[data-testid="stPopover"] {
        position: fixed;
        top: 8px !important; /* Fixed in header */
        right: 25px !important;
        z-index: 100000 !important;
    }

    div[data-testid="stPopover"] > button {
        background-color: #1a1a1a !important;
        color: #ccc !important;
        border: 1px solid #333 !important;
        height: 30px !important;
        font-size: 0.75rem !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. RENDER THE LOGO AND BAR
st.markdown(f"""
<div class="nav-bar"></div>
<div class="logo-container">
    <div style="width: 20px; height: 20px; background-color: var(--accent); border-radius: 4px;"></div>
    <div class="brand-name">PRANPIXL</div>
</div>
""", unsafe_allow_html=True)

# 4. RENDER THE LANGUAGE BUTTON (Streamlit pins it via CSS)
with st.popover("English ▾"):
    st.radio("Language", ["English", "Hindi", "French"], label_visibility="collapsed")

# 5. THE CONTENT SPLIT
st.markdown("""
<div class="app-body">
    <div class="sidebar">
        <h2 style="color: #c0a080; font-family: 'Georgia', serif;">The Blend</h2>
        <p style="opacity: 0.7; font-size: 0.9rem;">Sidebar locked to 1/3.</p>
    </div>
    <div class="workspace">
        <h1 style="font-family: 'Georgia', serif; border-bottom: 1px solid #3d2b1f; padding-bottom: 10px;">Workspace</h1>
        <p style="margin-top: 20px;">The header height is strictly 48px. The logo and button are manually pinned to prevent displacement.</p>
    </div>
</div>
""", unsafe_allow_html=True)
