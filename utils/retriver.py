from utils.splitters import get_text_splitter
from config.app_config import get_google_embedding

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

text_splitter = get_text_splitter()
embeddings = get_google_embedding()

def get_resume_retriever():
    resume_index_path = "./faiss_index"
    # PDF Loader
    pdf_loader = PyPDFLoader("./data/resume.pdf")
    splits = text_splitter.split_documents(pdf_loader.load())
    print(f"resume info is splitted up {len(splits)} chunks..")
    vs = FAISS.from_documents(splits,embeddings)
    vs.save_local(resume_index_path)
    retriever = vs.as_retriever()
    return retriever