from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import requests


def chat_with_agent(msj_user: str) -> str:
    response = chain.invoke({
        "historial": historial, 
        "question": msj_user
    })
    historial.append(HumanMessage(content=msj_user))
    historial.append(AIMessage(content=response.content))
    return response.content


def llm_models() -> list: 
    
    response = requests.get('http://localhost:8000/check-ollama')
    
    if response.status_code == 200: 
        data = response.json()
        list_model = data['modelos']['models']
        name_model = [value for model in list_model for name, value in model.items() if name == 'model']
        return name_model


llm = ChatOllama(
    model='llama3.1:8b', 
    base_url='http://localhost:11440', 
    temperature=0.7
)


historial = []

# Formato
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente util, responde con claridad."),
    MessagesPlaceholder(variable_name='historial'),
    ("human", "{question}")
])

chain = prompt | llm

if __name__ == "__main__":
    print('\n Refactorizando el chatbot')
    print('Comandos: "salir", "reset" \n')
    print(f'Lista de los modelos descargados: {llm_models()} \n')
    
    while True:
        user = input('Tu: ').lower()
        
        if user == 'salir':
            print('Bot: Hasta luego!\n')
            break
        
        if user == 'reset':
            historial.clear()
            print('Memoria reiniciada\n')
            continue

        respuesta = chat_with_agent(user)
        print(f"Bot: {respuesta}\n")