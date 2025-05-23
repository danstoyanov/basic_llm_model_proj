import os
import streamlit as st
from llama_cpp import Llama

MODEL_NAME = "Phi-3-mini-4k-instruct-q4.gguf"


def check_model():
    if not os.path.exists(MODEL_NAME):
        st.error(
            "❌ Моделът липсва! Свали го от: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf")
        st.stop()


@st.cache_resource
def load_model():
    check_model()
    return Llama(
        model_path=MODEL_NAME,
        n_ctx=1024,
        n_gpu_layers=35,
        n_threads=6
    )


def generate_response(llm, prompt):  # <-- Ключовата липсваща част!
    try:
        response = llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=256,
            stream=False
        )
        return response
    except Exception as e:
        st.error(f"Грешка: {str(e)}")
        return None


st.title("🫃 НАЩО МОМЧЕ")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Пиши съобщение..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Мисля..."):
        llm = load_model()
        response = generate_response(llm, prompt)
        ai_response = response['choices'][0]['message']['content']

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response})
    st.rerun()
