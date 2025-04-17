import streamlit as st
import wave as wav
from audio_recorder_streamlit import audio_recorder
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()


def voice_input(file_path):
    audio_bytes = audio_recorder(
    text="",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="6x",
    )
    if audio_bytes:
        #st.audio(audio_bytes, format="audio/wav")
        with wav.open(file_path, "wb") as wf:
            wf.setnchannels(1)      # Mono = 1, Stereo = 2
            wf.setsampwidth(4)      # 2 bytes per sample (16-bit audio)
            wf.setframerate(44100)  # Sample rate
            wf.writeframes(audio_bytes)
        
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
    print(transcription)
    return transcription.text


if __name__ == "__main__":
    input()

