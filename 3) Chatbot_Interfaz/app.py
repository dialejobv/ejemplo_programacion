import streamlit as st
import requests

# Configuración de la página
st.set_page_config(
    page_title="Chatbot DeepSeek",
    page_icon="🤖",
    layout="centered"
)

# API Configuration
API_KEY = ''
API_URL = 'https://api.deepseek.com/v1/chat/completions'

def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    """Envía un mensaje al API de DeepSeek y retorna la respuesta"""
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': modelo,
        'messages': [{'role': 'user', 'content': mensaje}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)

        if response.status_code != 200:
            error_detail = response.json() if response.text else "Sin detalles"
            return f"❌ Error {response.status_code}: {error_detail}"

        return response.json()['choices'][0]['message']['content']

    except requests.exceptions.Timeout:
        return "⏰ Tiempo de espera agotado. Por favor, intenta de nuevo."
    except requests.exceptions.RequestException as e:
        return f"🔌 Error de conexión: {e}"
    except Exception as e:
        return f"⚠️ Error Inesperado: {e}"

def main():
    # Título y descripción
    st.title("🤖 Chatbot DeepSeek")
    st.markdown("---")
    
    # Sidebar con información
    with st.sidebar:
        st.header("⚙️ Configuración")
        st.write("Modelo: DeepSeek Chat")
        st.write("Estado: ✅ Conectado")
        
        # Botón para limpiar el historial
        if st.button("🗑️ Limpiar conversación"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        st.caption("Desarrollado con Streamlit y DeepSeek API")
    
    # Inicializar el historial de mensajes en session_state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Verificar la API al inicio
    if not st.session_state.messages:
        test_response = enviar_mensaje("Hola")
        if "Error" in test_response or "❌" in test_response:
            st.error(f"⚠️ No se pudo conectar con la API: {test_response}")
            st.info("Por favor, verifica tu API Key en https://platform.deepseek.com/")
            return
    
    # Mostrar mensajes anteriores
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input del usuario
    if prompt := st.chat_input("Escribe tu mensaje aquí..."):
        # Agregar mensaje del usuario al historial
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Mostrar mensaje del usuario
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Obtener respuesta del bot
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = enviar_mensaje(prompt)
                st.markdown(response)
        
        # Agregar respuesta al historial
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()