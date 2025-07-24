from dotenv import load_dotenv
import os
from crewai import LLM
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

def get_google_llm():
    if not GOOGLE_API_KEY :
        raise ValueError("Google LLM API is not Found!!")
    
    llm = LLM(
    model='gemini/gemini-2.5-flash',
    api_key=GOOGLE_API_KEY,
    temperature = 0.5)

    return llm

def get_google_embedding():
    if not GOOGLE_API_KEY :
        raise ValueError("Google LLM API is not Found!!")
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")


