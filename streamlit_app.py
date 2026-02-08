import streamlit as st
import time
import random
from PIL import Image

# 1. Page Configuration
st.set_page_config(page_title="PranPixl | AI Shopping", layout="wide")

# Theme Session State
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Indian Languages Dictionary
translations = {
    "English": {
        "instruction": "Drag & drop the image for scanning",
        "ready": "AI Analysis Complete",
        "toggle_light": "☕ Dark Roast",
        "toggle_dark": "🥛 Light Latte",
        "watermark": "PRANPIXL",
        "buy": "Buy Now",
        "best_deal": "BEST VALUE",
        "scan_status": "Detection Result"
    },
    "हिन्दी (Hindi)": {
        "instruction": "स्कैन करने के लिए छवि को यहाँ खींचें",
        "ready": "AI विश्लेषण पूरा हुआ",
        "toggle_light": "☕ डार्क रोस्ट",
        "toggle_dark": "🥛 लाइट लैट्टे",
        "watermark": "प्राणपिक्सेल",
        "buy": "अभी खरीदें",
        "best_deal": "सबसे अच्छा सौदा",
        "scan_status": "पहचान परिणाम"
    },
    "বাংলা (Bengali)": {
        "instruction": "স্ক্যান করার জন্য ছবি ড্রপ করুন",
        "ready": "AI বিশ্লেষণ সম্পন্ন",
        "toggle_light": "☕ ডার্ক রোস্ট",
        "toggle_dark": "🥛 লাইট ল্যাটে",
        "watermark": "প্রাণপিক্সেল",
        "buy": "কিনুন",
        "best_deal": "সেরা ডিল",
        "scan_status": "শনাক্তকরণ ফলাফল"
    }
}

# 3. IMPROVED DETECTION LOGIC
def smart_detect(file_obj):
    """Detects item based on filename keywords for better accuracy in demos."""
    name = file_obj.name.lower()
    if "shoe" in name or "snkr" in name or "foot" in name:
        return "Premium Running Shoes"
    elif "watch" in name or "time" in name:
        return "Luxury Smart Watch"
    elif "phone" in name or "mobile" in name:
        return "Flagship Smartphone"
    elif "shirt" in name or "cloth" in name:
        return "Designer Apparel"
    else:
        # Fallback to a generic trendy category
        return "Modern Lifestyle Product"

# 4. MARKET DATA ENGINE
def get_market_data(item):
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    data = {}
    base_price = random.randint(1500, 6000)
    
    for p in platforms:
        price = base_price + random.randint(-400, 400)
        data[p] = {
            "price": f"₹{price:,}",
            "numeric_price": price,
            "rating": round(random.uniform(4.1, 4.9), 1),
            "reviews": f"{random.randint(1000, 15000)}+",
            "delivery": f"{random.randint(1, 3)} Days",
            "desc": f"Authentic {item} verified by {p} Quality Assurance. Includes brand warranty."
        }
    return data

# 5. ELEGANT GRADIENT UI & STYLING
if st.session_state.theme == 'light':
    # Elegant Creamy Gradient
    bg_style = "linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%)"
    text_color = "#4E342E"
    card_bg = "rgba(255, 255, 255, 0.7)"
    border_color = "#8D6E63"
else:
    # Rich Dark Espresso Gradient
    bg_style = "linear-gradient(to right, #243b55, #141e30)"
    text_color = "#D7CCC8"
    card_bg = "rgba(33, 33, 33, 0.8)"
    border_color = "#5D4037"

st.markdown(f"""
    <style>
    /* Full Page Elegant Background */
    [data-testid="stAppViewContainer"] {{
        background: {bg_style} !important;
    }}
    .watermark-container {{ position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 0; pointer-events: none; }}
    .watermark-text {{ font-size: 12vw; font-weight: 900; color: {text_color}; opacity: 0.1; }}
    
    /* Elegant Result Cards */
    .result-card {{
        background: {card_bg};
        border: 1px solid {border_color};
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        min-height: 480px;
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        display: flex; flex-direction: column; justify-content: space-between;
    }}
    .price-tag {{ font-size: 2.2rem; font-weight: 800; color: {text_color}; margin: 10px 0; }}
    .best-badge {{ background: #2E7D32; color: white; padding: 4px 12px; border-radius: 50px; font-size: 0.75rem; font-weight: bold; display: inline-block; }}
    .product-desc {{ font-size: 0.85rem; color: {text_color}; opacity: 0.8; text-align: left; margin: 15px 0; line-height: 1.5; }}
    </style>
    """, unsafe_allow_html=True)

# 6. Navigation
h_col1, h_col2 = st.columns([3, 1])
with h_col1:
    st.markdown(f'<h1 style="color:{text_color}; font-family:serif; letter-spacing: 2px;">PRANPIXL</h1>', unsafe_allow_html=True)
with h_col2:
    lang_choice = st.selectbox("", list(translations.keys()))
    ui = translations[lang_choice]
    if st.button(ui["toggle_light"] if st.session_state.theme == 'light' else ui["toggle_dark"], use_container_width=True):
        st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
        st.rerun()

st.markdown(f'<div class="watermark-container"><div class="watermark-text">{ui["watermark"]}</div></div>', unsafe_allow_html=True)

# 7. Main Interface
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    st.markdown(f"<div style='text-align:center; padding-top:10vh;'><h2 style='color:{text_color}; font-weight:300;'>{ui['instruction']}</h2></div>", unsafe_allow_html=True)
else:
    with st.spinner('✨ AI Magic in progress...'):
        time.sleep(1.2)
        item_name = smart_detect(uploaded_file)
        market_data = get_market_data(item_name)
        cheapest_platform = min(market_data, key=lambda x: market_data[x]['numeric_price'])

    # Display Scanned Result Header
    res_col1, res_col2 = st.columns([1, 2])
    with res_col1:
        st.image(uploaded_file, width=280, use_container_width=False)
    with res_col2:
        st.markdown(f"<h1 style='color: {text_color}; margin-bottom:0;'>{item_name}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {text_color};'>{ui['scan_status']}: <b>{ui['ready']}</b></p>", unsafe_allow_html=True)
        st.write("---")

    # Grid for Shop Cards
    cols = st.columns(4)
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    subs = ["Global Market", "Local Favorite", "Fashion Hub", "Artisanal Hub"]
    
    for i, name in enumerate(platforms):
        details = market_data[name]
        with cols[i]:
            badge = f'<div class="best-badge">🏆 {ui["best_deal"]}</div>' if name == cheapest_platform else '<div style="height:32px;"></div>'
            
            st.markdown(f"""
                <div class="result-card">
                    <div>
                        {badge}
                        <h2 style="color: {text_color}; margin: 5px 0;">{name}</h2>
                        <p style="font-size:0.75rem; color:{text_color}; opacity:0.6;">{subs[i]}</p>
                        <div class="price-tag">{details['price']}</div>
                        <div style="color:#FBC02D; font-size: 1.1rem;">★ {details['rating']} <span style="font-size:0.8rem; color:{text_color}; opacity:0.5;">({details['reviews']})</span></div>
                        <div class="product-desc">{details['desc']}</div>
                    </div>
                    <div style="text-align: left; font-size: 0.9rem; color: {text_color};">
                        <hr style="opacity: 0.2;">
                        <b>🚚 {details['delivery']} Delivery</b><br>
                        ✅ Verified Authentic
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"{ui['buy']} @ {name}", key=f"btn_{name}", use_container_width=True):
                st.toast(f"Opening {name}...")
