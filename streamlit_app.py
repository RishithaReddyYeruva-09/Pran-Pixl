import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# Initialize Session States
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Indian Language Translations
translations = {
    "English": {
        "instruction": "drang drop the image for scanning",
        "ready": "Ready to Scan",
        "toggle_light": "☕ Dark Roast",
        "toggle_dark": "🥛 Light Latte",
        "watermark": "PRANPIXL",
        "scanned_name": "Scanned Item Name",
        "buy": "Buy Now"
    },
    "हिन्दी": {
        "instruction": "स्कैनिंग के लिए छवि को यहाँ खींचें और छोड़ें",
        "ready": "स्कैन के लिए तैयार",
        "toggle_light": "☕ डार्क रोस्ट",
        "toggle_dark": "🥛 लाइट लैट्टे",
        "watermark": "प्राणपिक्सेल",
        "scanned_name": "स्कैन की गई वस्तु",
        "buy": "अभी खरीदें"
    }
}

# 3. Dynamic Styling
if st.session_state.theme == 'light':
    bg_color, text_color, box_bg, border_color = "#D7CCC8", "#3E2723", "rgba(255, 255, 255, 0.4)", "#3E2723"
    card_bg = "rgba(255, 255, 255, 0.5)"
else:
    bg_color, text_color, box_bg, border_color = "#1B1411", "#D7CCC8", "rgba(62, 39, 35, 0.6)", "#D7CCC8"
    card_bg = "rgba(45, 30, 25, 0.8)"

st.markdown(f"""
    <style>
    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: {bg_color} !important;
        color: {text_color};
        overflow: hidden !important;
        height: 100vh !important;
    }}

    /* Header Styling */
    .header-divider {{
        border-bottom: 3px solid {border_color};
        width: 100%;
        margin-top: 5px;
    }}

    /* Horizontal Scroll Container for Results */
    .scroll-wrapper {{
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 10px 0;
        width: 100%;
        scrollbar-width: thin;
    }}

    .market-card {{
        flex: 0 0 280px;
        background-color: {card_bg};
        border: 3px solid {border_color};
        border-radius: 30px;
        padding: 20px;
        text-align: left;
    }}

    .buy-btn {{
        background-color: white;
        color: black !important;
        border: 2px solid black;
        padding: 5px 15px;
        font-weight: bold;
        text-align: center;
        display: block;
        margin-top: 15px;
        text-decoration: none;
    }}

    /* Feedback Button (Bottom Right) */
    .feedback-box {{
        position: fixed; bottom: 20px; right: 20px;
        width: 40px; height: 40px; border: 3px solid #000;
        background: white; border-radius: 8px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Persistent Header
h_col1, h_col2 = st.columns([2, 1])
with h_col1:
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; padding-left: 5%;">
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; color: black; font-weight: bold;">logo</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: {text_color};">PranPixl</div>
        </div>
    """, unsafe_allow_html=True)

with h_col2:
    b1, b2 = st.columns([1, 1])
    with b2:
        lang = st.selectbox("Lang", list(translations.keys()), label_visibility="collapsed")
        ui = translations[lang]
    with b1:
        theme_label = ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"]
        if st.button(theme_label, use_container_width=True):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()

st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)

# 5. Logic Switch (First Page vs Second Page)
# We hide the uploader in the sidebar to act as the trigger
uploaded_file = st.sidebar.file_uploader(ui["instruction"], type=["png", "jpg", "jpeg"])

if not uploaded_file:
    # --- PAGE 1: LANDING (KEEP UNCHANGED) ---
    st.markdown(f'<div style="position:fixed; top:55%; left:50%; transform:translate(-50%,-50%); opacity:0.2; font-size:15vw; font-weight:900; font-style:italic; color:{text_color}; pointer-events:none;">{ui["watermark"]}</div>', unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(f"<br><br><br><h2 style='text-align: center;'>{ui['instruction']}</h2>", unsafe_allow_html=True)
        # Placeholder visual for the "centered" feel
        st.markdown(f"""<div style="height: 250px; border: 3px dashed {border_color}; border-radius: 30px; display: flex; align-items: center; justify-content: center; background: {box_bg};">
            <p>Please use sidebar to upload for scanning</p>
        </div>""", unsafe_allow_html=True)

else:
    # --- PAGE 2: RESULTS (BASED ON NEW REFERENCE) ---
    col_sidebar, col_results = st.columns([1, 3])
    
    with col_sidebar:
        # Left side: Drag & Drop box remains visible but as a "Sidebar"
        st.markdown(f"<div style='border: 3px solid {border_color}; padding: 20px; border-radius: 10px; height: 350px; background: {box_bg}; text-align: center;'>", unsafe_allow_html=True)
        st.write(ui["instruction"])
        st.image(uploaded_file, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_results:
        # Top Section: Uploaded preview and name
        res_img, res_name = st.columns([1, 2])
        with res_img:
            st.image(uploaded_file, width=150)
        with res_name:
            st.markdown(f"<br><h2 style='color:{text_color}'>{ui['scanned_name']}</h2>", unsafe_allow_html=True)

        # Horizontal Scroll Section for Marketplaces
        marketplaces = ["Amazon", "Flipkart", "Myntra", "Ajio", "Tata CLiQ", "Meesho", "Nykaa"]
        cards_html = "".join([f"""
            <div class="market-card">
                <h4 style="margin:0;">{m}</h4>
                <p style="font-size:0.8rem; margin:10px 0;">Includes description, product info, reviews.</p>
                <p style="font-weight:bold; font-size: 1.2rem;">₹1,499</p>
                <a href="#" class="buy-btn">{ui['buy']}</a>
            </div>
        """ for m in marketplaces])

        st.markdown(f'<div class="scroll-wrapper">{cards_html}</div>', unsafe_allow_html=True)

# Feedback Button
st.markdown('<div class="feedback-box"></div>', unsafe_allow_html=True)
