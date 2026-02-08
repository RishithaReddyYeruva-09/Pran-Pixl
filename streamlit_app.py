import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="PRANPIXL", page_icon="🖼️")

# 2. Precision CSS for Slim Header and Vertical Centering
st.markdown("""
<style>
    /* Global Overrides */
    header { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    :root {
        --espresso: #1a1612; /* Darker sidebar background */
        --mocha: #3d2b1f;
        --latte: #c0a080;
        --cream: #d1c4b9;
        --paper: #ece0d1;
        --accent: #00ffcc;
        --header-height: 44px; /* Industrial standard slim height */
    }

    /* FIXED HEADER BAR */
    .nav-bar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: var(--header-height);
        background-color: #0d0d0d; /* Deep black like target image */
        z-index: 9999;
        border-bottom: 1px solid #222;
    }

    /* VERTICAL ALIGNMENT FOR STREAMLIT WIDGETS */
    [data-testid="stHorizontalBlock"] {
        align-items: center; /* This centers the Logo and Button vertically */
        height: var(--header-height);
    }

    /* THE MAIN WRAPPER */
    .main-wrapper {
        display: flex;
        margin-top: var(--header-height); 
        height: calc(100vh - var(--header-height));
        width: 100vw;
    }

    .brand-text {
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    /* Sidebar and Main Panels */
    .left-sidebar {
        flex: 1;
        background-color: var(--espresso);
        padding: 30px 25px;
        color: var(--cream);
        border-right: 1px solid #222;
    }

    .right-content {
        flex: 2.5; /* Slightly wider main area */
        background-color: var(--paper);
        padding: 40px;
        overflow-y: auto;
    }

    /* POPPER BUTTON - Matching the "English v" look */
    div[data-testid="stPopover"] > button {
        background-color: #1a1a1a !important;
        color: #ddd !important;
        border: 1px solid #333 !important;
        height: 28px !important;
        padding: 0 12px !important;
        font-size: 0.75rem !important;
        border-radius: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. THE SLIM HEADER
# We use st.container to anchor the Python widgets into the black bar space
with st.container():
    c1, c2, c3 = st.columns([1.5, 6, 1.2]) # Adjusted ratios for better spacing
    
    with c1:
        # Pushes logo/name into the center of the 44px bar
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 18px; height: 18px; background-color: var(--accent); border-radius: 3px;"></div>
                <div class="brand-text">PRANPIXL</div>
            </div>
        """, unsafe_allow_html=True)
    
    with c3:
        # Language popover
        with st.popover("English ▾"):
            lang = st.radio("Select Language", ["English", "Hindi", "French"], label_visibility="collapsed")

# 4. RENDER BODY
st.markdown(f"""
<div class="nav-bar"></div>
<div class="main-wrapper">
    <div class="left-sidebar">
        <h2 style="color: var(--latte); font-family: 'Georgia', serif; font-size: 1.4rem; margin-bottom: 20px;">The Blend</h2>
        <p style="font-size: 0.85rem; line-height: 1.6; opacity: 0.8;">
            Sidebar layout is now proportional to the slim header.
        </p>
    </div>
    <div class="right-content">
        <h1 style="color: var(--mocha); font-family: 'Georgia', serif; border-bottom: 1px solid var(--mocha); padding-bottom: 10px; margin-top: 0;">
            Workspace
        </h1>
        <p style="margin-top: 20px; color: var(--espresso);">
            The header height is locked at 44px with 18px logo sizing. 
            This follows the visual hierarchy of the target design.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
