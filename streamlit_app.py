# app.py
import streamlit as st
from PIL import Image, ImageOps
import io
import base64
from datetime import datetime

st.set_page_config(page_title="PRANPIXL — Advanced Visual Intelligence", layout="wide")

# --- Initialize session state ---
if "uploaded_bytes" not in st.session_state:
    st.session_state.uploaded_bytes = None
if "uploaded_name" not in st.session_state:
    st.session_state.uploaded_name = None
if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "last_run" not in st.session_state:
    st.session_state.last_run = "Never"

# --- Simple CSS polish ---
st.markdown(
    """
    <style>
    :root{--bg:#f7fbfc;--card:#ffffff;--muted:#6b7280;--accent:#06b6d4;--border:#e6edf3}
    body { background: var(--bg); }
    .topbar { display:flex; justify-content:space-between; align-items:center; padding:12px 18px;
              background:linear-gradient(90deg,#ffffff,#f7fbfd); border-bottom:1px solid var(--border); }
    .brand { display:flex; gap:12px; align-items:center; font-weight:800; color:#0f172a; }
    .logo { width:44px; height:44px; background:#eef2f7; border-radius:8px; display:flex; align-items:center; justify-content:center; font-weight:800; }
    .uploader { border:2px dashed #d1d5db; border-radius:10px; padding:18px; background:var(--card); min-height:260px; }
    .panel { background:var(--card); padding:18px; border-radius:10px; box-shadow:0 6px 18px rgba(15,23,42,0.04); }
    .marketplace { display:flex; gap:12px; flex-wrap:wrap; margin-top:8px; }
    .market-card { background:var(--card); padding:14px; border-radius:10px; width:100%; border:1px solid var(--border); }
    .feedback { position:fixed; right:20px; bottom:20px; background:var(--accent); color:white; padding:10px 14px; border-radius:999px; font-weight:700; }
    @media(min-width:900px){ .market-card { width:calc(25% - 9px); } }
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
          <div style="font-size:16px;">PRANPIXL</div>
          <div style="font-size:12px;color:#6b7280;font-weight:600;">Advanced Visual Intelligence</div>
        </div>
      </div>
      <div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Language selector aligned right
_, mid, right = st.columns([1, 6, 1])
with right:
    lang = st.selectbox("", ["English", "हिन्दी"], index=0, label_visibility="collapsed")

st.write("")  # spacing

# --- Main layout ---
left_col, center_col, right_col = st.columns([2, 4, 2])

with left_col:
    st.markdown('<div class="uploader">', unsafe_allow_html=True)
    st.markdown("### Upload image")
    uploaded = st.file_uploader("Drop or choose an image (JPG, PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
    # Persist upload in session_state so it survives reruns
    if uploaded is not None:
        st.session_state.uploaded_bytes = uploaded.getvalue()
        st.session_state.uploaded_name = uploaded.name

    if st.session_state.uploaded_bytes:
        try:
            img = Image.open(io.BytesIO(st.session_state.uploaded_bytes)).convert("RGB")
            thumb = ImageOps.contain(img, (360, 360))
            st.image(thumb, use_column_width=True, caption=st.session_state.uploaded_name)
            st.markdown(f"**File:** {st.session_state.uploaded_name}")
        except Exception:
            st.error("Preview failed. The file may be corrupted.")
    else:
        st.info("No image uploaded yet. Use the uploader above.")

    st.markdown("</div>", unsafe_allow_html=True)

with center_col:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### Analyze image")
    st.write("Model: **MobileNetV2 (placeholder)**")
    # Disable run if no upload
    run_disabled = st.session_state.uploaded_bytes is None
    if st.button("Run analysis", disabled=run_disabled):
        if run_disabled:
            st.warning("Upload an image first.")
        else:
            with st.spinner("Running analysis..."):
                # Placeholder inference: replace with your model call
                st.session_state.analysis = {
                    "predictions": [("Object A", 0.78), ("Object B", 0.12), ("Object C", 0.04)],
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                }
                st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.success("Analysis complete.")
    if st.session_state.analysis:
        st.markdown("**Top predictions**")
        for label, prob in st.session_state.analysis["predictions"]:
            st.write(f"- {label} — {int(prob*100)}%")
        st.markdown(f"**Last run:** {st.session_state.last_run}")
    else:
        st.info("No analysis yet. Click Run analysis after uploading an image.")
    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### Controls and details")
    st.write("**Status:**", "Ready" if st.session_state.uploaded_bytes else "Idle")
    st.write("**Uploaded file:**", st.session_state.uploaded_name or "—")
    st.write("**Last analysis:**", st.session_state.last_run)
    if st.button("Clear upload"):
        st.session_state.uploaded_bytes = None
        st.session_state.uploaded_name = None
        st.session_state.analysis = None
        st.experimental_rerun()
    st.button("Download report", disabled=st.session_state.analysis is None)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Marketplace ---
st.markdown("### Marketplace")
st.markdown('<div class="marketplace">', unsafe_allow_html=True)

products = [
    {"title":"Site card", "price":"340.00", "meta":"100 credits"},
    {"title":"Image Enhance", "price":"517.00", "meta":"100 credits"},
    {"title":"Image Repair", "price":"251.00", "meta":"100 credits"},
    {"title":"Market Scroll", "price":"550.00", "meta":"Best Deal; 100 credits"},
]

for p in products:
    st.markdown(
        f"""
        <div class="market-card">
          <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:15px;font-weight:700;">{p['title']}</div>
            <div style="font-weight:800;color:#0f172a;">₹ {p['price']}</div>
          </div>
          <div style="color:#6b7280;margin-top:8px;">{p['meta']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# --- Floating feedback button (opens a simple form) ---
if st.button("Feedback"):
    with st.form("feedback_form"):
        st.write("Send feedback")
        name = st.text_input("Name")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thanks — feedback received.")

# --- Footer notes ---
st.markdown("---")
st.markdown(
    """
    **Notes**  
    - Replace the placeholder inference block with your model call.  
    - Use `st.session_state` to persist results across interactions.  
    - Buttons are disabled when not applicable to avoid confusing behavior.
    """
)
