import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = ChatOpenAI(
    model = os.getenv("MODEL"),
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY","dockermodelrunner")
)

st.title("LLM CHAT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

prompt = st.chat_input(
    "You..."
)

if prompt:
    st.session_state.messages.append({"role": "user", 
                                      "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        response = client.invoke(
            input=st.session_state.messages
        )

        st.session_state.messages.append({"role": "assistant", 
                                          "content": response.content})

    except Exception as e:
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"⚠️ Error: {str(e)}"
        })
