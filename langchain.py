from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import BSHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import load_agent
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from bs4 import BeautifulSoup 
from dotenv import load_dotenv
import requests
import transformers


load_dotenv()


model = 'text-davinci 003'
llm = OpenAI(model = model , temperature=0.7)
embeddings = OpenAIEmbeddings()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
    )



def create_faiss_vectorstore() -> FAISS:
    db = FAISS()
    return db

db = create_faiss_vectorstore() 

def tone_db_from_sample_document(sample):
    docs = text_splitter.split_documents(sample)
    db.from_documents(docs,embeddings)


def resume_db(resume):

    docs = text_splitter.split_documents(resume)
    db.from_documents(docs,embeddings)


def internship_details_db_from_url(url):

    loader = BSHTMLLoader(url)
    data = loader.load()

    docs = text_splitter.split_documents(data)

    db.from_documents(docs,embeddings)





