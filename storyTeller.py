import streamlit as st
import os
from groq import Groq
import wave
import io
from langchain_text_splitters import RecursiveCharacterTextSplitter

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
    st.audio(fullStory, format="audio/wav", autoplay=True)