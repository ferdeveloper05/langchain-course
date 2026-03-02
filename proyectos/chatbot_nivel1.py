from langchain_ollama import ChatOllama


# 1. Inicializar el modelo
llm = ChatOllama(
    model="llama3.1:8b", 
    temperature=0.7,
    base_url='http://10.90.20.12:11440'
)


# 2. Funcion simple para chatear
def chat(mensaje_usuario):
    respuesta = llm.invoke(mensaje_usuario)
    return respuesta.content


# 3. Probar la funcionalidad
if __name__ == "__main__":
    print('Chatbor listo! Escribe "salir" para terminar \n')
    
    while True:
        usuario = input('Tu: ')
        
        if usuario.lower() == 'salir':
            print('Hasta luego!')
            break
        
        respuesta = chat(usuario) # Llamamos a la funcion para chatear
        print(f'Bot: {respuesta}\n')