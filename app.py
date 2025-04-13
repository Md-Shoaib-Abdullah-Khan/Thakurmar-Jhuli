
import streamlit as st
from voiceInput import convert_spech_to_text, voice_input
from storyTeller import tts
from storyGenerator import story
st.set_page_config(page_title="Voice Input")
st.title("Record Voice")
voice_input("output.wav")
query = convert_spech_to_text("output.wav")
story = story(query)
#tts("tts_output.wav",story)
