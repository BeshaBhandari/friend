import streamlit as st
from PIL import Image
import random

# Set page configuration
st.set_page_config(page_title="Special App for My Best Friend", layout="centered")

# Welcome message
st.title("🌟 A Special App for My Best Friend 🌟")
st.subheader("Hey Luci, here's something special for you!")

# Display a heartfelt message
messages = [
    "You are the best friend anyone could ever ask for.",
    "Thank you for always being there for me.",
    "Your kindness and generosity make the world a better place.",
    "You inspire me every day with your strength and positivity.",
    "I am so grateful for your friendship. ❤️"
]

st.write(random.choice(messages))

# Display memorable photos
st.subheader("Memorable Moments")
photos = ["luci_pp.jfif", "memory.png"]  # Replace with your actual photo filenames
for photo in photos:
    img = Image.open(photo)
    st.image(img, caption="A moment to remember", use_column_width=True)

# Add an interactive love button
if st.button("❤️ Click here to feel loved ❤️"):
    st.write("You are loved and appreciated more than words can express!")

# Add a video slideshow
st.subheader("Special Video Messages")
videos = ["video1.mp4", "video2.mp4"]  # Replace with your actual video filenames
for video in videos:
    st.video(video)

# Add a final thank you message
st.write("Thank you for being the amazing person you are. This app is just a small token of my appreciation for our wonderful friendship. 💖")
