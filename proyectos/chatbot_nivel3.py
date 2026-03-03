from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage



list_model = ['gpt-oss:20b', 'llama3.1:8b']

# Funcion que permite cambiar el modelo que se usara
def change_model(list_model: list, item: int | None) -> str:
    for i, model in enumerate(list_model):
        if i == item:
            return model

# Funcion simple para chatear con el agente
def chat(user_message: str) -> str:
    # Agregar mensaje del usuario
    historial.append(HumanMessage(content=user_message))
    
    # Obtener respuestas
    response = llm.invoke(historial)
    
    historial.append(AIMessage(content=response.content))
    return response.content

# Historial de conversasion
historial = []


# Mensaje de sistema ()
msj_sistema = SystemMessage(content='Eres un asistente util y amable. Responde con claridad')
historial.append(msj_sistema)

# Inicializacion del agente
llm = ChatOllama(
    model=change_model(list_model, 0), 
    temperature=0.7,
    base_url='http://localhost:11440'
)


if __name__ == "__main__":
    print('Chatbot inteligente! Escribe "salir" para terminar y "reset" para limpiar...\n')
    
    while True:
        usuario = input('Tu: ').lower()
        
        if usuario == 'salir':
            print('Hasta luego!\n')
            break
        
        if usuario == 'reset':
            print(historial)
            historial.clear()
            historial.append(msj_sistema)
            print("Memoria reiniciada \n")
            continue
        
        response = chat(usuario)
        print(f'Bot: {response} \n')