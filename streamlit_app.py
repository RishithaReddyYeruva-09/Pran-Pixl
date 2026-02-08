# app.py
import streamlit as st
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="PRANPIXL — Upload", layout="wide", initial_sidebar_state="collapsed")

# --- Session state ---
if "uploaded_bytes" not in st.session_state:
    st.session_state.uploaded_bytes = None
if "uploaded_name" not in st.session_state:
    st.session_state.uploaded_name = None
if "ready" not in st.session_state:
    st.session_state.ready = False

# --- CSS: full viewport, no scroll, centered card ---
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] > div:first-child {
      height: 100vh !important;
      overflow: hidden !important;
      background: #f6fbfc;
    }
    .center-wrap {
      height: 100vh;
      display:flex;
      align-items:center;
      justify-content:center;
      padding: 24px;
      box-sizing: border-box;
    }
    .upload-card {
      width: 820px;
      max-width: 96vw;
      max-height: calc(100vh - 48px);
      overflow: auto;
      border-radius: 14px;
      background: #ffffff;
      padding: 28px;
      box-shadow: 0 10px 30px rgba(15,23,42,0.06);
      text-align:center;
      border: 1px solid #e6edf3;
    }
    .brand { font-size:28px; font-weight:800; color:#0f172a; margin-bottom:6px; letter-spacing:1px; }
    .hint { color:#6b7280; margin-bottom:18px; }
    .drop-area {
      margin: 0 auto 18px auto;
      width: 100%;
      max-width: 760px;
      padding: 28px;
      border-radius: 12px;
      border: 2px dashed #d1d5db;
      color: #6b7280;
      background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(255,255,255,0.9));
      cursor: pointer;
    }
    .drop-area:hover { border-color: #06b6d4; color: #0f172a; }
    .controls { display:flex; gap:12px; justify-content:center; margin-top:12px; }
    .small { color:#6b7280; font-size:13px; margin-top:8px; }
    img.preview { max-width:100%; height:auto; border-radius:8px; display:block; margin: 12px auto 0 auto; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="center-wrap">', unsafe_allow_html=True)
st.markdown('<div class="upload-card">', unsafe_allow_html=True)
st.markdown('<div class="brand">PRANPIXL</div>', unsafe_allow_html=True)
st.markdown('<div class="hint">Drop an image (JPG / PNG) or click the area below to choose a file</div>', unsafe_allow_html=True)

# Actual uploader (hidden label)
uploaded = st.file_uploader("", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="uploader", label_visibility="collapsed")

# Persist upload
if uploaded is not None:
    st.session_state.uploaded_bytes = uploaded.getvalue()
    st.session_state.uploaded_name = uploaded.name

# Preview or visual drop area
if st.session_state.uploaded_bytes:
    try:
        img = Image.open(io.BytesIO(st.session_state.uploaded_bytes)).convert("RGB")
        # Fit preview to card without causing page overflow
        thumb = ImageOps.contain(img, (760, 520))
        st.image(thumb, use_column_width=False, caption=st.session_state.uploaded_name, output_format="PNG")
        st.markdown(f"<div class='small'>File: <strong>{st.session_state.uploaded_name}</strong></div>", unsafe_allow_html=True)
    except Exception:
        st.error("Preview failed. The file may be corrupted.")
else:
    # Visual hint that triggers the file input when clicked
    st.markdown(
        """
        <div class="drop-area" onclick="document.querySelector('input[type=file]').click();">
          <div style="font-size:18px;font-weight:700;margin-bottom:6px;">Drop image here</div>
          <div style="color:#9aa4ad;">JPG or PNG — recommended max 10 MB</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Controls: Proceed and Clear
col1, col2, col3 = st.columns([1,1,1])
with col1:
    proceed_disabled = st.session_state.uploaded_bytes is None
    if st.button("Proceed", disabled=proceed_disabled):
        st.session_state.ready = True
        st.experimental_rerun()
with col2:
    if st.button("Clear"):
        st.session_state.uploaded_bytes = None
        st.session_state.uploaded_name = None
        st.session_state.ready = False
        st.experimental_rerun()
with col3:
    st.write("")

st.markdown('<div class="small">Tip: use clear, high-contrast images for best results.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Ready flag for next step
if st.session_state.ready:
    st.success("Image accepted. Ready for the next step.")
