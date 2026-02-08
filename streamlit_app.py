import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PranPixl", layout="wide")

# Initialize Session States
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Translation Dictionary
translations = {
    "English": {
        "instruction": "drag drop the image for scanning",
        "ready": "Image Received",
        "toggle_light": "☕ Dark Roast",
        "toggle_dark": "🥛 Light Latte",
        "watermark": "PRANPIXL",
        "buy": "Buy Now"
    },
    "हिन्दी": {
        "instruction": "स्कैनिंग के लिए छवि को यहाँ खींचें और छोड़ें",
        "ready": "छवि प्राप्त हुई",
        "toggle_light": "☕ डार्क रोস্ট",
        "toggle_dark": "🥛 लाइट लैट्टे",
        "watermark": "प्राणपिक्सेल",
        "buy": "अभी खरीदें"
    },
    "বাংলা": {
        "instruction": "স্ক্যান করার জন্য ছবি এখানে ড্র্যাগ এবং ড্রপ করুন",
        "ready": "ছবি পাওয়া গেছে",
        "toggle_light": "☕ ডার্ক রোস্ট",
        "toggle_dark": "🥛 লাইট ল্যাটে",
        "watermark": "প্রাণপিক্সেল",
        "buy": "কিনুন"
    },
    "தமிழ்": {
        "instruction": "ஸ்கேன் செய்ய படத்தை இங்கே இழுத்து விடவும்",
        "ready": "படம் பெறப்பட்டது",
        "toggle_light": "☕ டார்க் ரோஸ்ட்",
        "toggle_dark": "🥛 லைட் லேட்டே",
        "watermark": "பிரான்பிக்சல்",
        "buy": "வாங்க"
    },
    "తెలుగు": {
        "instruction": "స్కానింగ్ కోసం చిత్రాన్ని ఇక్కడ డ్రాగ్ చేసి వదలండి",
        "ready": "చిత్రం అందింది",
        "toggle_light": "☕ డార్క్ రోస్ట్",
        "toggle_dark": "🥛 లైట్ లాట్టే",
        "watermark": "ప్రాన్‌పిక్సెల్",
        "buy": "కొనండి"
    }
}

# 3. Theme & Responsive CSS
if st.session_state.theme == 'light':
    bg_color, text_color, box_bg, border_color = "#D7CCC8", "#3E2723", "rgba(255, 255, 255, 0.4)", "#3E2723"
    watermark_opacity = "0.2"
else:
    bg_color, text_color, box_bg, border_color = "#1B1411", "#D7CCC8", "rgba(62, 39, 35, 0.6)", "#D7CCC8"
    watermark_opacity = "0.15"

st.markdown(f"""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main .block-container {{
        overflow-x: hidden !important;
        background-color: {bg_color} !important;
        margin: 0 !important;
        padding: 0 !important;
    }}
    .watermark-container {{
        position: fixed; top: 55%; left: 50%; transform: translate(-50%, -50%); z-index: 0; pointer-events: none;
    }}
    .watermark-text {{
        font-size: 14vw; font-weight: 900; font-style: italic; color: {text_color};
        opacity: {watermark_opacity}; font-family: sans-serif; white-space: nowrap;
    }}
    .central-workspace {{
        position: relative; padding-top: 20px;
        display: flex; flex-direction: column; align-items: center; z-index: 5;
    }}
    [data-testid="stFileUploader"] section {{
        padding: 5vh 2vw !important; background-color: {box_bg} !important; 
        border: 3px dashed {border_color} !important; border-radius: 30px !important; backdrop-filter: blur(4px);
    }}
    /* Result Card Styling */
    .result-card {{
        background-color: {box_bg}; border: 3px solid {border_color};
        border-radius: 40px; padding: 20px; text-align: center;
        min-height: 400px; backdrop-filter: blur(4px);
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Header Section
h_col1, h_col2 = st.columns([2, 1.2])

with h_col1:
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; padding-left: 5%; padding-top: 15px;">
            <div style="border: 3px solid #000; padding: 5px 15px; background: white; color: black; font-weight: bold;">logo</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: {text_color};">PranPixl</div>
        </div>
    """, unsafe_allow_html=True)

with h_col2:
    st.markdown('<div style="padding-top: 15px;">', unsafe_allow_html=True)
    btn_col1, btn_col2 = st.columns([1, 1])
    
    with btn_col2:
        lang = st.selectbox("Language", list(translations.keys()), label_visibility="collapsed")
        ui = translations[lang]

    with btn_col1:
        theme_btn = ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"]
        if st.button(theme_btn, use_container_width=True):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"<div style='border-bottom: 3px solid {border_color}; width: 100%; margin-top: 10px;'></div>", unsafe_allow_html=True)

# 5. Background Watermark
st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 6. Logic for Screen Change
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)

# File Uploader always present at top or logic-based
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    # --- ORIGINAL SCREEN ---
    st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-top: 5vh;'>{ui['instruction']}</h3>", unsafe_allow_html=True)
else:
    # --- NEW REFERENCE SCREEN ---
    # Top Section: Scanned Image and Name
    res_col1, res_col2 = st.columns([1, 1])
    with res_col1:
        st.image(uploaded_file, width=300)
    with res_col2:
        st.markdown(f"<h2 style='color: {text_color}; padding-top: 40px;'>Scanned Item Name</h2>", unsafe_allow_html=True)
        st.info(ui["ready"])

    st.markdown("<br>", unsafe_allow_html=True)

    # App Cards Section
    apps = [
        {"name": "Amazon", "desc": "Global marketplace with fast delivery."},
        {"name": "Flipkart", "desc": "India's favorite shopping destination."},
        {"name": "Myntra", "desc": "Premium fashion and lifestyle trends."},
        {"name": "Ajio", "desc": "Handpicked artisanal and trendy fashion."}
    ]

    cols = st.columns(len(apps))
    
    for i, app in enumerate(apps):
        with cols[i]:
            st.markdown(f"""
                <div class="result-card">
                    <h2 style="color: {text_color};">{app['name']}</h2>
                    <p style="color: {text_color}; text-align: left; font-size: 0.9rem;">
                        <b>Includes:</b><br>
                        - Description<br>
                        - Product Info<br>
                        - Reviews
                    </p>
                    <p style="font-size: 0.8rem; color: {text_color}; opacity: 0.8;">{app['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"{ui['buy']}", key=f"btn_{app['name']}", use_container_width=True):
                st.toast(f"Redirecting to {app['name']}...")

st.markdown('</div>', unsafe_allow_html=True)

# Feedback Button (Floating bottom right)
st.markdown("""
    <style>
    .feedback-btn {
        position: fixed; bottom: 20px; right: 20px;
        width: 50px; height: 50px; border: 3px solid black;
        background: white; border-radius: 10px; cursor: pointer;
    }
    </style>
    <div class="feedback-btn"></div>
""", unsafe_allow_html=True)
