import streamlit as st

# Step 1: Force wide mode
st.set_page_config(layout="wide", page_title="Vintage App", page_icon="📜")

# Step 2: Define CSS and HTML Structure
# We'll use Python string formatting to inject dynamic data later
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

    /* Hide Streamlit UI elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    .app-wrapper {
        display: flex;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        font-family: 'Georgia', serif;
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
        background-image: radial-gradient(var(--paper) 70%, #e3d5c5 100%);
    }

    .vintage-card {
        background: rgba(255, 255, 255, 0.3);
        border: 1px solid var(--border);
        padding: 20px;
        margin-top: 20px;
        border-radius: 2px;
        box-shadow: 3px 3px 0px var(--mocha);
    }

    h1 { border-bottom: 2px solid var(--mocha); padding-bottom: 15px; }
    h2 { border-bottom: 2px solid var(--latte); color: var(--latte); }
</style>
"""

# Step 3: Streamlit Logic (The "Brain")
# Since we are using a fixed CSS layout, we use the sidebar for controls 
# and the main area for the "Gallery" output.

with st.sidebar:
    st.markdown("### 🖋️ Ledger Entry")
    user_name = st.text_input("Correspondent Name", "Arthur Morgan")
    ink_color = st.selectbox("Select Ink", ["Sepia", "Charcoal", "Oxblood"])
    
    st.markdown("---")
    stamp_button = st.button("Apply Official Stamp")

# Step 4: Render the Layout
# We inject the CSS first
st.markdown(interface_css, unsafe_allow_html=True)

# We create the HTML structure but leave "slots" for our Streamlit data
if stamp_button:
    status_msg = f"Document notarized for {user_name} in {ink_color} ink."
else:
    status_msg = "Awaiting correspondence..."

main_content = f"""
<div class="app-wrapper">
    <div class="sidebar">
        <h2>The Blend</h2>
        <p>Use the Streamlit sidebar on the left to input data.</p>
        <div style="margin-top: 50px; opacity: 0.7;">
            <small>ESTABLISHED 1892</small>
        </div>
    </div>
    <div class="main-section">
        <h1>Vintage Workspace</h1>
        <p>Welcome, <b>{user_name}</b>.</p>
        <div class="vintage-card">
            <h3>Status Report</h3>
            <p>{status_msg}</p>
        </div>
        <p style="margin-top:30px;">
            The layout remains partitioned 1/3 to 2/3. By using Python f-strings, 
            we can inject Streamlit variables directly into your custom HTML.
        </p>
    </div>
</div>
"""

st.markdown(main_content, unsafe_allow_html=True)
