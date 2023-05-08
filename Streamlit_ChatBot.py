from llama_index import download_loader, GPTSimpleVectorIndex
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings
from base import ArxivReader_mod_search, ArxivReader_mod
import os
import sys
import openai
import streamlit as st
#import numpy as np


# create the website reader
ArxivReader = download_loader("ArxivReader")
global index,dummy



st.set_page_config(page_title="My App")

st.header("Arxiv ChatBot ")
st.subheader(
    "I am a Chatbot Research Scientist. Please fill the fields below to start our discussion."
)


api_key = st.text_input('Open Api Key:')

if 'OPENAI_API_KEY' not in st.session_state:
   if api_key:
      st.session_state['OPENAI_API_KEY'] = api_key
      st.write(st.session_state.get('OPENAI_API_KEY'))



os.environ['OPENAI_API_KEY'] = str(st.session_state.get('OPENAI_API_KEY'))


query = st.text_input("What scientific topic do you want to discuss?")

max_query = st.number_input("How many papers should i investigate?", step=0)
dummy = st.radio(
    "According to which criterion?",
    ('Relevance', 'LastUpdated', 'SubmittedDate'))


#st.write(load_call(documents))
if query and max_query:
    if dummy == 'Relevance':
        search_query_int = 0

    if dummy== "LastUpdated":
        search_query_int = 1

    if dummy == "SubmittedDate":
        search_query_int = 2

    # load the reader
    loader = ArxivReader_mod()
    documents = loader.load_data(search_query=query,    papers_dir= "papers", max_results=max_query, search_criterion=search_query_int)
    index = GPTSimpleVectorIndex.from_documents(documents)
    st.markdown("Arxiv papers are loaded based on the criteria")



with st.form("my_form"):
    user = st.text_input("Ask me any question about "+query+":")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if user:
        response = str(index.query(user))
    if submitted:
        st.text_area("Bot:", response, height=500)
