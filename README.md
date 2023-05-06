# ArxivChatBot_StreamlitApp
A Chatbot based on openAI and streamlit for Arxiv 

## **Intro**

We create an ArxivChatBot App  using Streamlit, llama_index, Langchain and OpenAI.You need to have an account on OpenAI along
with its available Api key. The ChatBot is trained on a specific query, the number of files and a specific criterion. This ChatBot
is an extension of the  previous related Arxiv repos and is trained based on three parameters:
1. Search query
2. Number of files
3. Search criterion:
    - a)Relevance 
    - b)Last updated 
    - c)Submitt Date 
    



### **Quick Start**  
- Input the Open Api-key and press Enter.
- Input Query,number of files and choose Relevance, Last updated or Submitted date and press load.
- The maximum number of files you can enter are 50. 
- When you see the message "Arxiv papers are loaded based on the criteria" you are ready to chat as a User.
- Under the User ask the question and press the Submit button, wait a little and the Chatbot will respond you.

We are using the default chat model from OpenAI ChatGPT-4.

### Issues
It is not so fast during the training along with the response from the Chatbot engine.

### Future Prospectives 
We  are looking to improve the layout and be more self-explanatory. Also, we will provide
option to download the requested pdf files along with their abstracts. 

### **References**
1. https://github.com/StanfordVL/arxivbot/
2. https://github.com/emptycrown/llama-hub/blob/main/loader_hub/papers/arxiv/
3. https://llamahub.ai/l/papers-arxiv

