import base64
from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def story( query):

    prompt = ChatPromptTemplate.from_template(
    """
    You are a fairy tale story teller. I will ask you to tell a story and you have to make a short fairy tale on that topic.
    Ouestion: {query}
    """
    )
    llm = ChatOllama(
        model = "gemma2-9b-it",
        ) 

    story = llm.invoke(prompt.invoke({'query':query})).content
    print(story)
    return story