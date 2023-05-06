from llama_index import GPTSimpleVectorIndex, download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings
from base import ArxivReader_mod_search, ArxivReader_mod
import os
import openai
import streamlit as st
#import numpy as np



# create the website reader
ArxivReader = download_loader("ArxivReader")
global index,dummy

st.set_page_config(page_title="My App")

st.header("Arxiv ChatBot ")
st.subheader(
    "A Scientific Chatbot  based on  Arxiv Papers. Ask anything based on the"
    " 1)query 2)no of files and 3)selection criteria "
)

api_key = st.text_input('Open Api Key:')
if 'OPENAI_API_KEY' not in st.session_state:
   if api_key:
      st.session_state['OPENAI_API_KEY'] = api_key
      st.write(st.session_state.get('OPENAI_API_KEY'))



os.environ['OPENAI_API_KEY'] = str(st.session_state.get('OPENAI_API_KEY'))


query = st.text_input("Query:")
max_query = st.number_input("Number of files(integer number):", step=0)
dummy = st.radio(
    "Search Criterion",
    ('Relevance', 'LastUpdated', 'SubmittedDate'))



if st.button('load') :
    if query and max_query and dummy:
        dummy1 = dummy  # radio_query.get()
        if dummy1 == 'Relevance':
            search_query_int = 0

        if dummy1 == "LastUpdated":
            search_query_int = 1

        if dummy1 == "SubmittedDate":
            search_query_int = 2

        # load the reader
        loader = ArxivReader_mod()
        documents = loader.load_data(search_query=query,    papers_dir= "hey", max_results=max_query, search_criterion=search_query_int)

        # create an index of the data for the AI to be able to read
        index = GPTSimpleVectorIndex.from_documents(documents)
        index.save_to_disk('index.json')
        st.markdown("Arxiv papers are loaded based on the criteria")


with st.form("my_form"):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    user = st.text_input("User:")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if user:
        response = str(index.query(user))
    if submitted:
        st.text_area("Bot:", response, height=500)