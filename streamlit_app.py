# app.py
import streamlit as st
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="PRANPIXl — Advanced Visual Intelligence", layout="wide")

# --- CSS styling ---
st.markdown(
    """
    <style>
    :root {
      --bg:#f8fafc;
      --card:#ffffff;
      --muted:#6b7280;
      --accent:#06b6d4;
      --border:#e6edf3;
      --shadow: 0 6px 18px rgba(15,23,42,0.06);
    }
    body { background: var(--bg); }
    .topbar {
      display:flex; align-items:center; justify-content:space-between;
      padding:12px 18px; background:linear-gradient(90deg,#ffffff,#f7fbfd);
      border-bottom:1px solid var(--border);
    }
    .brand { display:flex; align-items:center; gap:12px; font-weight:800; font-size:18px; color:#0f172a; }
    .brand .logo {
      width:44px; height:44px; background:#eef2f7; border-radius:8px; display:inline-flex;
      align-items:center; justify-content:center; font-weight:700; color:#0f172a;
    }
    .lang-buttons { display:flex; gap:8px; align-items:center; }
    .uploader {
      border:2px dashed #d1d5db; border-radius:10px; padding:18px; background:var(--card);
      min-height:260px; box-shadow:var(--shadow);
    }
    .analyze {
      background:var(--card); padding:18px; border-radius:10px; min-height:360px; box-shadow:var(--shadow);
    }
    .marketplace { display:flex; gap:12px; flex-wrap:wrap; }
    .market-card {
      background:var(--card); padding:14px; border-radius:10px; width:100%;
      box-shadow:var(--shadow); border:1px solid var(--border);
    }
    .market-card .price { font-weight:800; color:#0f172a; font-size:18px; }
    .feedback {
      position:fixed; right:20px; bottom:20px; background:var(--accent); color:white;
      padding:12px 16px; border-radius:999px; box-shadow:0 8px 24px rgba(6,182,212,0.18);
      font-weight:700; cursor:pointer;
    }
    @media(min-width:900px){
      .market-card { width:calc(25% - 9px); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Top bar ---
st.markdown(
    """
    <div class="topbar">
      <div class="brand">
        <div class="logo">PP</div>
        <div>
          <div style="font-size:14px;color:#0f172a;">PRANPIXl</div>
          <div style="font-size:12px;color:var(--muted);font-weight:600;">Advanced Visual Intelligence</div>
        </div>
      </div>
      <div class="lang-buttons">
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Put language selector to the right using columns
_, mid, right = st.columns([1, 6, 1])
with right:
    lang = st.radio("", ["English", "हिन्दी"], horizontal=True)

st.write("")  # spacing

# --- Main layout: left upload, center analyze, right info ---
left_col, center_col, right_col = st.columns([2, 4, 2])

with left_col:
    st.markdown('<div class="uploader">', unsafe_allow_html=True)
    st.markdown("### Upload Zone")
    uploaded = st.file_uploader("Drop your image here (JPG, PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
    st.markdown("**Uploaded file**")
    if uploaded:
        st.write(uploaded.name)
        try:
            img = Image.open(uploaded)
            img_thumb = ImageOps.contain(img, (300, 300))
            st.image(img_thumb, use_column_width=True)
        except Exception:
            st.error("Unable to preview this file.")
    else:
        st.info("No file uploaded yet.")
    st.markdown("</div>", unsafe_allow_html=True)

with center_col:
    st.markdown('<div class="analyze">', unsafe_allow_html=True)
    st.markdown("### ANALYZE IMAGE")
    if uploaded:
        st.markdown("**Preview & quick analysis**")
        try:
            st.image(img, caption="Uploaded image", use_column_width=True)
        except Exception:
            pass
        st.markdown("---")
        st.markdown("**Model**: MobileNetV2 (placeholder)")
        st.markdown("**Top predictions**")
        st.write("- Prediction 1 — 78%")
        st.write("- Prediction 2 — 12%")
        st.write("- Prediction 3 — 4%")
        st.markdown("---")
        if st.button("Run full analysis"):
            st.success("Analysis started. (Hook your model inference here.)")
    else:
        st.markdown("<div style='text-align:center; padding:40px 10px;'>Drop an image on the left to start analysis.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="analyze">', unsafe_allow_html=True)
    st.markdown("### Details")
    st.write("**Status:** Idle")
    st.write("**Last run:** —")
    st.write("**Model weights:** imagenet (placeholder)")
    st.markdown("---")
    st.markdown("### Controls")
    st.button("Clear upload")
    st.button("Download report")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Marketplace section ---
st.markdown("### MARKETPLACE")
st.markdown('<div class="marketplace">', unsafe_allow_html=True)

# Four product cards
products = [
    {"title":"Site card", "price":"340.00", "meta":"100 drirapowes"},
    {"title":"Anche Image here", "price":"517.00", "meta":"100 dnathapoes"},
    {"title":"Mo your imag heal", "price":"251.00", "meta":"100 dnathapoes"},
    {"title":"market Scroll", "price":"550.00", "meta":"Best Deal; 100 alun dic poowes"},
]

for p in products:
    st.markdown(
        f"""
        <div class="market-card">
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:15px;font-weight:700;">{p['title']}</div>
            <div class="price">₹ {p['price']}</div>
          </div>
          <div style="color:var(--muted);margin-top:8px;">{p['meta']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# --- Floating feedback button ---
st.markdown('<div class="feedback">FEEDBACK</div>', unsafe_allow_html=True)

# --- Footer / developer notes ---
st.markdown("---")
st.markdown(
    """
    **Developer notes**  
    - Replace placeholder model text and predictions with your inference pipeline.  
    - Use session state to persist uploaded images and analysis results across interactions.  
    - To implement a real marketplace, connect product data to a backend or a JSON file.
    """
)
