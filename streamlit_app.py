import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# Initialize Session States
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Translation Dictionary (Indian Languages)
translations = {
    "English": {
        "instruction": "drang drop the image for scanning",
        "ready": "Image Received",
        "toggle_light": "☕ Dark Roast",
        "toggle_dark": "🥛 Light Latte",
        "watermark": "PRANPIXL",
        "scanned_name": "Scanned Item Name",
        "buy": "Buy Now",
    },
    "हिन्दी": {
        "instruction": "स्कैनिंग के लिए छवि को यहाँ खींचें और छोड़ें",
        "ready": "छवि प्राप्त हुई",
        "toggle_light": "☕ डार्क रोस्ट",
        "toggle_dark": "🥛 लाइट लैट्टे",
        "watermark": "प्राणपिक्सेल",
        "scanned_name": "स्कैन की गई वस्तु",
        "buy": "अभी खरीदें",
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
    /* Prevent overall page scroll */
    html, body, [data-testid="stAppViewContainer"] {{
        overflow: hidden !important;
        height: 100vh !important;
        background-color: {bg_color} !important;
        color: {text_color};
    }}

    /* Horizontal Scroll Container */
    .scroll-wrapper {{
        display: flex;
        overflow-x: auto;
        overflow-y: hidden;
        gap: 20px;
        padding: 20px 0;
        width: 100%;
        white-space: nowrap;
        scrollbar-width: thin;
        scrollbar-color: {border_color} transparent;
    }}
    .scroll-wrapper::-webkit-scrollbar {{
        height: 8px;
    }}
    .scroll-wrapper::-webkit-scrollbar-thumb {{
        background: {border_color};
        border-radius: 10px;
    }}

    /* Card Styling */
    .market-card {{
        flex: 0 0 300px; /* Fixed width for horizontal scroll */
        background-color: {card_bg};
        border: 3px solid {border_color};
        border-radius: 25px;
        padding: 20px;
        display: inline-block;
        vertical-align: top;
    }}
    
    .buy-link {{
        background-color: white;
        color: black !important;
        text-decoration: none;
        font-weight: bold;
        padding: 8px 15px;
        border: 2px solid black;
        border-radius: 5px;
        display: block;
        text-align: center;
        margin-top: 15px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Header Section
h_col1, h_col2 = st.columns([2, 1.2])
with h_col1:
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; padding: 15px 0 0 5%;">
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; color: black; font-weight: bold;">logo</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: {text_color};">PranPixl</div>
        </div>
    """, unsafe_allow_html=True)

with h_col2:
    st.markdown('<div style="padding-top: 15px;">', unsafe_allow_html=True)
    b1, b2 = st.columns([1, 1])
    with b2:
        lang_choice = st.selectbox("Language", list(translations.keys()), label_visibility="collapsed")
        ui = translations[lang_choice]
    with b1:
        if st.button(ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"], use_container_width=True):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"<div style='border-bottom: 3px solid {border_color}; width: 100%; margin: 10px 0 20px 0;'></div>", unsafe_allow_html=True)

# 5. Application Flow
uploaded_file = st.sidebar.file_uploader(ui["instruction"], type=["png", "jpg", "jpeg"])

if not uploaded_file:
    # Landing Watermark
    st.markdown(f'<div style="position:fixed; top:50%; left:50%; transform:translate(-50%,-50%); opacity:0.1; font-size:15vw; font-weight:900; font-style:italic; color:{text_color}; pointer-events:none; z-index:0; white-space:nowrap;">{ui["watermark"]}</div>', unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(f"<br><br><h2 style='text-align: center;'>{ui['instruction']}</h2>", unsafe_allow_html=True)
else:
    # --- SCAN RESULTS VIEW (HORIZONTAL SCROLL) ---
    img_col, name_col = st.columns([1, 4])
    with img_col:
        st.image(uploaded_file, width=150)
    with name_col:
        st.markdown(f"<h2 style='margin:0;'>{ui['scanned_name']}</h2>", unsafe_allow_html=True)
        st.write("Comparison of all available Indian marketplaces:")

    # Define all marketplaces
    marketplaces = [
        {"name": "Amazon", "desc": "Prime delivery, high reviews."},
        {"name": "Flipkart", "desc": "Exclusive bank offers available."},
        {"name": "Myntra", "desc": "Best for fashion & genuine brands."},
        {"name": "Ajio", "desc": "Trendiest ethnic & western wear."},
        {"name": "Tata CLiQ", "desc": "Luxury & authentic electronics."},
        {"name": "Meesho", "desc": "Lowest prices, direct factory."},
        {"name": "Nykaa", "desc": "Specialty in beauty & fashion."},
        {"name": "Snapdeal", "desc": "Value for money & daily deals."}
    ]

    # Horizontal Scroll HTML
    cards_html = "".join([f"""
        <div class="market-card">
            <h3 style="color:{text_color}; margin-top:0;">{m['name']}</h3>
            <p style="font-size:0.9rem; white-space: normal;">{m['desc']}</p>
            <p style="font-weight:bold; margin:10px 0;">₹1,299.00</p>
            <a href="#" class="buy-link">{ui['buy']}</a>
        </div>
    """ for m in marketplaces])

    st.markdown(f'<div class="scroll-wrapper">{cards_html}</div>', unsafe_allow_html=True)

# Feedback Button
st.markdown('<div style="position:fixed; bottom:20px; right:20px; border:3px solid #000; width:40px; height:40px; background:white; border-radius:8px;"></div>', unsafe_allow_html=True)
