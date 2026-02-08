# Pranpixl: Shop Smarter with AI

Ever seen a luxury watch or a cool pair of sneakers at the mall and wondered if you could get them cheaper online? That’s exactly why I built **Pranpixl**. 

It’s a simple but powerful tool: you take a photo, and the AI figures out what it is and immediately checks major Indian stores (like Amazon and Flipkart) to find you the best price. No more manual searching.

---

## Why I built this
Luxury prices in India are all over the place. One site might have a 20% discount while another sells it at MRP. I wanted to build a "Digital Shopping Assistant" that does the heavy lifting for you—using AI to analyze the item and data to find the deal.

### What it does:
* **Instant ID:** I used a MobileNetV2 model (a specialized AI) so it recognizes objects in a split second.
* **Talks your language:** Works perfectly in **English**, **తెలుగు (Telugu)**, and **Hindi**.
* **Finds the "Best Deal":** The app automatically highlights the cheapest price with a glowing effect so you don't miss it.
* **Sleek Vibes:** Includes a cool "Laser Scan" animation while the AI thinks, making the whole experience feel premium.

---

## The Tech Behind It
I kept the stack modern and efficient:
* **The Brain:** TensorFlow & Keras (for the AI vision).
* **The Look:** Streamlit + Custom CSS (for that "Glassmorphism" blurry card effect).
* **The Engine:** Python (Pillow for images, NumPy for data).

---

## How the Magic Happens
1. **Snap it:** You upload a photo.
2. **Prep it:** The app cleans up the photo and resizes it so the AI can read it.
3. **Identify it:** The AI model guesses what the item is (with high accuracy!).
4. **Compare it:** It checks prices across the web.
5. **Show it:** You get a swipeable list of cards showing where to buy it and for how much.



---

## Get it running on your machine

1. **Grab the code:**
   ```bash
   git clone [https://github.com/your-username/pranpixl.git](https://github.com/your-username/pranpixl.git)
### How to run it on your own machine

1. Install the requirements

   ```
  pip install -r requirements.txt
   ```

2. Run the app

   ```
  streamlit run app.py
   ```
