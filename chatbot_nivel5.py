from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import requests


def chat_with_agent(msj_user: str):
    historial.append(HumanMessage(content=msj_user))
    response = llm.invoke(historial)
    historial.append(AIMessage(content=response.content))
    return response.content
       


llm = ChatOllama(
    model='llama3.1:8b', 
    base_url='http://localhost:11440', 
    temperature=0.7
)


historial = []
msj_system = SystemMessage(content='Eres un asistente util responde con claridad')

# prompt = ChatPromptTemplate.from_messages()

if __name__ == "__main__":
    print("\nRefactorizando el chatbot")
    print("Comandos: 'salir', 'reset' \n")
    
    while True:
        user = input('Tu: ').lower()
        
        if user == 'salir':
            print('Bot: Hasta luego!\n')
            break
        
        if user == 'reset':
            historial.clear()
            print('Bot: Se ha limpiado el historial\n')
            historial.append(SystemMessage(content=msj_system))
            continue
        
        response = chat_with_agent(user)
        print(f'Bot: {response}\n')