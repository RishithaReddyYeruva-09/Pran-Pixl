import streamlit as st
import base64

# 1. Setup Page
st.set_page_config(layout="wide", page_title="PRANPIXL Vintage")

# 2. Function to load local image as Base64 (needed for custom HTML)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Replace with your actual filename if different
logo_base64 = get_base64_image("FullLogo_Transparent_NoBuffer.png")

# 3. The Unified Interface Code
interface_html = f"""
<style>
    :root {{
        --espresso: #3d2b1f;
        --mocha: #6f4e37;
        --latte: #c0a080;
        --cream: #f5f5dc;
        --paper: #ece0d1;
        --border: #a67c52;
    }}

    /* Reset Streamlit Defaults */
    .stApp {{ padding: 0; }}
    header {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}

    .app-wrapper {{
        display: flex;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        font-family: 'Georgia', serif;
    }}

    /* Sidebar (1/3) */
    .sidebar {{
        flex: 1;
        background-color: var(--espresso);
        color: var(--cream);
        border-right: 5px double var(--border);
        padding: 40px 30px;
        overflow-y: auto;
    }}

    /* Logo Section */
    .logo-container {{
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 40px;
        border-bottom: 1px solid var(--mocha);
        padding-bottom: 20px;
    }}

    .logo-img {{
        width: 60px;
        height: auto;
        /* Optional: gives the modern logo a slightly vintage warm tint */
        filter: sepia(0.5) brightness(1.2);
    }}

    .brand-name {{
        font-size: 1.8rem;
        font-weight: bold;
        letter-spacing: 3px;
        color: var(--latte);
        text-transform: uppercase;
    }}

    /* Main Section (2/3) */
    .main-section {{
        flex: 2;
        background-color: var(--paper);
        color: var(--espresso);
        padding: 60px;
        overflow-y: auto;
        background-image: radial-gradient(var(--paper) 70%, #e3d5c5 100%);
    }}

    h1 {{
        border-bottom: 2px solid var(--mocha);
        padding-bottom: 15px;
        text-transform: uppercase;
    }}

    p {{ line-height: 1.8; font-style: italic; }}
</style>

<div class="app-wrapper">
    <div class="sidebar">
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" class="logo-img">
            <span class="brand-name">PRAN PIXL</span>
        </div>
        
        <p>Your creative studio, brewed to perfection.</p>
    </div>

    <div class="main-section">
        <h1>Workspace</h1>
        <p>The logo is now integrated. The 1/3 sidebar is ready for your navigation links or tools.</p>
    </div>
</div>
"""

# 4. Render
st.markdown(interface_html, unsafe_allow_html=True)
