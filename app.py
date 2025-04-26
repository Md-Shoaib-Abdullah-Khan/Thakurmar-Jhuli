import streamlit as st
from voiceInput import convert_spech_to_text, voice_input
from storyTeller import textToVoiceStory
from storyGenerator import story
import base64

# Set page layout
st.set_page_config(page_title="Thakurmar Jhuli", layout="centered")

# Load and encode your PNG logo
with open("thakurmar jhuli.png", "rb") as img_file:
    logo_bytes = img_file.read()
logo_base64 = base64.b64encode(logo_bytes).decode()

# Custom dark CSS and UI styles
st.markdown("""
    <style>
    body {
        background-color: black;
        color: #f5f5f5;
        font-family: 'Georgia', serif;
    }

    .stApp {
        background-color: black;
        color: #f5f5f5;
    }

    .app-title {
        text-align: center;
        margin-top: 20px;
    }

    .app-title h1 {
        color: #ffcc70;
        font-size: 3em;
        text-shadow: 0 0 10px #ffae00;
        margin-bottom: 0;
    }

    .app-title img {
        margin-top: 10px;
        height: 200px;
    }

    .record-button > button {
        background-color: #ff5c5c;
        color: white;
        border-radius: 25px;
        padding: 0.75em 2em;
        font-size: 1.1em;
        border: none;
        transition: 0.3s;
        box-shadow: 0 0 15px #ff5c5c80;
    }

    .record-button > button:hover {
        background-color: #ff1c1c;
        box-shadow: 0 0 20px #ff1c1caa;
    }

    .story-box {
        background-color: #1e1e1e;
        padding: 1.5em;
        border-radius: 12px;
        box-shadow: 0 0 20px #ffcc7080;
        margin-top: 2em;
        font-size: 1.2em;
        line-height: 1.7;
        color: #fefefe;
    }
    </style>
""", unsafe_allow_html=True)

#Title and Logo
st.markdown(f"""
<div class="app-title">
<img src="data:image/png;base64,{logo_base64}" alt="App Logo">
    <h1>Thakurmar Jhuli</h1>
    
</div>
""", unsafe_allow_html=True)

#Record button
st.markdown('<div class="record-button">', unsafe_allow_html=True)
inputVoice = voice_input("input.wav")
st.write(f"User input: {inputVoice}")
st.markdown('</div>', unsafe_allow_html=True)

#Show story
if inputVoice:
    story_text = story(inputVoice)

    textToVoiceStory(story=story_text)
