import streamlit as st
from app.agent import create_agent

st.set_page_config(page_title="Analisador de Vendas com IA")
st.title("Analisador de Vendas com IA")

question = st.text_input("Digite sua pergunta sobre os dados:")

# Cria o agente uma vez por sessão
if "agent" not in st.session_state:
    with st.spinner("Carregando agente..."):
        st.session_state.agent = create_agent('gemini')  # ou 'gpt'

if question:
    with st.spinner("Consultando IA..."):
        response = st.session_state.agent.run(question)
        st.write("### Resposta:")
        st.write(response)