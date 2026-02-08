import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Pran Pixl", layout="wide")

# Header with logo and language selector
st.sidebar.image("logo.png", use_column_width=True)  # Assuming logo.png is in your repo
language = st.sidebar.selectbox("Select Language", ["English", "Spanish", "French"])

# Left sidebar for image upload
st.sidebar.header("Upload Image")
uploaded_file = st.sidebar.file_uploader("Drag and drop your image here", type=["jpg", "png", "jpeg"])

# Display scanned item name
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    # Assume scanned_item_name is derived from some processing
    scanned_item_name = "Sample Item Name"  # Placeholder
    st.write(f"Scanned Item Name: {scanned_item_name}")

# Marketplace cards for Amazon, Flipkart, Myntra
st.title("Marketplace Options")
# Placeholder for product listings
products = [
    {"name": "Amazon Product Name", "price": "$25", "rating": "4.5", "link": "https://amazon.com"},
    {"name": "Flipkart Product Name", "price": "$20", "rating": "4.0", "link": "https://flipkart.com"},
    {"name": "Myntra Product Name", "price": "$30", "rating": "4.1", "link": "https://myntra.com"},
]

for product in products:
    st.card(product['name'])
    st.write(f"Price: {product['price']}, Rating: {product['rating']}")
    if st.button("Buy Now", key=product['name']):
        st.write(f"Redirecting to {product['link']}...")

# Feedback button in bottom right corner
if st.button("Feedback"):
    st.write("Thanks for your feedback!")

