import streamlit as st
import wave as wav
from audio_recorder_streamlit import audio_recorder
from groq import Groq
import os
from langchain_ollama import ChatOllama, OllamaLLM
from dotenv import load_dotenv
load_dotenv()


def voice_input(file_path):

    audio_bytes = st.audio_input("What kind of story would you like to hear?")

    if audio_bytes:
        print(type(audio_bytes))
        with open(file_path, "wb") as f:
            f.write(audio_bytes.getbuffer())

        
        return convert_spech_to_text(file_path)
        
def convert_spech_to_text(file_path):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    client = Groq(api_key=GROQ_API_KEY)
    stt_model = 'whisper-large-v3-turbo'
    audio_file = open(file_path,'rb')
    transcription = client.audio.transcriptions.create(
        model = stt_model,
        file=audio_file,
        language='en'
    )
    print(transcription.text)
    return transcription.text

