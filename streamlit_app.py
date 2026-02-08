# app.py
import streamlit as st
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="PRANPIXL — Upload", layout="wide", initial_sidebar_state="collapsed")

# Session state
if "uploaded_bytes" not in st.session_state:
    st.session_state.uploaded_bytes = None
if "uploaded_name" not in st.session_state:
    st.session_state.uploaded_name = None
if "ready" not in st.session_state:
    st.session_state.ready = False

# CSS: force full viewport, hide page scrollbars, make card content fit without scrolling
st.markdown(
    """
    <style>
    /* Force app container to exactly viewport height and hide browser scroll */
    html, body, [data-testid="stAppViewContainer"] > div:first-child {
      height: 100vh !important;
      overflow: hidden !important;
      margin: 0;
      padding: 0;
      background: #f6fbfc;
    }
    /* Centering wrapper fills viewport */
    .center-wrap {
      height: 100vh;
      display:flex;
      align-items:center;
      justify-content:center;
      box-sizing: border-box;
      padding: 20px;
    }
    /* Card must not exceed viewport; internal content scroll disabled */
    .upload-card {
      width: 880px;
      max-width: 96vw;
      height: calc(100vh - 40px);
      border-radius: 14px;
      background: #ffffff;
      padding: 28px;
      box-shadow: 0 10px 30px rgba(15,23,42,0.06);
      text-align:center;
      border: 1px solid #e6edf3;
      display:flex;
      flex-direction:column;
      align-items:center;
      justify-content:space-between;
      overflow: hidden; /* Prevent internal scrolling */
    }
    .brand { font-size:28px; font-weight:800; color:#0f172a; margin-bottom:6px; letter-spacing:1px; }
    .hint { color:#6b7280; margin-bottom:12px; }
    .drop-area {
      width: 100%;
      max-width: 760px;
      padding: 22px;
      border-radius: 12px;
      border: 2px dashed #d1d5db;
      color: #6b7280;
      background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(255,255,255,0.9));
      cursor: pointer;
      display:flex;
      flex-direction:column;
      align-items:center;
      justify-content:center;
      gap:6px;
    }
    .drop-area:hover { border-color: #06b6d4; color: #0f172a; }
    .preview-wrap {
      width: 100%;
      max-width: 760px;
      flex: 1 1 auto;
      display:flex;
      align-items:center;
      justify-content:center;
      margin-top:12px;
      margin-bottom:12px;
    }
    img.preview {
      max-width: 100%;
      max-height: calc(100vh - 260px); /* ensure image never forces page height */
      object-fit: contain;
      border-radius:8px;
      display:block;
    }
    .controls { display:flex; gap:12px; justify-content:center; margin-top:8px; }
    .small { color:#6b7280; font-size:13px; margin-top:6px; }
    /* Hide any Streamlit default overflow on inner containers */
    [data-testid="stVerticalBlock"] { overflow: visible !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="center-wrap">', unsafe_allow_html=True)
st.markdown('<div class="upload-card">', unsafe_allow_html=True)

st.markdown('<div style="width:100%;display:flex;flex-direction:column;align-items:center;">', unsafe_allow_html=True)
st.markdown('<div class="brand">PRANPIXL</div>', unsafe_allow_html=True)
st.markdown('<div class="hint">Drop an image (JPG / PNG) or click the area below to choose a file</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Hidden label uploader (actual control)
uploaded = st.file_uploader("", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="uploader", label_visibility="collapsed")

# Persist upload
if uploaded is not None:
    st.session_state.uploaded_bytes = uploaded.getvalue()
    st.session_state.uploaded_name = uploaded.name

# Preview area that will not expand beyond viewport
if st.session_state.uploaded_bytes:
    try:
        img = Image.open(io.BytesIO(st.session_state.uploaded_bytes)).convert("RGB")
        # Create a thumbnail that fits safely inside the card
        thumb = ImageOps.contain(img, (1200, 900))
        # Use st.image but constrain size via HTML wrapper to avoid causing page overflow
        st.markdown('<div class="preview-wrap">', unsafe_allow_html=True)
        st.image(thumb, use_column_width=False, output_format="PNG", caption=st.session_state.uploaded_name)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='small'>File: <strong>{st.session_state.uploaded_name}</strong></div>", unsafe_allow_html=True)
    except Exception:
        st.error("Preview failed. The file may be corrupted.")
else:
    # Clickable visual drop area that triggers the hidden file input
    st.markdown(
        """
        <div class="drop-area" onclick="document.querySelector('input[type=file]').click();">
          <div style="font-size:18px;font-weight:700;">Drop image here</div>
          <div style="color:#9aa4ad;">JPG or PNG — recommended max 10 MB</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Controls at bottom of card; keep them inside the card so page height doesn't change
st.markdown('<div style="width:100%;display:flex;flex-direction:column;align-items:center;">', unsafe_allow_html=True)
cols = st.columns([1,1,1])
with cols[0]:
    proceed_disabled = st.session_state.uploaded_bytes is None
    if st.button("Proceed", disabled=proceed_disabled):
        st.session_state.ready = True
with cols[1]:
    if st.button("Clear"):
        st.session_state.uploaded_bytes = None
        st.session_state.uploaded_name = None
        st.session_state.ready = False
        st.experimental_rerun()
with cols[2]:
    st.write("")  # reserved
st.markdown('<div class="small">Tip: use clear, high-contrast images for best results.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Ready flag for next step
if st.session_state.ready:
    st.success("Image accepted. Ready for the next step.")
