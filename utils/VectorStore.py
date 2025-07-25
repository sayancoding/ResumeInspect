from utils.Splitters import Splitters
from config.app_config import get_google_embedding
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader

class VectorStore:
    
    jd_index_path = "./faiss/jd_index"
    resume_index_path = "./faiss/resume_index"

    def __init__(self) -> None:
        self.splitter = Splitters().get_text_splitter()
        self.embeddings = get_google_embedding()

    async def store_Jd_as_Vector(self,jd:str):
        print("JD is embedding and storing to vector-store..")
        splits = self.splitter.split_text(jd)
        print(f"JD info is splitted up {len(splits)} chunks..")
        documents = [Document(page_content=text) for text in splits]
        jd_vs = FAISS.from_documents(documents,self.embeddings)
        jd_vs.save_local(self.jd_index_path)
        print("Save JD as embedded in FAISS.")
    
    async def store_resume_as_Vector(self,resume_path:str):
        print("Resume is embedding and storing to vector-store..")
        pdf_loader = PyPDFLoader(resume_path)
        splits = self.splitter.split_documents(pdf_loader.load())
        print(f"Resume info is splitted up {len(splits)} chunks..")
        vs = FAISS.from_documents(splits,self.embeddings)
        vs.save_local(self.resume_index_path)
        print("Save Resume as embedded in FAISS.")

    def get_JD_vector(self):
        return FAISS.load_local(
            self.jd_index_path,
            self.embeddings,
            allow_dangerous_deserialization=True)
    
    def get_resume_vector(self):
        return FAISS.load_local(
            self.resume_index_path,
            self.embeddings,
            allow_dangerous_deserialization=True)
