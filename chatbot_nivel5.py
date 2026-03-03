from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import requests


llm = ChatOllama(
    model='', 
    base_url='http://localhost:11440', 
    temperature=0.7
)

# prompt = ChatPromptTemplate.from_messages()