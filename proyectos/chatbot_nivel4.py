from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import requests


def change_model(list_model: list, item: int) -> str: 
    try: 
        for i, model in enumerate(list_model):
            if i == item:
                return model
        else: 
            return list_model[0]
    except Exception as e:
        print(f'Ha ocurrido un error! Detalles: {e}')


def chat_with_memory(msj_user):
    historial.append(HumanMessage(msj_user))
    response = llm.invoke(historial)
    historial.append(response.content)
    return response.content


def models_llm():
    response = requests.get("http://10.90.20.12:8000/check-ollama")
    
    if response.status_code == 200:
        data = response.json()
        return data['modelos']

print(models_llm())

llm = ChatOllama(
    model='', 
    base_url='http://10.90.20.12:11440', 
    temperature=0.7
)


historial = []


msj_system = SystemMessage(content='Eres un asistente inteligente. Responde con claridad')
historial.append(msj_system)

