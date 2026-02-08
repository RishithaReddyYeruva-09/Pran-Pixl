import streamlit as st

# Step 1: Force wide mode
st.set_page_config(layout="wide", page_title="Vintage App", page_icon="📜")

# Step 2: Custom CSS for the Header and Layout
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

    .app-wrapper {
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: 100vw;
        position: absolute;
        top: 0;
        left: 0;
        font-family: 'Georgia', serif;
    }

    /* HEADER STYLING */
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 40px;
        background-color: white;
        border-bottom: 2px solid #eeeeee;
        height: 70px;
        z-index: 1000;
    }

    .logo-section {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo-box {
        width: 35px;
        height: 35px;
        background: linear-gradient(135deg, #00ffcc, #006666);
        border-radius: 6px;
    }

    .brand-text {
        color: #333;
        font-weight: 800;
        font-size: 1.2rem;
        letter-spacing: 1px;
    }

    /* SPLIT BODY */
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
    }

    .main-section {
        flex: 2; 
        background-color: var(--paper);
        color: var(--espresso);
        padding: 60px;
    }

    /* Positioning the Streamlit Popover to the right */
    .stPopover {
        position: fixed;
        right: 40px;
        top: 15px;
        z-index: 2000;
    }
</style>
"""

# Inject CSS
st.markdown(interface_css, unsafe_allow_html=True)

# Step 3: Top Navigation (Logo Area)
# We render the HTML for the logo first
logo_html = """
<div class="top-nav">
    <div class="logo-section">
        <div class="logo-box"></div>
        <div class="brand-text">PRANPIXL <span style="font-size: 0.7rem; color: #888;">ADVANCED VISUAL INTELLIGENCE</span></div>
    </div>
    <div></div> </div>
"""
st.markdown(logo_html, unsafe_allow_html=True)

# Step 4: The Language Dropdown Button
# Using Streamlit's Popover as a "Button with Dropdown"
with st.container():
    col1, col2 = st.columns([8, 1]) # Push the popover to the far right
    with col2:
        with st.popover("🌐 Language"):
            selected_lang = st.radio(
                "Select Language",
                ["English", "Hindi", "Spanish", "French"],
                index=0
            )

# Step 5: The Layout Content
body_html = f"""
<div class="app-wrapper" style="margin-top: 70px;">
    <div class="content-body">
        <div class="sidebar">
            <h2>The Blend</h2>
            <p>Active Language: <b>{selected_lang}</b></p>
            <p>The sidebar maintains its 1/3 width as requested.</p>
        </div>

        <div class="main-section">
            <h1>Vintage Workspace</h1>
            <p>The logo is now pinned to the left, and the language selector is a functional button-dropdown on the right.</p>
            <div style="margin-top: 40px; padding: 20px; border: 1px dashed var(--border);">
                <i>Document initialized in {selected_lang} mode...</i>
            </div>
        </div>
    </div>
</div>
"""

st.markdown(body_html, unsafe_allow_html=True)
