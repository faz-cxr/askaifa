import streamlit as st
import os
import openai
from datetime import datetime
from streamlit.components.v1 import html
from gpt_index import GPTSimpleVectorIndex
import pandas as pd
import csv
st.set_page_config(page_title="Ask Aifa 🧠")

html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

with st.sidebar:
    st.markdown("""
    # About 
    \n*Aifa* is a web app that answers medical queries in **natural language**.
    \n\n**Do not** use *Aifa* as a substitute for professional medical advice.
    \n\n\nComing Soon: Chat with *Aifa!*
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.64)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    \n*Aifa* has been trained on a large corpus of medical text and can provide quick and accurate responses. 
    \nSimply type your question in the text box and hit enter to get a response. 
    You can also download the output as txt.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.64)"),unsafe_allow_html=True)
    st.markdown("""
    <a href = "mailto:abc@example.com?subject = Feedback&body = Message">Send Feedback</a>
    """,
    unsafe_allow_html=True,
    )


input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0

if st.session_state['output'] <=5:
    st.markdown("""
    # Ask Aifa 🧠
    """)
    input_text = st.text_input("Start typing below and click enter ⏎", disabled=False, placeholder="Example: What's the difference between cold and flu?")
    st.session_state['output'] = st.session_state['output'] + 1
else:
    # input_text = st.text_input("Brainstorm ideas for", disabled=True)
    st.info("Thank you! Refresh to ask more")
    st.markdown('''
    <a target="_blank" style="color: black" href="https://twitter.com/intent/tweet?text=I%20just%20used%20the%20Ask%20Aifa%20App%0A%0Ahttps://askaifa.streamlit.app/">
        <button class="btn">
            Tweet about this!
        </button>
    </a>
    <style>
    .btn{
        display: inline-flex;
        -moz-box-align: center;
        align-items: center;
        -moz-box-pack: center;
        justify-content: center;
        font-weight: 400;
        padding: 0.25rem 0.75rem;
        border-radius: 0.25rem;
        margin: 0px;
        line-height: 1.6;
        color: #fff;
        background-color: #00acee;
        width: auto;
        user-select: none;
        border: 1px solid #00acee;
        }
    .btn:hover{
        color: #00acee;
        background-color: #fff;
    }
    </style>
    ''',
    unsafe_allow_html=True
    )

hide="""
<style>
footer{
	visibility: hidden;
    position: relative;
}
.viewerBadge_container__1QSob{
    visibility: hidden;
}
#MainMenu{
	visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
if input_text:
    prompt = str(input_text)
    if prompt:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        index = GPTSimpleVectorIndex.load_from_disk('SVindex-BMJ.json')
        response = index.query(prompt, response_mode="tree_summarize")
        query_output = response
        today = datetime.today().strftime('%Y-%m-%d')
        topic = input_text+"\n@Date: "+str(today)+"\n"+str(query_output)
        
        st.info(query_output)
        filename = "answers_"+str(today)+".txt"
        btn = st.download_button(
            label="Download txt",
            data=topic,
            file_name=filename
        )
        fields = [input_text, query_output, str(today)]
        # read local csv file
        r = pd.read_csv('./data/prompts.csv')
        if len(fields)!=0:
            with open('./data/prompts.csv', 'a', encoding='utf-8', newline='') as f:
                # write to csv file (append mode)
                writer = csv.writer(f, delimiter=',', lineterminator='\n')
                writer.writerow(fields)
