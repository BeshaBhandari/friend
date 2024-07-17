import streamlit as st
from PIL import Image
import random

# Set page configuration
st.set_page_config(page_title="Special App for My Best Friend", layout="centered")

# Welcome message
st.title("🌟 A Special App for My Best Friend 🌟")
st.subheader("Hey Luci, here's something special for you!")

# Display a heartfelt message function
def display_message():
    messages = [
        "You are the best friend anyone could ever ask for.",
        "Thank you for always being there for me.",
        "Your kindness and generosity make the world a better place.",
        "You inspire me every day with your strength and positivity.",
        "I am so grateful for your friendship. ❤️",
        "Your smile brightens up my darkest days.",
        "Distance may separate us, but our friendship knows no bounds.",
        "Looking forward to creating more memories together.",
        "You have a heart of gold and a spirit that shines.",
        "Even miles apart, you're always in my thoughts and heart.",
        "Our friendship is a treasure I hold dear.",
        "Cheers to the countless laughs and unforgettable moments.",
        "Every moment spent with you is a cherished memory.",
        "Your support and encouragement mean everything to me.",
        "Here's to many more adventures and shared dreams.",
        "You make the world a better place just by being in it.",
        "Through thick and thin, you're my rock.",
        "Grateful for the bond we share, no matter the distance.",
        "Your friendship is a gift I treasure every day.",
        "To the friend who understands me like no one else.",
        "You're not just a friend, you're family.",
        "Thank you for being you — incredible, kind, and simply amazing."
    ]
    return random.choice(messages)

# Display initial message
if st.button("❤️ Click here to feel loved ❤️"):
    new_message = display_message()
    st.write(new_message)

# Display memorable photos in a loop
st.subheader("Memorable Moments")
photos = ["luci_pp.jfif", "memory.png", "image.png"]  # Remove the unnecessary comma

# Initialize session state for photo index
if 'photo_index' not in st.session_state:
    st.session_state.photo_index = 0

# Display current photo
img = Image.open(photos[st.session_state.photo_index])
st.image(img, caption="A moment to remember", use_column_width=True)

# Button to show next photo
if st.button("Next photo for my best friend in the distance!"):
    st.session_state.photo_index = (st.session_state.photo_index + 1) % len(photos)
    st.experimental_rerun()

# Add a video slideshow with "Next" button
st.subheader("Special Video Messages")
videos = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4", "video6.mp4"]  # Replace with your actual video filenames

# Initialize session state for video index
if 'video_index' not in st.session_state:
    st.session_state.video_index = 0

# Display current video
st.video(videos[st.session_state.video_index])

# Button to show next video
if st.button("Next video for my amazing best friend!"):
    st.session_state.video_index = (st.session_state.video_index + 1) % len(videos)
    st.experimental_rerun()

# Add a final thank you message
st.write("Thank you for being the amazing person you are. This app is just a small token of my appreciation for our wonderful friendship. 💖")
