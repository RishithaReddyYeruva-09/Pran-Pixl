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
        "watermark": "PRANPIXL"
    },
    "हिन्दी": {
        "instruction": "स्कैनिंग के लिए छवि को यहाँ खींचें और छोड़ें",
        "ready": "छवि प्राप्त हुई",
        "toggle_light": "☕ डार्क रोस्ट",
        "toggle_dark": "🥛 लाइट लैट्टे",
        "watermark": "प्राणपिक्सेल"
    },
    "বাংলা": {
        "instruction": "স্ক্যান করার জন্য ছবি এখানে ড্র্যাগ এবং ড্রপ করুন",
        "ready": "ছবি পাওয়া গেছে",
        "toggle_light": "☕ ডার্ক রোস্ট",
        "toggle_dark": "🥛 লাইট ল্যাটে",
        "watermark": "প্রাণপিক্সেল"
    },
    "தமிழ்": {
        "instruction": "ஸ்கேன் செய்ய படத்தை இங்கே இழுத்து விடவும்",
        "ready": "படம் பெறப்பட்டது",
        "toggle_light": "☕ டார்க் ரோஸ்ட்",
        "toggle_dark": "🥛 லைட் லேட்டே",
        "watermark": "பிரான்பிக்சல்"
    },
    "తెలుగు": {
        "instruction": "స్కానింగ్ కోసం చిత్రాన్ని ఇక్కడ డ్రాగ్ చేసి వదలండి",
        "ready": "చిత్రం అందింది",
        "toggle_light": "☕ డార్క్ రోస్ట్",
        "toggle_dark": "🥛 లైట్ లాట్టే",
        "watermark": "ప్రాన్‌పిక్సెల్"
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
        overflow: hidden !important;
        height: 100vh !important;
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
        position: absolute; top: 130px; bottom: 0; left: 0; right: 0;
        display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 5;
    }}
    [data-testid="stFileUploader"] section {{
        padding: 5vh 2vw !important; background-color: {box_bg} !important; 
        border: 3px dashed {border_color} !important; border-radius: 30px !important; backdrop-filter: blur(4px);
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

# 5. Background Watermark (Dynamic Language)
st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 6. Central Workspace (Dynamic Language)
st.markdown('<div class="central-workspace">', unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-bottom: 2vh;'>{ui['instruction']}</h3>", unsafe_allow_html=True)

_, uploader_col, _ = st.columns([1, 4, 1])
with uploader_col:
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    if uploaded_file:
        st.image(uploaded_file, width=220)
        st.success(ui["ready"])
st.markdown('</div>', unsafe_allow_html=True)
