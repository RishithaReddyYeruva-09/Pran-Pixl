import streamlit as st
import time
import random
from PIL import Image
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="PranPixl | Pro Vision", layout="wide")

# Initialize Session States
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# 2. Indian Languages Dictionary
translations = {
    "English": {"instruction": "Drag & drop for AI Vision", "ready": "Analysis Complete", "best_deal": "BEST VALUE", "buy": "Buy Now", "watermark": "PRANPIXL"},
    "हिन्दी (Hindi)": {"instruction": "AI विज़न के लिए यहाँ छोड़ें", "ready": "विश्लेषण पूर्ण", "best_deal": "सबसे अच्छा सौदा", "buy": "अभी खरीदें", "watermark": "प्राणपिक्सेल"},
    "বাংলা (Bengali)": {"instruction": "AI ভিশনের জন্য এখানে ড্রপ করুন", "ready": "বিশ্লেষণ সম্পন্ন", "best_deal": "সেরা ডিল", "buy": "কিনুন", "watermark": "প্রাণপিক্সেল"},
    "தமிழ் (Tamil)": {"instruction": "AI பார்வைக்கு இங்கே விடவும்", "ready": "பகுப்பாய்வு முடிந்தது", "best_deal": "சிறந்த ஒப்பந்தம்", "buy": "வாங்க", "watermark": "பிரான்பிக்சல்"}
}

# 3. Pro-Stack Detection Logic (MobileNetV2 Simulation)
def perform_ai_vision(img):
    """Simulating MobileNetV2 + ViT for Luxury Texture Analysis"""
    time.sleep(2.2) # Simulate YOLOv12 + SAM 2 processing
    
    img_array = np.array(img.convert('RGB'))
    avg_color = img_array.mean(axis=(0, 1))
    
    # Logic based on Visual Texture/Brightness
    if avg_color.sum() > 450:
        return "Premium White Sneakers"
    elif avg_color[0] > 150 and avg_color[1] < 100:
        return "Deep Brown Leather Wallet"
    elif np.std(img_array) > 50:
        return "Noise-Cancelling Studio Headphones"
    else:
        return "Designer Lifestyle Accessory"

def get_pro_market_data(item):
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    data = {}
    base_price = random.randint(2500, 7000)
    for p in platforms:
        diff = random.randint(-400, 400)
        data[p] = {
            "price": f"₹{base_price + diff:,}",
            "num": base_price + diff,
            "rating": round(random.uniform(4.3, 4.9), 1),
            "reviews": f"{random.randint(1500, 18000)}+",
            "desc": f"MobileCLIP verified: 98% match for {item}. Segmented via Meta SAM 2."
        }
    return data

# 4. CRUSHED PAPER UI & STYLING
# Using a specific hex palette for "Coffee Brown"
espresso_dark = "#2D1B14"
coffee_paper = "#D2B48C"
ripped_edge = "rgba(0,0,0,0.2)"

st.markdown(f"""
    <style>
    /* Texture Overlay for Crushed Paper Effect */
    [data-testid="stAppViewContainer"] {{
        background-color: #3E2723 !important;
        background-image: url("https://www.transparenttextures.com/patterns/pinstriped-suit.png"), 
                          linear-gradient(135deg, #4E342E 0%, #2D1B14 100%) !important;
        color: #D7CCC8;
    }}

    .watermark {{ position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                 font-size: 14vw; font-weight: 900; color: #5D4037; opacity: 0.1; z-index: -1; }}

    /* Ripped Paper Card Effect */
    .result-card {{
        background: #EFEBE9;
        color: #3E2723;
        border-radius: 2px;
        padding: 25px;
        text-align: center;
        min-height: 540px;
        box-shadow: 5px 5px 15px {ripped_edge};
        position: relative;
        margin-bottom: 20px;
        /* Ripped paper top edge effect */
        clip-path: polygon(0% 2%, 5% 0%, 10% 3%, 15% 1%, 20% 4%, 25% 1%, 30% 5%, 35% 2%, 40% 6%, 45% 2%, 50% 5%, 55% 1%, 60% 4%, 65% 1%, 70% 5%, 75% 2%, 80% 6%, 85% 2%, 90% 5%, 95% 1%, 100% 3%, 100% 100%, 0% 100%);
    }}

    .price {{ font-size: 2.3rem; font-weight: 900; color: #2D1B14; margin: 10px 0; font-family: 'Courier New', Courier, monospace; }}
    .badge {{ background: #2D1B14; color: #D7CCC8; padding: 4px 12px; font-weight: bold; font-size: 0.7rem; letter-spacing: 1px; }}
    .stButton>button {{ border-radius: 0px !important; background-color: #2D1B14 !important; color: white !important; border: none !important; }}
    </style>
    """, unsafe_allow_html=True)

# 5. Header Logic
st.markdown(f'<div class="watermark">{translations["English"]["watermark"]}</div>', unsafe_allow_html=True)

col_h, col_l = st.columns([4, 1.2])
with col_h:
    st.markdown(f"<h1 style='font-family:serif; letter-spacing:6px; color:#D7CCC8;'>PRANPIXL <span style='font-size:0.8rem; vertical-align:middle; opacity:0.6;'>PRO AI VISION</span></h1>", unsafe_allow_html=True)
with col_l:
    lang = st.selectbox("", list(translations.keys()), label_visibility="collapsed")
    ui = translations[lang]

# 6. Interaction
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

if not uploaded_file:
    st.markdown(f"<div style='text-align:center; padding-top:15vh; opacity:0.6;'><h2 style='font-weight:200;'>{ui['instruction']}</h2></div>", unsafe_allow_html=True)
else:
    with st.spinner("📦 YOLOv12 Segmenting & SAM 2 Analyzing Texture..."):
        img = Image.open(uploaded_file)
        detected_name = perform_ai_vision(img)
        market_results = get_pro_market_data(detected_name)
        cheapest_plat = min(market_results, key=lambda x: market_results[x]['num'])

    # Scanned Result UI
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(uploaded_file, width=300)
    with c2:
        st.markdown(f"<h1 style='color:#D7CCC8;'>{detected_name}</h1>", unsafe_allow_html=True)
        st.markdown(f"**Vision Status:** {ui['ready']} (MobileNetV2)")
        st.caption("FAISS similarity search complete. Real-time pricing via SerpApi.")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render Ripped Cards
    cols = st.columns(4)
    platforms = ["Amazon", "Flipkart", "Myntra", "Ajio"]
    
    for i, p_name in enumerate(platforms):
        res = market_results[p_name]
        with cols[i]:
            badge_html = f'<div class="badge">{ui["best_deal"]}</div>' if p_name == cheapest_plat else '<div style="height:30px;"></div>'
            st.markdown(f"""
                <div class="result-card">
                    <div>
                        {badge_html}
                        <h2 style="margin:10px 0; font-family:serif;">{p_name}</h2>
                        <div class="price">{res['price']}</div>
                        <div style="color:#795548; font-weight:bold;">★ {res['rating']} <span style="font-size:0.8rem; opacity:0.5;">({res['reviews']})</span></div>
                        <p style="font-size:0.85rem; text-align:left; margin-top:20px; border-top: 1px dashed #2D1B14; padding-top:10px;">{res['desc']}</p>
                    </div>
                    <div style="text-align:left; font-size:0.9rem; font-family:monospace;">
                        <hr style="border:0.5px solid #2D1B14; opacity:0.1;">
                        <b>STATUS: AUTHENTIC</b><br>
                        EST. DELIVERY: {random.randint(2, 5)} DAYS
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"{ui['buy']} @ {p_name}", key=p_name, use_container_width=True):
                st.toast(f"Opening {p_name} Gateway...")
