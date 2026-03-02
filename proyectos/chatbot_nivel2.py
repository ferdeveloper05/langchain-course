from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def selection_model(name_model: str) -> str:
    return name_model

llm = ChatOllama(
    model=input('Ingrese el modelo: ').lower(), 
    temperature=0.7, 
    base_url='http://10.90.20.12:11440'
)

# 2. Historial de conversacion
historial = []

# Mensaje de sistema (personalidad del bot)
mensaje_sistema = SystemMessage(content='Eres un asistente útil y amable. Responde de manera clara')
historial.append(mensaje_sistema)

# Funcion para chatear con memoria
def chatear(mensaje_usuario):
    # Agregar mensaje del usuario
    historial.append(HumanMessage(content=mensaje_usuario))
    
    # Obtener respuesta
    response = llm.invoke(historial)
     
    #Guardar respuesta en historial
    historial.append(AIMessage(content=response.content))
    return response.content


if __name__ == "__main__":
    print('Chatbot de IA, "salir" para cerrar \n')

    while True:
        usuario = input('Tu: ').lower()
        
        if usuario == "salir":
            break
        
        if usuario == "reset":
            historial.clear()
            historial.append(mensaje_sistema)
            print('Memoria reiniciada \n')
            continue
        
        response = chatear(usuario)
        print(f"Bot: {response} \n")