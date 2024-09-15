import streamlit as st
import pandas as pd
import openai
import os
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

# Additional imports
from langchain.docstore.document import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS  # or use Chroma if FAISS is not available

# OpenAI API Key
openai.api_key = ""  # Replace with your actual API key

# Load CSV file into a DataFrame
@st.cache_data
def load_data(file_path='home_properties.csv'):
    return pd.read_csv(file_path)

# Automatically load the CSV file
data = load_data()

# Display data
# st.write("Here is the data:")
# st.dataframe(data)

st.title("Personal Housing Agent")
st.write("Start off by describing your needs so your agent can assist you!")

# Step 1: Convert DataFrame to documents
def dataframe_to_documents(df):
    documents = []
    for index, row in df.iterrows():
        content = " ".join([f"{column}: {row[column]}" for column in df.columns])
        documents.append(Document(page_content=content))
    return documents

documents = dataframe_to_documents(data)

# Step 2: Create embeddings
embeddings = OpenAIEmbeddings()

# Step 3: Create vector store
vectorstore = FAISS.from_documents(documents, embeddings)
# If FAISS is not available, you can use Chroma:
# from langchain.vectorstores import Chroma
# vectorstore = Chroma.from_documents(documents, embeddings)

# Step 4: Create retriever
retriever = vectorstore.as_retriever()

# Step 5: Set up LangChain with LLM and retriever
model = OpenAI(temperature=0.0)

# Define a custom prompt for the QA chain
qa_template = """
You are an assistant that helps users find houses based on the provided data. You are only able to answer using data from what the csv that we provided you. Also make sure to answer only in normal letters, no italics or anything like that. This previous one is very important. Every one of your answers should return only in plain text, no matter what is in your data. Do not provide any specific listing numbers such as "the fourth listing..." or "first listing". also make sure to include the price if they ask for more information about it.

Use the following context to answer the user's question.

{context}

Conversation history:
{chat_history}

Question: {question}

Assistant:
"""

QA_PROMPT = PromptTemplate(
    input_variables=["context", "chat_history", "question"],
    template=qa_template
)

# Define a custom prompt for the question generator
condense_question_template = """
Given the following conversation and a follow-up question, rephrase the follow-up question to be a standalone question.

Conversation history:
{chat_history}

Follow-up question: {question}

Standalone question:
"""

CONDENSE_QUESTION_PROMPT = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=condense_question_template
)

# Create the question generator chain
question_generator = LLMChain(
    llm=model,
    prompt=CONDENSE_QUESTION_PROMPT
)

# Create the QA chain with the custom prompt
qa_chain = load_qa_chain(
    llm=model,
    chain_type="stuff",
    prompt=QA_PROMPT
)

# Create the ConversationalRetrievalChain using the custom QA chain and question generator
conversational_chain = ConversationalRetrievalChain(
    retriever=retriever,
    question_generator=question_generator,
    combine_docs_chain=qa_chain
)

# Initialize the conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display the conversation history
for i, (user_msg, bot_msg) in enumerate(st.session_state.chat_history):
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)

# Get user input using chat input box
user_input = st.chat_input("Ask your house finding questions:")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Query the model
    result = conversational_chain(
        {"question": user_input, "chat_history": st.session_state.chat_history}
    )
    answer = result['answer']

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Update the chat history
    st.session_state.chat_history.append((user_input, answer))

