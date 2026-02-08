import streamlit as st
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="PranPixl | Smart Shopping", layout="wide")

if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Comprehensive Indian Language Dictionary
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
        "instruction": "స్కానింగ్ కోసం చిత్రాన్ని ఇక్కడ ఉంచండి",
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

# 3. MOCK API LOGIC (Simulates Data Fetching)
def get_live_market_data(item_name):
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    data = {}
    base_price = random.randint(1500, 5000)
    
    # Platform-specific "simulated" descriptions
    descriptions = {
        "Amazon": f"Bestselling {item_name} with high-grade finish. Reliable performance and top-tier seller rating.",
        "Flipkart": f"Exclusive {item_name} deal. Features advanced comfort technology and stylish design elements.",
        "Myntra": f"Premium fashion-forward {item_name}. Handpicked quality materials for a luxury feel.",
        "Ajio": f"Artisanal {item_name} with a focus on trendy aesthetics and traditional craftsmanship."
    }

    for p in platforms:
        price = base_price + random.randint(-250, 400)
        data[p] = {
            "price": f"₹{price:,}",
            "numeric_price": price,
            "rating": round(random.uniform(4.0, 4.9), 1),
            "reviews": f"{random.randint(800, 12000)}+",
            "delivery": f"{random.randint(1, 4)} Days",
            "desc": descriptions[p]
        }
    return data

# 4. Theme & Custom CSS
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
        border-radius: 35px; padding: 25px; text-align: center;
        min-height: 520px; backdrop-filter: blur(8px);
        display: flex; flex-direction: column; justify-content: space-between;
    }}
    .price-tag {{ font-size: 2.1rem; font-weight: 800; color: {text_color}; margin: 5px 0; }}
    .best-badge {{ 
        background-color: #1B5E20; color: white; padding: 6px 15px; 
        border-radius: 20px; font-size: 0.8rem; font-weight: bold; display: inline-block; margin-bottom: 10px;
    }}
    .product-desc {{
        font-size: 0.85rem; color: {text_color}; opacity: 0.8;
        text-align: left; margin: 15px 0; line-height: 1.4;
        min-height: 65px; border-left: 3px solid {border_color}; padding-left: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. Header Section
h_col1, h_col2 = st.columns([2, 1.2])
with h_col1:
    st.markdown(f'<h1 style="color:{text_color}; padding-left: 20px; font-weight:900;">PranPixl</h1>', unsafe_allow_html=True)

with h_col2:
    lang_choice = st.selectbox("Language", list(translations.keys()), label_visibility="collapsed")
    ui = translations[lang_choice]
    if st.button(ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"], use_container_width=True):
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
        st.rerun()

st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 6. Main Workspace
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    st.markdown(f"<h3 style='text-align: center; color: {text_color}; margin-top: 15vh;'>{ui['instruction']}</h3>", unsafe_allow_html=True)
else:
    with st.spinner('Deep Scanning Object...'):
        time.sleep(1.5)
        item_name = "Premium Sneakers" # Simulated AI Tagging
        market_data = get_live_market_data(item_name)
        cheapest_platform = min(market_data, key=lambda x: market_data[x]['numeric_price'])

    # Scanned Item Preview
    r_col1, r_col2 = st.columns([1, 2])
    with r_col1:
        st.image(uploaded_file, width=280)
    with r_col2:
        st.markdown(f"<h2 style='color: {text_color}; margin-bottom:0;'>{item_name}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color}; opacity:0.7;'>{ui['scan_status']}: <span style='color:#2E7D32; font-weight:bold;'>{ui['ready']}</span></p>", unsafe_allow_html=True)
        st.success("Matching found across 4 major Indian marketplaces.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Comparison Grid
    apps = [
        {"name": "Amazon", "sub": "Global Marketplace"},
        {"name": "Flipkart", "sub": "Big Billion Deals"},
        {"name": "Myntra", "sub": "Style & Fashion"},
        {"name": "Ajio", "sub": "Handpicked Trends"}
    ]

    cols = st.columns(len(apps))
    for i, app in enumerate(apps):
        name = app['name']
        details = market_data[name]
        with cols[i]:
            badge = f'<div class="best-badge">🏆 {ui["best_deal"]}</div>' if name == cheapest_platform else '<div style="height:42px;"></div>'
            
            st.markdown(f"""
                <div class="result-card">
                    <div>
                        {badge}
                        <h2 style="color: {text_color}; margin:0;">{name}</h2>
                        <p style="font-size:0.7rem; color:{text_color}; opacity:0.6; margin-bottom:10px;">{app['sub']}</p>
                        <div class="price-tag">{details['price']}</div>
                        <div style="color:#FBC02D; font-weight:bold;">★ {details['rating']} <span style="font-size:0.8rem; color:{text_color}; opacity:0.5;">({details['reviews']})</span></div>
                        
                        <div class="product-desc">{details['desc']}</div>
                    </div>
                    
                    <div style="text-align: left; font-size: 0.9rem; color: {text_color};">
                        <hr style="border: 0.5px solid {border_color}; opacity: 0.2;">
                        <b>📦 {details['delivery']} Delivery</b><br>
                        ✅ Verified Authentic<br>
                        🔄 7-Day Replacement
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Action Button
            if st.button(f"{ui['buy']}", key=f"btn_{name}", use_container_width=True):
                st.toast(f"Opening {name} Store...")

st.markdown("""<div style="position: fixed; bottom: 20px; right: 20px; width: 45px; height: 45px; background: white; border: 2.5px solid black; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.7rem; cursor: pointer;">HELP</div>""", unsafe_allow_html=True)
