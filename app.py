import streamlit as st
from database import limpar_historico
from database import (
    criar_tabela,
    salvar_mensagem,
    carregar_historico,
)
from chatbot import gerar_resposta
from chatbot import criar_chat

# Configuração da página
st.set_page_config(
    page_title="MemoryChat AI",
    page_icon="🤖",
    layout="wide",
)


# Tema visual
st.markdown(
    """
    <style>
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
    }

    .main {
        background-color: #0E1117;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Inicializa banco
criar_tabela()


# Título
st.title("🤖 MemoryChat AI")
st.caption("Chatbot com memória persistente usando Gemini")


# Carrega histórico
historico = carregar_historico()

with st.sidebar:
    st.title("🚀 MemoryChat AI")
    st.markdown("---")
    st.markdown("### Tecnologias")
    st.markdown("""
    - Python
    - Gemini API
    - SQLite
    - Streamlit
    """)
    if st.button("🗑️ Limpar conversa"):
        limpar_historico()
        st.session_state.chat = criar_chat()
        st.rerun()

# Exibe histórico
for role, mensagem in historico:
    with st.chat_message(role):
        st.markdown(mensagem)


# Input do usuário
prompt = st.chat_input("Digite sua mensagem...")


if prompt:
    # Exibe usuário
    with st.chat_message("user"):
        st.markdown(prompt)

    salvar_mensagem("user", prompt)

    # Gera resposta
    resposta = gerar_resposta(prompt)

    # Exibe IA
    with st.chat_message("assistant"):
        st.markdown(resposta)

    salvar_mensagem("assistant", resposta)