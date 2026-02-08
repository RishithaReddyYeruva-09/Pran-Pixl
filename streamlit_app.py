import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="PRANPIXL", page_icon="🖼️")

# 2. THE FINAL "HARD-LOCKED" CSS
# This kills all Streamlit-native margins and forces our custom skeleton to the edges.
st.markdown("""
<style>
    /* RESET: Wipe all default Streamlit padding/spacing */
    [data-testid="stHeader"], [data-testid="stSidebar"], header, footer {display: none !important;}
    .stApp {margin: 0; padding: 0;}
    .reportview-container .main .block-container {padding: 0 !important; max-width: 100% !important;}
    div.block-container {padding: 0 !important;}

    :root {
        --h-height: 55px;
        --s-width: 320px;
        --accent: #00ffcc;
        --dark-bg: #0b0b0b;
        --side-bg: #15120f;
        --paper-bg: #f2f2f2; /* Light grey/paper background */
    }

    /* THE HEADER: FIXED AT TOP */
    .header-bar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: var(--h-height);
        background-color: var(--dark-bg);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 25px;
        z-index: 99999;
        border-bottom: 1px solid #222;
    }

    .brand-section {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo-sq {
        width: 24px; height: 24px;
        background: linear-gradient(135deg, var(--accent), #008888);
        border-radius: 4px;
    }

    .brand-name {
        color: white;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 0.5px;
    }

    /* THE VIEWPORT WRAPPER */
    .viewport {
        display: flex;
        margin-top: var(--h-height);
        height: calc(100vh - var(--h-height));
        width: 100vw;
        overflow: hidden;
    }

    /* LEFT SIDEBAR: 1/3 FIXED */
    .sidebar-locked {
        width: var(--s-width);
        background-color: var(--side-bg);
        border-right: 1px solid #222;
        padding: 40px 25px;
        color: #d1c4b9;
    }

    /* MAIN CONTENT: 2/3 SCROLLABLE */
    .content-locked {
        flex: 1;
        background-color: var(--paper-bg);
        padding: 40px;
        overflow-y: auto;
    }

    /* THE DROPZONE BOX */
    .dropzone-container {
        border: 2px dashed #444;
        background-color: #1a1714;
        border-radius: 8px;
        padding: 40px 20px;
        text-align: center;
        margin-top: 20px;
    }

    /* MARKETPLACE CARDS */
    .market-grid {
        display: flex;
        gap: 20px;
        margin-top: 30px;
    }

    .card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        flex: 1;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #ddd;
    }

    /* PINNING THE POPOVER TO THE TOP RIGHT */
    div[data-testid="stPopover"] {
        position: fixed !important;
        top: 10px !important;
        right: 25px !important;
        z-index: 1000000 !important;
    }

    div[data-testid="stPopover"] > button {
        background-color: #222 !important;
        color: white !important;
        border: 1px solid #444 !important;
        height: 35px !important;
        border-radius: 6px !important;
    }
</style>

<div class="header-bar">
    <div class="brand-section">
        <div class="logo-sq"></div>
        <div class="brand-name">PRANPIXL</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. INTERACTIVE LANGUAGE BUTTON
with st.popover("English ▾"):
    lang = st.radio("Select Language", ["English", "Hindi", "French"], label_visibility="collapsed")

# 4. MAIN BODY STRUCTURE (Matching your Wireframe)
st.markdown(f"""
<div class="viewport">
    <div class="sidebar-locked">
        <h3 style="color: #c0a080; font-family: 'Georgia', serif;">UPLOAD ZONE</h3>
        <div class="dropzone-container">
            <span style="color: #666; font-size: 0.8rem;">Drag and drop the image for scanning</span>
        </div>
    </div>

    <div class="content-locked">
        <h2 style="font-family: 'Georgia', serif; color: #3d2b1f;">Analysis Result</h2>
        
        <div style="background: white; padding: 25px; border-radius: 12px; display: flex; gap: 20px; align-items: flex-start; border: 1px solid #ddd; margin-top: 20px;">
            <div style="width: 150px; height: 150px; background: #eee; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                <span style="color: #999; font-size: 0.8rem;">Scanned Item</span>
            </div>
            <div>
                <h4 style="margin: 0; color: #3d2b1f;">Golden Retriever</h4>
                <p style="color: #777; font-size: 0.9rem;">Model: MobileNetV2 | Precision: High</p>
                <div style="margin-top: 10px; padding: 10px; background: #f9f9f9; border-left: 4px solid var(--accent); font-size: 0.85rem;">
                    Detected attributes: Canine, Domestic, Friendly.
                </div>
            </div>
        </div>

        <h3 style="margin-top: 40px; font-family: 'Georgia', serif; color: #3d2b1f;">MARKETPLACE</h3>
        
        <div class="market-grid">
            <div class="card">
                <b>Amazon</b>
                <p style="font-size: 0.8rem; color: #666;">Includes description, product info, and reviews.</p>
                <button style="width: 100%; background: #251e18; color: white; border: none; padding: 8px; border-radius: 4px; margin-top: 10px;">Buy Button</button>
            </div>
            <div class="card">
                <b>Flipkart</b>
                <p style="font-size: 0.8rem; color: #666;">Includes description, product info, and reviews.</p>
                <button style="width: 100%; background: #251e18; color: white; border: none; padding: 8px; border-radius: 4px; margin-top: 10px;">Buy Button</button>
            </div>
            <div class="card" style="border: 2px solid var(--accent);">
                <b>Myntra</b> <span style="font-size: 0.6rem; background: var(--accent); padding: 2px 5px; border-radius: 3px;">Best Deal</span>
                <p style="font-size: 0.8rem; color: #666;">Includes description, product info, and reviews.</p>
                <button style="width: 100%; background: #251e18; color: white; border: none; padding: 8px; border-radius: 4px; margin-top: 10px;">Buy Button</button>
            </div>
        </div>
    </div>
</div>

<div style="position: fixed; bottom: 30px; right: 30px; background: var(--accent); color: #0b0b0b; padding: 12px 20px; border-radius: 50px; font-weight: bold; box-shadow: 0 4px 15px rgba(0,255,204,0.3); z-index: 1000000; cursor: pointer;">
    FEEDBACK BUTTON
</div>
""", unsafe_allow_html=True)
