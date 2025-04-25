import streamlit as st
import os
from groq import Groq
import wave
import io
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit.components.v1 as components
import base64

def tts(query):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    model = "playai-tts"
    voice = "Indigo-PlayAI"
    text = query
    response_format = "wav"

    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text,
        response_format=response_format
    )

    return response.read()
   
def textToVoiceStory(story):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    storyParts = text_splitter.split_text(story)

    speech = bytes()
    parts = []
    for i in range(len(storyParts)):
        parts.append(tts(storyParts[i]))

    fullStory = speech.join(parts)

    audio_bytes = fullStory

    # Convert audio bytes to base64
    b64_audio = base64.b64encode(audio_bytes).decode("utf-8")

    with open("animation.gif", "rb") as f:
        gif_bytes = f.read()
    gif_base64 = base64.b64encode(gif_bytes).decode("utf-8")

    # Embed HTML with audio and animation control
    components.html(f"""
    <audio id="storyAudio" autoplay controls>
        <source src="data:audio/wav;base64,{b64_audio}" type="audio/wav">
        Your browser does not support the audio element.
    </audio>

    <div style="text-align: center; margin-top: 20px;">
        <img id="talkingAnim" src="data:image/gif;base64,{gif_base64}" style="height: 200px; display: none;" />
    </div>

    <script>
    const audio = document.getElementById("storyAudio");
    const anim = document.getElementById("talkingAnim");

    audio.onplay = () => {{
        anim.style.display = "inline";
    }}

    audio.onpause = () => {{
        anim.style.display = "none";
    }}

    audio.onended = () => {{
        anim.style.display = "none";
    }}
    </script>
    """, height=300)