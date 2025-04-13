import base64
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

def story( query):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

    prompt = ChatPromptTemplate.from_template(
    """
You are a fairy tale story teller. I will ask you to tell a story and you have to make a short fairy tale on that topic.
Ouestion: {query}
"""
)

    llm = ChatGroq(
        model = "gemma2-9b-it",
        api_key=GROQ_API_KEY
        ) 

    story = llm.invoke(prompt.invoke({'query':query})).content
    print(story)
    return story