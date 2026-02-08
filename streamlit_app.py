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

# --- Minimal CSS to center the uploader and make it full-screen-ish ---
st.markdown(
    """
    <style>
    .full-screen {
      min-height: 72vh;
      display:flex;
      align-items:center;
      justify-content:center;
      padding: 40px 16px;
    }
    .upload-card {
      width: 720px;
      max-width: 92vw;
      border-radius: 12px;
      background: #ffffff;
      padding: 36px;
      box-shadow: 0 8px 30px rgba(15,23,42,0.06);
      text-align:center;
      border: 1px solid #e6edf3;
    }
    .title {
      font-size:28px;
      font-weight:800;
      margin-bottom:8px;
      color:#0f172a;
      letter-spacing:1px;
    }
    .subtitle {
      color:#6b7280;
      margin-bottom:18px;
    }
    .uploader-inner { margin-top:12px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Page content: centered uploader only ---
st.markdown('<div class="full-screen">', unsafe_allow_html=True)
st.markdown('<div class="upload-card">', unsafe_allow_html=True)
st.markdown('<div class="title">PRANPIXL</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Drop an image to start — JPG or PNG</div>', unsafe_allow_html=True)

# File uploader (large, single-purpose)
uploaded = st.file_uploader("", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="uploader")

# Persist upload in session_state
if uploaded is not None:
    st.session_state.uploaded_bytes = uploaded.getvalue()
    st.session_state.uploaded_name = uploaded.name

# Show preview and proceed button only after upload
if st.session_state.uploaded_bytes:
    try:
        img = Image.open(io.BytesIO(st.session_state.uploaded_bytes)).convert("RGB")
        thumb = ImageOps.contain(img, (640, 480))
        st.image(thumb, use_column_width=True, caption=st.session_state.uploaded_name)
    except Exception:
        st.error("Preview failed. The file may be corrupted.")

    st.markdown('<div style="margin-top:12px;">', unsafe_allow_html=True)
    if st.button("Proceed"):
        # Placeholder: set a flag or navigate to next page logic
        st.session_state.ready_for_analysis = True
        st.success("Proceeding to analysis (hook your next step here).")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Large empty hint area to encourage drag-and-drop
    st.markdown(
        """
        <div class="uploader-inner">
          <div style="padding:28px;border-radius:8px;border:2px dashed #d1d5db;color:#6b7280;">
            Drag & drop your image here or click to browse
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
