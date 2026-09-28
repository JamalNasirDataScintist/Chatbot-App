import streamlit as st
from chatbot import ask_gemini

st.set_page_config(
    page_title="PMA Chatbot",
    page_icon="🎖️",
    layout="centered"
)

st.title("🎖️ Pakistan Military Academy Chatbot")

st.write("Ask any question related to Pakistan Military Academy.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("Thinking..."):
        answer = ask_gemini(question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)