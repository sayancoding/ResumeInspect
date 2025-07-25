from utils.VectorStore import VectorStore

class VectorRetriever:

    def get_resume_retriever(self):
        resume_vs = VectorStore().get_resume_vector()
        return resume_vs.as_retriever()

    def get_JD_retriever(self):
        jd_vs = VectorStore().get_JD_vector()
        return jd_vs.as_retriever()