import streamlit as st

# Step 1: Force the page to wide mode to support the 1/3 - 2/3 split
st.set_page_config(layout="wide", page_title="Vintage App")

# Step 2: Define the interface in a single Python string
interface_html = """
<style>
    /* THEME VARIABLES */
    :root {
        --espresso: #3d2b1f;
        --mocha: #6f4e37;
        --latte: #c0a080;
        --cream: #f5f5dc;
        --paper: #ece0d1;
        --border: #a67c52;
    }

    /* CLEAN SLATE: Hide Streamlit's default margins and UI */
    .stApp { padding: 0; }
    header { visibility: hidden; }
    footer { visibility: hidden; }
    #root > div:nth-child(1) > div > div > div > div > section > div { padding: 0; }

    .app-wrapper {
        display: flex;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        font-family: 'Georgia', serif;
    }

    /* LEFT PART: 1/3 WIDTH */
    .sidebar {
        flex: 1; 
        background-color: var(--espresso);
        color: var(--cream);
        border-right: 5px double var(--border);
        padding: 40px 30px;
        overflow-y: auto;
        box-shadow: 5px 0 15px rgba(0,0,0,0.2);
    }

    /* RIGHT PART: 2/3 WIDTH */
    .main-section {
        flex: 2; 
        background-color: var(--paper);
        color: var(--espresso);
        padding: 60px;
        overflow-y: auto;
        background-image: radial-gradient(var(--paper) 70%, #e3d5c5 100%);
    }

    h1, h2 {
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    h2 {
        border-bottom: 2px solid var(--latte);
        padding-bottom: 10px;
        color: var(--latte);
        font-size: 1.5rem;
    }

    h1 {
        border-bottom: 2px solid var(--mocha);
        padding-bottom: 15px;
        margin-top: 0;
    }

    p {
        line-height: 1.8;
        font-style: italic;
        font-size: 1.1rem;
    }
</style>

<div class="app-wrapper">
    <div class="sidebar">
        <h2>The Blend</h2>
        <p>This is your control panel.</p>
        <p>Everything here is contained within the first third of your screen.</p>
    </div>

    <div class="main-section">
        <h1>Vintage Workspace</h1>
        <p>Welcome to the main gallery. The layout is now correctly partitioned, and the "SyntaxError" is resolved.</p>
        <p>We are using a single-file monolithic structure as requested.</p>
    </div>
</div>
"""

# Step 3: Execute the HTML/CSS
st.markdown(interface_html, unsafe_allow_html=True)
