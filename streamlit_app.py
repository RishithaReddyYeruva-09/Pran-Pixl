import streamlit as st

# Step 1: Force wide mode
st.set_page_config(layout="wide", page_title="Vintage App", page_icon="📜")

# Step 2: Integrated CSS
st.markdown("""
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

    /* Main Layout positioning */
    .app-wrapper {
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        font-family: 'Georgia', serif;
    }

    /* HEADER: FLEX CONTAINER */
    .top-nav-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 30px;
        background-color: white;
        border-bottom: 1px solid #ddd;
        height: 65px;
        z-index: 1001;
    }

    .logo-group {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo-square {
        width: 32px;
        height: 32px;
        background: linear-gradient(135deg, #00ffcc, #008888);
        border-radius: 6px;
    }

    .brand-name {
        font-weight: 800;
        font-size: 1.1rem;
        color: #222;
        letter-spacing: 0.5px;
    }

    /* Layout Split */
    .content-split {
        display: flex;
        flex: 1;
        overflow: hidden;
    }

    .sidebar-panel {
        flex: 1;
        background-color: var(--espresso);
        color: var(--cream);
        border-right: 5px double var(--border);
        padding: 30px;
    }

    .main-panel {
        flex: 2;
        background-color: var(--paper);
        color: var(--espresso);
        padding: 50px;
        overflow-y: auto;
    }

    /* Styling the Streamlit Popover Button to look like a small header button */
    div[data-testid="stPopover"] > button {
        background-color: transparent !important;
        border: 1px solid #ddd !important;
        color: #555 !important;
        padding: 4px 12px !important;
        border-radius: 4px !important;
        font-size: 0.85rem !important;
        height: auto !important;
    }
</style>
""", unsafe_allow_html=True)

# Step 3: Header Rendering
# We use a container to wrap the logo and the Streamlit widget on the same line
header_placeholder = st.empty()

with st.container():
    # This creates a layout for the header
    h_col1, h_col2 = st.columns([5, 1])
    
    with h_col1:
        st.markdown("""
            <div class="logo-group" style="padding-top: 10px;">
                <div class="logo-square"></div>
                <div class="brand-name">PRANPIXL <span style="font-weight: 300; font-size: 0.7rem; color: #888; margin-left: 10px;">ADVANCED VISUAL INTELLIGENCE</span></div>
            </div>
        """, unsafe_allow_html=True)
    
    with h_col2:
        # The Button/Dropdown sitting on the same line
        with st.popover("English ▾"):
            selected_lang = st.radio("Select Language", ["English", "Hindi", "French"], label_visibility="collapsed")

# Step 4: Body Content (The 1/3 - 2/3 Split)
st.markdown(f"""
<div class="app-wrapper" style="margin-top: 65px;">
    <div class="content-split">
        <div class="sidebar-panel">
            <h2 style="color: var(--latte); border-bottom: 2px solid var(--latte);">The Blend</h2>
            <p>Controls and metadata go here.</p>
        </div>
        <div class="main-panel">
            <h1 style="border-bottom: 2px solid var(--mocha);">Vintage Workspace</h1>
            <p>The interface is now aligned. The logo and language selector share the header line.</p>
            <p style="margin-top: 20px; font-style: italic;">Current Language: {selected_lang}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
