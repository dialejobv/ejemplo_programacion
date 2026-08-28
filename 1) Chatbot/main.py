import requests

API_KEY = ''
API_URL = 'https://api.deepseek.com/v1/chat/completions'

def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': modelo,
        'messages': [{'role': 'user', 'content': mensaje}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)

        # Verificar si la respuesta no es exitosa
        if response.status_code != 200:
            error_detail = response.json() if response.text else "Sin detalles"
            return f"Error {response.status_code}: {error_detail}"

        return response.json()['choices'][0]['message']['content']

    except requests.exceptions.RequestException as e:
        return f"Error de conexión: {e}"
    except Exception as e:
        return f"Error Inesperado: {e}"

def main():
    print("Bienvenido al chatbot de DeepSeek. Escribe 'salir' para terminar")

    # Verificar que la API key funciona al inicio
    test_response = enviar_mensaje("Hola")
    if "Error" in test_response:
        print(f"⚠️ {test_response}")
        print("Por favor, verifica tu API Key en https://platform.deepseek.com/")
        return

    while True:
        mensaje_usuario = input("Tú: ")

        if mensaje_usuario.lower() == 'salir':
            print("Chatbot: ¡Hasta Luego!")
            break

        respuesta = enviar_mensaje(mensaje_usuario)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    main()