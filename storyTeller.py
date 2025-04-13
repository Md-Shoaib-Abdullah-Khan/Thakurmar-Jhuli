import streamlit as st
import os
from groq import Groq

def tts(file_path, query):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    file_path = "speech.wav" 
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
    # if response:
    #         st.audio(response, format="audio/wav")
    response.write_to_file(file_path)