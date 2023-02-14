"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message
import faiss
from langchain import OpenAI
from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.agents import initialize_agent
from gpt_index import GPTSimpleVectorIndex
import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

# Load the LangChain.
index = GPTSimpleVectorIndex.load_from_disk('SVindex-BMJ.json')

tools = [
    Tool(
        name = "GPT Index",
        func=lambda q: str(index.query(q)),
        description="useful for when you want to answer questions about the author. The input to this tool should be a complete english sentence.",
        return_direct=True
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history")
llm=OpenAI(temperature=0)

chain = initialize_agent(tools, llm, agent="conversational-react-description", memory=memory)


# From here down is all the StreamLit UI.
st.set_page_config(page_title="Aifa QA Bot", page_icon=":robot:")
st.header("Aifa QA Bot")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text


user_input = get_text()

if user_input:
    result = chain({"question": user_input})
    output = f"Answer: {result['answer']}\nSources: {result['sources']}"

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
