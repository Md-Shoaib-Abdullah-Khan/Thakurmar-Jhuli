import streamlit as st
import wave as wav
from audio_recorder_streamlit import audio_recorder



def input():
    audio_bytes = audio_recorder(
    text="",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="6x",
    )
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        with wav.open("output.wav", "wb") as wf:
            wf.setnchannels(1)      # Mono = 1, Stereo = 2
            wf.setsampwidth(4)      # 2 bytes per sample (16-bit audio)
            wf.setframerate(44100)  # Sample rate
            wf.writeframes(audio_bytes)


if __name__ == "__main__":
    input()

