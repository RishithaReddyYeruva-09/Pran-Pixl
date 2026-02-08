import streamlit as st

# Step 1: Force wide mode
st.set_page_config(layout="wide", page_title="Vintage App", page_icon="📜")

# Step 2: Define CSS with Header Logic
interface_css = """
<style>
    :root {
        --espresso: #3d2b1f;
        --mocha: #6f4e37;
        --latte: #c0a080;
        --cream: #f5f5dc;
        --paper: #ece0d1;
        --border: #a67c52;
    }

    /* Hide Streamlit default UI */
    header { visibility: hidden; }
    footer { visibility: hidden; }

    /* Main Container */
    .app-wrapper {
        display: flex;
        flex-direction: column; /* Stack header on top */
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        font-family: 'Georgia', serif;
    }

    /* TOP NAVIGATION BAR */
    .top-nav {
        display: flex;
        justify-content: space-between; /* Pushes logo left, language right */
        align-items: center;
        padding: 15px 40px;
        background-color: var(--cream);
        border-bottom: 3px double var(--border);
        z-index: 1000;
    }

    .logo-section {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .logo-icon {
        width: 40px;
        height: 40px;
        background-color: var(--espresso);
        border-radius: 8px; /* Matching the rounded-square look in your image */
    }

    .app-name {
        font-weight: bold;
        font-size: 1.4rem;
        color: var(--espresso);
        letter-spacing: 1px;
    }

    /* CONTENT SPLIT (1/3 - 2/3) */
    .content-body {
        display: flex;
        flex: 1;
        overflow: hidden;
    }

    .sidebar {
        flex: 1; 
        background-color: var(--espresso);
        color: var(--cream);
        border-right: 5px double var(--border);
        padding: 40px 30px;
        overflow-y: auto;
    }

    .main-section {
        flex: 2; 
        background-color: var(--paper);
        color: var(--espresso);
        padding: 60px;
        overflow-y: auto;
    }

    /* Streamlit Selectbox override to match vintage style */
    div[data-baseweb="select"] {
        border: 1px solid var(--border) !important;
        background-color: var(--paper) !important;
    }
</style>
"""

# Step 3: Streamlit Interaction for the Language Dropdown
with st.sidebar:
    # We place the logic in the sidebar for Streamlit to track, 
    # but we will visually position it in the top right using columns.
    st.markdown("### ⚙️ Settings")
    lang = st.selectbox("Current Language", ["English", "Hindi", "French", "Spanish"])

# Step 4: Render HTML
st.markdown(interface_css, unsafe_allow_html=True)

# Constructing the HTML with the Logo Left and Language info Right
# Note: The dropdown is handled by Streamlit, so we "mimic" its position in the header
header_html = f"""
<div class="app-wrapper">
    <div class="top-nav">
        <div class="logo-section">
            <div class="logo-icon"></div>
            <div class="app-name">PRANPIXL <span style="font-size: 0.8rem; font-weight: normal; opacity: 0.7;">ADVANCED VISUAL INTELLIGENCE</span></div>
        </div>
        <div class="language-display">
            <span style="border: 1px solid var(--border); padding: 5px 15px; border-radius: 5px; font-size: 0.9rem;">
                🌐 {lang}
            </span>
        </div>
    </div>
    
    <div class="content-body">
        <div class="sidebar">
            <h2>The Blend</h2>
            <p>Select your language in the ledger to the left to update the header.</p>
        </div>

        <div class="main-section">
            <h1>Vintage Workspace</h1>
            <p>The top navigation bar now mimics your uploaded layout with the brand on the left and selected language on the right.</p>
        </div>
    </div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)
