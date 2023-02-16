# Importing required packages
import streamlit as st
import openai
import os

from gpt_index import GPTSimpleVectorIndex

st.title("Ask Aifa 🧠")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''Aifa is a web app that offers medical information to patients in natural language. 
        It has been trained on a large corpus of text and can provide quick and accurate answers to medical queries. 
        Simply type your question in the text box and hit enter to get a response. 
        \n\nIt should not be used as a substitute for professional medical advice.
       '''
    )
# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
os.environ["OPENAI_API_KEY"] = "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"

def main():
    '''
    This function gets the user input, pass it to GPT index function and 
    displays the response
    '''
    # Load index
    #index = GPTSimpleVectorIndex.load_from_disk('SVindex-BMJ.json')
    # Get user input
    user_query = st.text_input("Enter query here, to exit enter :q", "How does Aspirin work?")
    if user_query != ":q" or user_query != "":
        # Pass the query to the GPT index function
        response = index.query(user_query, response_mode="tree_summarize")
        return st.write(f"{user_query}  \n\n {response}")

main()
