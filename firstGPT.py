import streamlit as st
import os
from langchain_openai import OpenAI
from apikey import apikey


os.environ['OPENAI_API_KEY'] = apikey

# app framework
st.title('ASK QUESTIONS ABOUT ME')
prompt = st.text_input('Plug in your prompt here')

# llms
llm = OpenAI(temperature=0.9) # temperature defined how creative llm is 

# show stuff to the screen if there is prompt
if prompt:
    response = llm(prompt)
    st.write(response)