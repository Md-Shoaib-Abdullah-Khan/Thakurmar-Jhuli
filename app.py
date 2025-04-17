
import streamlit as st
from voiceInput import convert_spech_to_text, voice_input
from storyTeller import textToVoiceStory
from storyGenerator import story



st.set_page_config(page_title="Thakurmar Jhuli")
st.title("Thakurmar Jhuli")

voice_input("input.wav")

inputVoice = convert_spech_to_text("input.wav")

story = story(inputVoice)
textToVoiceStory(story=story)
