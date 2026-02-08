import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Vintage App", page_icon="📜")

# 2. Enhanced CSS
st.markdown("""
<style>
    /* Hide default Streamlit overhead */
    header { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }

    :root {
        --espresso: #3d2b1f;
        --mocha: #6f4e37;
        --latte: #c0a080;
        --cream: #f5f5dc;
        --paper: #ece0d1;
        --border: #a67c52;
    }

    /* THE HEADER BAR */
    .custom-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 40px;
        height: 70px;
        background-color: white;
        border-bottom: 1px solid #e0e0e0;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
    }

    /* THE MAIN WRAPPER (Starts below header) */
    .app-container {
        display: flex;
        height: calc(100vh - 70px);
        margin-top: 70px;
        font-family: 'Georgia', serif;
    }

    /* 1/3 SIDEBAR */
    .vintage-sidebar {
        flex: 1;
        background-color: var(--espresso);
        color: var(--cream);
        border-right: 5px double var(--border);
        padding: 40px 30px;
        overflow-y: auto;
    }

    /* 2/3 MAIN SECTION */
    .vintage-main {
        flex: 2;
        background-color: var(--paper);
        color: var(--espresso);
        padding: 60px;
        overflow-y: auto;
    }

    /* Styling the Language Button to be small and clean */
    div[data-testid="stPopover"] > button {
        border-radius: 20px !important;
        border: 1px solid #ddd !important;
        padding: 2px 15px !important;
        font-size: 0.8rem !important;
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. THE HEADER (LOGO + BUTTON)
# We use a container to ensure these appear at the very top of the app
with st.container():
    # This HTML creates the background bar
    st.markdown('<div class="custom-header"></div>', unsafe_allow_html=True)
    
    # We use st.columns to place widgets inside that bar area
    # Note: Streamlit widgets have their own z-index, so we place them in columns
    col_logo, col_filler, col_lang = st.columns([2, 5, 1])
    
    with col_logo:
        # Pushing the logo into the header space
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 12px; height: 70px;">
                <div style="width: 30px; height: 30px; background: #00ffcc; border-radius: 6px;"></div>
                <div style="font-weight: 800; font-size: 1.1rem; color: #333;">PRANPIXL</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col_lang:
        # Pushing the language button into the header space
        st.write('<div style="height: 15px;"></div>', unsafe_allow_html=True) # Vertical spacer
        with st.popover("English ▾"):
            selected_lang = st.radio("Language", ["English", "Hindi", "French"], label_visibility="collapsed")

# 4. THE CONTENT SPLIT
# We render this after the header logic
st.markdown(f"""
<div class="app-container">
    <div class="vintage-sidebar">
        <h2 style="color: var(--latte);">The Blend</h2>
        <p>Your controls are now active.</p>
        <p>Selected: <b>{selected_lang}</b></p>
    </div>
    <div class="vintage-main">
        <h1 style="border-bottom: 2px solid var(--mocha);">Vintage Workspace</h1>
        <p>The Logo and Language button should now be visible in the top header bar, aligned to the left and right respectively.</p>
    </div>
</div>
""", unsafe_allow_html=True)
