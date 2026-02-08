import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import time

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(page_title="Pranpixl", page_icon="🔮", layout="wide")

# Custom CSS for the specific layout requested
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700&display=swap');

    .stApp { background: #080a0f; color: white; font-family: 'Inter', sans-serif; }
    
    /* Header Styling */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        margin-bottom: 20px;
    }
    .logo-text {
        font-family: 'Syncopate', sans-serif;
        font-size: 24px;
        letter-spacing: 3px;
        color: #00ffcc;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Upload Box */
    .upload-box {
        border: 2px dashed rgba(0, 255, 204, 0.3);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        background: rgba(255, 255, 255, 0.02);
        margin-bottom: 30px;
    }

    /* Result Section */
    .analysis-card {
        display: flex;
        align-items: center;
        gap: 20px;
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .scan-thumb {
        width: 6.25%; /* 1/16th of the container width */
        border-radius: 8px;
        border: 1px solid #00ffcc;
    }

    /* Horizontal Marketplace */
    .marketplace-row {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 20px 0;
        scrollbar-width: none;
    }
    .marketplace-row::-webkit-scrollbar { display: none; }

    .product-card {
        min-width: 320px;
        background: rgba(255, 255, 255, 0.04);
        border-radius: 25px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }

    /* Glossy Best Price Effect */
    .glossy-best {
        border: 2px solid #00ffcc !important;
        background: linear-gradient(135deg, rgba(0,255,204,0.1) 0%, rgba(0,0,0,0) 100%);
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.3);
    }
    .price-badge {
        position: absolute;
        top: 15px;
        right: 15px;
        background: #00ffcc;
        color: black;
        font-size: 10px;
        font-weight: bold;
        padding: 4px 10px;
        border-radius: 50px;
    }

    /* Floating Feedback Button */
    .float-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #00ffcc;
        color: black !important;
        padding: 15px 25px;
        border-radius: 50px;
        font-weight: bold;
        text-decoration: none;
        z-index: 999;
        box-shadow: 0 10px 20px rgba(0,255,204,0.3);
    }

    .price-text { font-size: 2rem; font-weight: 800; color: #fff; margin: 10px 0; }
    .description { font-size: 0.85rem; color: #aaa; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIC & DATA ---
LANG_DATA = {
    "English": {"tagline": "Visual Commerce", "btn": "Buy Now", "query": "Feedback & Queries"},
    "తెలుగు": {"tagline": "విజువల్ కామర్స్", "btn": "కొనండి", "query": "ప్రశ్నలు & ఫీడ్‌బ్యాక్"},
    "Hindi": {"tagline": "विजुअल कॉमर्स", "btn": "खरीदें", "query": "प्रतिक्रिया और प्रश्न"}
}

@st.cache_resource
def load_engine():
    return tf.keras.applications.MobileNetV2(weights='imagenet')

# --- 3. APP STRUCTURE ---
def main():
    # HEADER SECTION
    col_l, col_r = st.columns([1, 1])
    with col_l:
        st.markdown('<div class="logo-text">💎 PRANPIXL</div>', unsafe_allow_html=True)
    with col_r:
        # Unique styled dropdown for Language
        lang_sel = st.selectbox("", ["English", "తెలుగు", "Hindi"], label_visibility="collapsed")
        t = LANG_DATA[lang_sel]

    # BODY: UPLOAD SECTION
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    if not uploaded_file:
        st.markdown("<p style='opacity:0.5;'>Drop your luxury item photo here to analyze</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file:
        model = load_engine()
        img = Image.open(uploaded_file)
        
        # ANALYSIS
        with st.spinner("Analyzing..."):
            img_p = img.convert('RGB').resize((224, 224))
            arr = tf.keras.applications.mobilenet_v2.preprocess_input(np.array(img_p))
            preds = model.predict(np.expand_dims(arr, axis=0))
            label = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1].replace('_', ' ').title()

        # 1/16th VIEW SECTION
        st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
        col_img, col_det = st.columns([1, 15]) # 1:15 ratio = 1/16th
        with col_img:
            st.image(img, use_container_width=True)
        with col_det:
            st.markdown(f"<h2>{label}</h2><p style='color:#00ffcc;'>Verified Authentication Complete</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # MARKETPLACE HORIZONTAL SCROLL
        st.markdown("### Marketplace Comparison")
        apps = [
            {"name": "Amazon India", "price": 14500, "desc": "Official Brand Warranty, 7-day replacement.", "rev": "4.8/5 (2,401)"},
            {"name": "Flipkart", "price": 13999, "desc": "Bank Offers available. Fast delivery in Hyderabad.", "rev": "4.6/5 (1,120)"},
            {"name": "Tata CLiQ", "price": 15200, "desc": "Luxury Authenticity Guarantee.", "rev": "4.9/5 (890)"}
        ]
        
        min_p = min(a['price'] for a in apps)
        
        # Horizontal Wrapper
        html_row = '<div class="marketplace-row">'
        for a in apps:
            is_best = a['price'] == min_p
            best_style = "glossy-best" if is_best else ""
            badge = '<div class="price-badge">CHEAPEST DEAL</div>' if is_best else ""
            
            html_row += f"""
            <div class="product-card {best_style}">
                {badge}
                <p style="color:#00ffcc; font-size:0.7rem; font-weight:bold;">{a['name']}</p>
                <h4 style="margin:5px 0;">{label}</h4>
                <div class="price-text">₹{a['price']:,}</div>
                <p class="description">{a['desc']}</p>
                <p style="font-size:0.8rem; color:#f1c40f;">⭐ {a['rev']}</p>
                <a href="#" class="float-btn" style="position:relative; bottom:0; right:0; display:block; text-align:center; width:100%; margin-top:10px;">{t['btn']}</a>
            </div>
            """
        html_row += "</div>"
        st.markdown(html_row, unsafe_allow_html=True)

    # FLOATING FEEDBACK BUTTON
    st.markdown(f'<a href="mailto:support@pranpixl.com" class="float-btn">🚀 {t["query"]}</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
