from langchain_community.document_loaders import PyPDFLoader
#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import load_agent
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from bs4 import BeautifulSoup 
from dotenv import load_dotenv
import requests


#load_dotenv()

#embeddings = OpenAIEmbeddings()
#text_splitter = RecursiveCharacterTextSplitter()
model = 'Some OpenAI LLM'
#llm = OpenAI(model = model , temperature=0.7)


prompt = PromptTemplate(

    input_variables=[],
    template= '''
'''
)

def get_internship_details(url):   

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html parser')
        extracted_html = soup.prettify()

        print(extracted_html)

url = "https://en.wikipedia.org/wiki/Website#:~:text=A%20website%20(also%20written%20as,commerce%2C%20entertainment%20or%20social%20networking."
get_internship_details(url=url)




