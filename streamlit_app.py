import streamlit as st
import cv2
import numpy as np
import requests

# Initialize session state for product categories
if 'detected_products' not in st.session_state:
    st.session_state.detected_products = []

def preprocess_image(image):
    # Convert image to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

def extract_features(image):
    # Feature extraction function that detects edges, contours, and dominant colors
    edges = cv2.Canny(image, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    dominant_color = get_dominant_color(image)
    return contours, dominant_color

def get_dominant_color(image):
    # Dummy implementation - replace with actual color detection logic
    return "#ffcc00"  # Sample hex color code

def detect_product(image):
    # Main product detection function
    processed_image = preprocess_image(image)
    contours, dominant_color = extract_features(processed_image)
    # Detect product categories based on contours and dominant colors
    product_category = "Electronics"  # Placeholder category
    if contours:
        # Logic to detect category from contours
        return product_category
    return None

def fetch_product_details(category):
    # API call to fetch product details based on category
    try:
        response = requests.get(f'https://api.example.com/products?category={category}')
        if response.status_code == 200:
            return response.json()  # Return product details
        else:
            st.error('Failed to fetch product details.')
            return []
    except Exception as e:
        st.error(f'Error fetching products: {e}')
        return []

def display_products(products):
    # Display product information in the app
    for product in products:
        st.image(product['image_url'], caption=product['name'])
        st.write(f"Price: {product['price']}")
        st.write("---")

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    detected_category = detect_product(image)
    if detected_category:
        st.session_state.detected_products.append(detected_category)
        product_details = fetch_product_details(detected_category)
        display_products(product_details)
    else:
        st.warning('No product detected.')