from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool
from crewai import LLM

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY :
    raise ValueError("Google LLM API is not Found!!")

# initialization 
llm = LLM(
    model='gemini/gemini-2.5-flash',
    api_key=GOOGLE_API_KEY,
    temperature = 0.5)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") 
vector_db_path = "faiss_index"

# PDF Loader
pdf_loader = PyPDFLoader("./data/resume.pdf")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000,chunk_overlap=200)
splits = text_splitter.split_documents(pdf_loader.load())
# print(f"Chunking documents => {splits}")

vs = FAISS.from_documents(splits,embeddings)
vs.save_local(vector_db_path)
retriever = vs.as_retriever()

class PdfSearchTool(BaseTool): 
    name:str = "PDF Retriever Tool"
    description:str = "Search related information."

    def _run(self,query:str):
        responsesFromVs = retriever.invoke(query,k=3)
        print(f"Search list size from VS :: {len(responsesFromVs)}")
        info = []
        for res in responsesFromVs:
            info.append(res.page_content)
        return "\n".join(info)

pdf_query_agent = Agent(
    role="Query Agent",
    goal="To Query vector store where pdf information is embedded",
    backstory="You're able to query on pdf information using PdfSearchTool",
    tools=[PdfSearchTool()],
    verbose=True,
    llm=llm
)

task = Task(
    description="{question}",
    agent= pdf_query_agent,
    expected_output="Give the output concise way and be clean and clear"
)

crew = Crew(
    agents=[pdf_query_agent],
    tasks=[task],
    verbose=True
)

res = crew.kickoff(inputs={'question': 'What is candidate name ? '})
print(res)

