import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="PRANPIXL", layout="wide")

# --- Styles ---
st.markdown(
    """
    <style>
    /* Top bar */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 16px;
        border-bottom: 1px solid #eee;
        background: linear-gradient(90deg, #ffffff, #f8fafc);
    }
    .logo {
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 700;
        font-size: 20px;
        color: #111827;
    }
    .logo img {
        height: 36px;
        width: 36px;
        object-fit: contain;
        border-radius: 6px;
        background: #f3f4f6;
        padding: 6px;
    }
    .lang {
        display:flex;
        align-items:center;
        gap:8px;
    }
    /* Main layout */
    .uploader-box {
        border: 2px dashed #d1d5db;
        border-radius: 8px;
        padding: 28px;
        text-align: center;
        color: #6b7280;
        background: #ffffff;
        min-height: 260px;
    }
    .center-title {
        display:flex;
        align-items:center;
        justify-content:center;
        height:100%;
        font-size:48px;
        font-weight:800;
        color:#0f172a;
        letter-spacing:2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Top bar ---
top_bar = st.container()
with top_bar:
    st.markdown(
        """
        <div class="top-bar">
            <div class="logo">
                <img src="https://via.placeholder.com/80x80.png?text=Logo" alt="logo">
                <div>PranPixl</div>
            </div>
            <div class="lang">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Place language selector in the top-right using columns trick
col1, col2, col3 = st.columns([1, 6, 1])
with col3:
    lang = st.selectbox("Language", ["English", "हिन्दी", "తెలుగు", "Español"], index=0)

st.write("")  # spacing

# --- Main content: left uploader, center title, right placeholder ---
left, center, right = st.columns([2, 3, 1])

with left:
    st.markdown('<div class="uploader-box">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        label="Drag and drop an image to scan",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=False,
        help="Drop a single image file here or click to browse."
    )
    if uploaded_file:
        try:
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True, caption="Uploaded image preview")
        except Exception:
            st.error("Could not open the image. Try a different file.")
    else:
        st.info("No image uploaded yet.")
    st.markdown('</div>', unsafe_allow_html=True)

with center:
    st.markdown('<div class="center-title">PRANPIXL</div>', unsafe_allow_html=True)

with right:
    st.empty()

# --- Footer or additional controls ---
st.markdown("---")
st.markdown("**Actions**")
col_a, col_b, col_c = st.columns(3)
with col_a:
    if st.button("Scan"):
        if uploaded_file:
            st.success("Scanning started. (Hook your processing here.)")
        else:
            st.warning("Upload an image first.")
with col_b:
    if st.button("Clear"):
        # Streamlit cannot programmatically clear file_uploader; instruct user
        st.info("To clear the upload, re-run the app or upload a new file.")
with col_c:
    st.write("")

# --- Notes for developers ---
st.markdown(
    """
    **Developer notes**  
    - Replace the placeholder logo URL with your asset or use `st.image` for a local file.  
    - Hook image processing logic where the Scan button is handled.  
    - Adjust CSS colors and spacing to match your brand.
    """
)
