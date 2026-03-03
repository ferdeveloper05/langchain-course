# En este nivel integro una funcion que consulta al modelo de ollama para saber los modelos que tiene y usarlos mas adelante
# Ademas integro un diccionario de personalidad del bot.

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


def chat_with_memory(msj_user: str) -> str:
    historial.append(HumanMessage(msj_user))
    response = llm.invoke(historial)
    historial.append(AIMessage(content=response.content))
    return response.content


def models_llm() -> list:
    """ 
    Realiza una request al servidor de los modelos. 
    Guarda en una variable los datos obtenidos en la consulta.
    Luego itera la variable para almacenar solo los datos importantes. 
    Devuelve los nombres de los modelos almacenados. 
    """
    response = requests.get("http://localhost:8000/check-ollama")
    
    if response.status_code == 200:
        data = response.json()
        list_container_models = data['modelos']['models']                    
        list_name_models = [value for model in list_container_models for name, value in model.items() if name == "model"]
        return list_name_models
    
def cambiar_personalidad(nombre: str): 
    """ Cambia la personalidad del Bot """
    if nombre in PERSONALIDADES:
        historial.clear()
        sistema = SystemMessage(content=PERSONALIDADES[nombre])
        historial.append(sistema)
        print(f'Personalidad cambiada a: {nombre.upper()}\n')
    else:
        print(f'Personalidad no encontrada. Opciones: {list(PERSONALIDADES.keys())}')


# Diccionario de personalidades para el Bot
PERSONALIDADES = {
    "asistente":"Eres un asistente útil y profesional. Responde de manera clara y concisa.", 
    "profesor":"Eres un profesor paciente. Explica conceptos de manera educativa y con ejemplos sencillos", 
    "amigo":"Eres un amigo casual. Responde de manera relajada y con humor.", 
    "experto":"Eres un experto técnico. Da respuestas detalladas y precisas con terminología técnica."
}



llm = ChatOllama(
    model=change_model(models_llm(), 1), 
    base_url='http://localhost:11440', 
    temperature=0.7
)


historial = []


#msj_system = SystemMessage(content='Eres un asistente inteligente. Responde con claridad')
#historial.append(msj_system)


if __name__ == "__main__":
    print('Chatbot Avanzado! Escribe "salir" para terminar y "reset" para limpiar \n')
    print('Comandos: "salir", "reset", "personalidad [nombre]"')
    print(f'Personalidades disponibles: {list(PERSONALIDADES.keys())} \n')
    
    cambiar_personalidad('asistente')
    
    while True: 
        user = input('Tu: ').lower()
        
        if user == 'salir':
            print('Bot: Hasta Luego!\n')
            break
        
        if user == 'reset':
            historial.clear()
            historial.append(SystemMessage(content=PERSONALIDADES["asistente"]))
            print('Bot: Memoria reiniciada!\n')
            continue
        
        if user.startswith('personalidad '):
            nombre = user.split(' ', 1)[1].lower()
            cambiar_personalidad(nombre)
            print()
            continue
        
        response = chat_with_memory(user)
        print(f'Bot: {response}\n')