import requests

#Aquí voy a usar mi APIKEY
API_KEY = ''
API_URL = 'https://api.deepseek.com/v1/chat/completions'

def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    headers ={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data ={
        'model': modelo,
        'messages': [{'role':'user','content':mensaje}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  #Lo que nos dice esta línea es si existe un posible error HTTP
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err}"
    except Exception as e:
        return f"Error Inesperado: {e}"
    

def main():
    print("Bienvenido al chatbot de DeepSeek. Si usted desea salir escriba 'salir' para terminar")

    while True:
        mensaje_usuario = input("Tú: ")

        if mensaje_usuario.lower() == 'salir':
            print("Chatbot: Hasta Luego!")
            break 

        respuesta = enviar_mensaje(mensaje_usuario)
        print(f"Chatbot: {respuesta}")


if __name__ == "__main__":
    main()