import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Ricardin - Chatbot com IA", layout="centered")
st.title("🤖 Ricardin - Seu Chatbot com IA Generativa")
st.markdown("Converse com o Ricardin! Faça uma pergunta ou peça uma explicação e ele responderá com inteligência.")

@st.cache_resource
def carregar_modelo():
    return pipeline("text2text-generation", model="google/flan-t5-base")

modelo_ia = carregar_modelo()

prompt = st.text_area("💬 O que deseja perguntar ao Ricardin?", height=100)

if st.button("🧠 Obter resposta do Ricardin"):
    if prompt.strip() == "":
        st.warning("Digite algo para que o Ricardin possa responder.")
    else:
        with st.spinner("Ricardin está pensando..."):
            resposta = modelo_ia(prompt, max_length=200, do_sample=True)[0]['generated_text']
            st.success("💡 Resposta do Ricardin:")
            st.write(resposta)