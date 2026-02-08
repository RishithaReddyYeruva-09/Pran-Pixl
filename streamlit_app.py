import streamlit as st

# Streamlit app code

st.title('Image Upload App')

# Update file uploader to allow both png and jpg uploads
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # Process the uploaded file
    st.image(uploaded_file)
    
# More app code...