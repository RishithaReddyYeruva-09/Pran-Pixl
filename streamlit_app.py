import streamlit as st
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="PranPixl | Smart Shopping", layout="wide")

if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Indian Languages Translation Dictionary
translations = {
    "English": {
        "instruction": "Drag & drop the image for scanning",
        "ready": "Image Received",
        "toggle_light": "☕ Dark Roast",
        "toggle_dark": "🥛 Light Latte",
        "watermark": "PRANPIXL",
        "buy": "Buy Now",
        "best_deal": "BEST VALUE",
        "scan_status": "Scan Status"
    },
    "हिन्दी (Hindi)": {
        "instruction": "स्कैन करने के लिए छवि को यहाँ खींचें",
        "ready": "छवि प्राप्त हुई",
        "toggle_light": "☕ डार्क रोस्ट",
        "toggle_dark": "🥛 लाइट लैट्टे",
        "watermark": "प्राणपिक्सेल",
        "buy": "अभी खरीदें",
        "best_deal": "सबसे अच्छा सौदा",
        "scan_status": "स्कैन स्थिति"
    },
    "বাংলা (Bengali)": {
        "instruction": "স্ক্যান করার জন্য ছবি এখানে ড্রপ করুন",
        "ready": "ছবি পাওয়া গেছে",
        "toggle_light": "☕ ডার্ক রোস্ট",
        "toggle_dark": "🥛 লাইট ল্যাটে",
        "watermark": "প্রাণপিক্সেল",
        "buy": "কিনুন",
        "best_deal": "সেরা ডিল",
        "scan_status": "স্ক্যান স্ট্যাটাস"
    },
    "தமிழ் (Tamil)": {
        "instruction": "ஸ்கேன் செய்ய படத்தை இங்கே இழுக்கவும்",
        "ready": "படம் பெறப்பட்டது",
        "toggle_light": "☕ டார்க் ரோஸ்ட்",
        "toggle_dark": "🥛 லைட் லேட்டே",
        "watermark": "பிரான்பிக்சல்",
        "buy": "வாங்க",
        "best_deal": "சிறந்த சலுகை",
        "scan_status": "ஸ்கேன் நிலை"
    },
    "తెలుగు (Telugu)": {
        "instruction": "స్కానింగ్ కోసం చిత్రా妞ని ఇక్కడ ఉంచండి",
        "ready": "చిత్రం అందింది",
        "toggle_light": "☕ డార్క్ రోస్ట్",
        "toggle_dark": "🥛 లైట్ లాట్టే",
        "watermark": "ప్రాన్‌పిక్సెల్",
        "buy": "కొనండి",
        "best_deal": "ఉత్తమ ధర",
        "scan_status": "స్కాన్ స్థితి"
    },
    "मराठी (Marathi)": {
        "instruction": "स्कॅन करण्यासाठी प्रतिमा येथे टाका",
        "ready": "प्रतिमा प्राप्त झाली",
        "toggle_light": "☕ डार्क रोस्ट",
        "toggle_dark": "🥛 लाईट लॅट्टे",
        "watermark": "प्राणपिक्सेल",
        "buy": "आता खरेदी करा",
        "best_deal": "सर्वोत्तम डील",
        "scan_status": "स्कॅन स्थिती"
    },
    "ગુજરાતી (Gujarati)": {
        "instruction": "સ્કેન કરવા માટે છબી અહીં ખેંચો",
        "ready": "છબી મળી છે",
        "toggle_light": "☕ ડાર્ક રોસ્ટ",
        "toggle_dark": "🥛 લાઈટ લેટ્ટે",
        "watermark": "પ્રાણપિક્સેલ",
        "buy": "હમણાં ખરીદો",
        "best_deal": "શ્રેષ્ઠ સોદો",
        "scan_status": "સ્કેન સ્થિતિ"
    },
    "ಕನ್ನಡ (Kannada)": {
        "instruction": "ಸ್ಕ್ಯಾನ್ ಮಾಡಲು ಚಿತ್ರವನ್ನು ಇಲ್ಲಿಗೆ ಎಳೆಯಿರಿ",
        "ready": "ಚಿತ್ರ ಸ್ವೀಕರಿಸಲಾಗಿದೆ",
        "toggle_light": "☕ ಡಾರ್ಕ್ ರೋಸ್ಟ್",
        "toggle_dark": "🥛 ಲೈಟ್ ಲ್ಯಾಟ್ಟೆ",
        "watermark": "ಪ್ರಾಣ್‌ಪಿಕ್ಸೆಲ್",
        "buy": "ಈಗ ಖರೀದಿಸಿ",
        "best_deal": "ಅತ್ಯುತ್ತಮ ಡೀಲ್",
        "scan_status": "ಸ್ಕ್ಯಾನ್ ಸ್ಥಿತಿ"
    },
    "മലയാളം (Malayalam)": {
        "instruction": "സ്കാൻ ചെയ്യാൻ ചിത്രം ഇവിടെ ഇടുക",
        "ready": "ചിത്രം ലഭിച്ചു",
        "toggle_light": "☕ ഡാർക്ക് റോസ്റ്റ്",
        "toggle_dark": "🥛 ലൈറ്റ് ലാറ്റെ",
        "watermark": "പ്രാൺപിക്സൽ",
        "buy": "ഇപ്പോൾ വാങ്ങുക",
        "best_deal": "മികച്ച ഡീൽ",
        "scan_status": "സ്കാൻ നില"
    }
}

# 3. MOCK API LOGIC
def get_live_market_data(item_name):
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    data = {}
    base_price = random.randint(1500, 5000)
    for p in platforms:
        price = base_price + random.randint(-200, 500)
        data[p] = {
            "price": f"₹{price:,}",
            "numeric_price": price,
            "rating": round(random.uniform(3.8, 4.9), 1),
            "reviews": f"{random.randint(500, 5000)}+",
            "delivery": f"{random.randint(1, 4)} Days"
        }
    return data

# 4. Theme & Styling (Keeping your custom aesthetic)
if st.session_state.theme == 'light':
    bg_color, text_color, box_bg, border_color = "#D7CCC8", "#3E2723", "rgba(255, 255, 255, 0.5)", "#3E2723"
    watermark_opacity = "0.15"
else:
    bg_color, text_color, box_bg, border_color = "#1B1411", "#D7CCC8", "rgba(62, 39, 35, 0.7)", "#D7CCC8"
    watermark_opacity = "0.1"

st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-color: {bg_color} !important; }}
    .watermark-container {{ position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 0; pointer-events: none; }}
    .watermark-text {{ font-size: 14vw; font-weight: 900; color: {text_color}; opacity: {watermark_opacity}; font-family: sans-serif; }}
    .result-card {{
        background-color: {box_bg}; border: 2px solid {border_color};
        border-radius: 30px; padding: 25px; text-align: center;
        min-height: 440px; backdrop-filter: blur(8px);
    }}
    .price-tag {{ font-size: 2.2rem; font-weight: 800; color: {text_color}; margin: 10px 0; }}
    .best-badge {{ 
        background-color: #2E7D32; color: white; padding: 6px 18px; 
        border-radius: 20px; font-size: 0.85rem; font-weight: bold; display: inline-block; margin-bottom: 15px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. Header Section
h_col1, h_col2 = st.columns([2, 1.2])
with h_col1:
    st.markdown(f'<h1 style="color:{text_color}; padding-left: 20px;">PranPixl</h1>', unsafe_allow_html=True)

with h_col2:
    # Language selector with Indian options
    lang_choice = st.selectbox("Select Language", list(translations.keys()), label_visibility="collapsed")
    ui = translations[lang_choice]
    if st.button(ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"], use_container_width=True):
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
        st.rerun()

st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 6. Content Logic
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-top: 10vh;'>{ui['instruction']}</h3>", unsafe_allow_html=True)
else:
    with st.spinner('Scanning...'):
        time.sleep(1.2)
        item_name = "Premium Ethnic Wear" # Example item for Indian context
        market_data = get_live_market_data(item_name)
        cheapest_platform = min(market_data, key=lambda x: market_data[x]['numeric_price'])

    r_col1, r_col2 = st.columns([1, 2])
    with r_col1:
        st.image(uploaded_file, width=250)
    with r_col2:
        st.markdown(f"<h2 style='color: {text_color};'>{item_name}</h2>", unsafe_allow_html=True)
        st.info(f"{ui['scan_status']}: {ui['ready']}")

    st.divider()

    # The platform list
    apps = [
        {"name": "Amazon", "desc": "Global marketplace."},
        {"name": "Flipkart", "desc": "India's favorites."},
        {"name": "Myntra", "desc": "Premium lifestyle."},
        {"name": "Ajio", "desc": "Artisanal fashion."}
    ]

    cols = st.columns(len(apps))
    for i, app in enumerate(apps):
        name = app['name']
        details = market_data[name]
        with cols[i]:
            # Highlight the cheapest option
            badge_html = f'<div class="best-badge">✨ {ui["best_deal"]}</div>' if name == cheapest_platform else '<div style="height:45px;"></div>'
            
            st.markdown(f"""
                <div class="result-card">
                    {badge_html}
                    <h2 style="color: {text_color}; margin-top:0;">{name}</h2>
                    <div class="price-tag">{details['price']}</div>
                    <div class="rating-tag" style="color:#FBC02D;">★ {details['rating']}</div>
                    <p style="color: {text_color}; opacity: 0.7; font-size: 0.8rem;">{details['reviews']} Reviews</p>
                    <hr style="border: 0.5px solid {border_color}; opacity: 0.3;">
                    <p style="color: {text_color}; text-align: left; font-size: 0.95rem;">
                        • {details['delivery']} Delivery<br>
                        • COD Available<br>
                        • 100% Original
                    </p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"{ui['buy']} @ {name}", key=f"btn_{name}", use_container_width=True):
                st.toast(f"Redirecting...")
