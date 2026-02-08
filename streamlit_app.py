import streamlit as st

# Configure the page to be wide by default
st.set_page_config(layout="wide")

# This is the single-file monolithic structure
app_code = """
<style>
    /* 1. VINTAGE COFFEE THEME VARIABLES */
    :root {
        --espresso: #3d2b1f;
        --mocha: #6f4e37;
        --latte: #c0a080;
        --cream: #f5f5dc;
        --paper: #ece0d1;
        --border: #a67c52;
    }

    /* 2. LAYOUT RESET */
    /* We hide Streamlit's default padding to take over the screen */
    .stApp {
        padding: 0;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .main-container {
        display: flex;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        font-family: 'Georgia', serif;
    }

    /* 3. SIDEBAR (1/3 Width) */
    .sidebar {
        flex: 1; 
        background-color: var(--espresso);
        color: var(--cream);
        border-right: 5px double var(--border);
        padding: 40px 30px;
        overflow-y: auto;
        box-shadow: 5px 0 15px rgba(0,0,0,0.3);
    }

    /* 4. MAIN SECTION (2/3 Width) */
    .main-section {
        flex: 2;
        background-color: var(--paper);
        padding: 60px;
        overflow-y: auto;
        color: var(--espresso);
        /* Subtle parchment texture */
        background-image: radial-gradient(var(--paper) 70%, #e3d5c5 100%);
    }

    /* TYPOGRAPHY */
    h1, h2 {
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid var(--mocha);
        padding-bottom: 10px;
    }

    .sidebar h2 {
        color: var(--latte);
        border-bottom-color: var(--latte);
    }

    p {
        line-height: 1.8;
        font-style: italic;
    }

    /* CUSTOM SCROLLBAR for that vintage look */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: var(--paper);
    }
    ::-webkit-scrollbar-thumb {
        background: var(--mocha);
    }
</style>

<div class="main-container">
    <div class="sidebar">
        <h2>The Blend</h2>
        <p>This is your control panel.</p>
        <p>Use this area for navigation, filters, or settings.</p>
    </div>

    <div class="main-section">
        <h1>Vintage Workspace</h1>
        <p>This is your main canvas. Everything here is styled with the coffee-brown palette and a 2/3 ratio layout.</p>
        <p>The code is fully contained in one file and ready for your next instruction.</p>
    </div>
</div>
"""

# Render the entire app
st.markdown(app_code, unsafe_allow_html=True)
