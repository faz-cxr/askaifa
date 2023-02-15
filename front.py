"""Python file to serve as the frontend"""
import os
import streamlit as st
import openai

from gpt_index import GPTSimpleVectorIndex
from pathlib import Path
from gpt_index import download_loader
from streamlit_chat import message

openai.api_key = os.environ["OPENAI_API_KEY"]

history_input = []

st.set_page_config(
    page_title="Ask Aifa",
    page_icon=":robot:"
)

st.header("Ask about anything medical")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("Chatting is not possible right now. Do not ask follow up questions. Frame your questions in full below: ", key="input")
    return input_text 

user_input = get_text()
index = GPTSimpleVectorIndex.load_from_disk('SVindex-BMJ.json')

if user_input:
    response = index.query(user_input, response_mode="compact")
    output = str(response)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
