import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="PRANPIXL", page_icon="🖼️")

# 2. Tightened CSS
st.markdown("""
<style>
    /* Hide default Streamlit overhead */
    header { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    :root {
        --espresso: #251e18;
        --mocha: #3d2b1f;
        --latte: #c0a080;
        --cream: #f5f5dc;
        --paper: #ece0d1;
        --accent: #00ffcc;
    }

    /* REDUCED HEADER SIZE (From 60px/70px to 45px) */
    .nav-bar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 45px;
        background-color: #111; 
        z-index: 9999;
        border-bottom: 1px solid #333;
    }

    /* THE MAIN WRAPPER (Offset by new header height) */
    .main-wrapper {
        display: flex;
        margin-top: 45px; 
        height: calc(100vh - 45px);
        width: 100vw;
    }

    .brand-name {
        color: #FFFFFF;
        font-family: sans-serif;
        font-weight: 700;
        font-size: 0.9rem; /* Smaller font */
        letter-spacing: 0.5px;
    }

    /* Content Panels */
    .left-sidebar {
        flex: 1;
        background-color: var(--espresso);
        padding: 25px; /* Reduced padding */
        border-right: 1px solid #444;
        color: var(--cream);
    }

    .right-content {
        flex: 2;
        background-color: var(--paper);
        padding: 30px; /* Reduced padding */
        overflow-y: auto;
        color: var(--espresso);
    }

    /* Make the Popover button tiny to fit the header */
    div[data-testid="stPopover"] > button {
        background-color: #222 !important;
        color: white !important;
        border: 1px solid #444 !important;
        height: 28px !important; /* Shorter button */
        padding: 0 10px !important;
        font-size: 0.75rem !important;
        margin-top: -5px; /* Alignment tweak */
    }
</style>
""", unsafe_allow_html=True)

# 3. RENDER TIGHT HEADER
with st.container():
    # Columns for the tiny header
    c1, c2, c3 = st.columns([1.5, 5, 1])
    with c1:
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px;">
                <div style="width: 20px; height: 20px; background-color: var(--accent); border-radius: 3px;"></div>
                <div class="brand-name">PRANPIXL</div>
            </div>
        """, unsafe_allow_html=True)
    
    with c3:
        st.markdown('<div style="margin-top: 6px; text-align: right;">', unsafe_allow_html=True)
        with st.popover("English ▾"):
            lang = st.radio("Language", ["English", "Hindi", "French"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

# 4. RENDER BODY
st.markdown(f"""
<div class="nav-bar"></div>
<div class="main-wrapper">
    <div class="left-sidebar">
        <h3 style="color: var(--latte); margin-top: 0;">The Blend</h3>
        <p style="font-size: 0.9rem;">Sidebar is now more compact.</p>
    </div>
    <div class="right-content">
        <h2 style="color: var(--mocha); border-bottom: 1px solid var(--mocha); margin-top: 0; padding-bottom: 10px;">
            Workspace
        </h2>
        <p>Header height reduced to 45px for a more natural feel.</p>
    </div>
</div>
""", unsafe_allow_html=True)
