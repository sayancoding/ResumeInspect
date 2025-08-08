from crewai.tools import BaseTool

from utils.VectoreRetriever import VectorRetriever

class ResumeSearchTool(BaseTool): 
    name:str = "Resume Retriever Tool"
    description:str = "Search related information on resume only ,if not found do nothing"

    def _run(self,query:str):
        responsesFromVs = VectorRetriever().get_resume_retriever().invoke(query,k=3)
        print(f"Search list size from vector store : {len(responsesFromVs)}")
        info = []
        for res in responsesFromVs:
            info.append(res.page_content)
        return "\n".join(info)
    
class JDSearchTool(BaseTool): 
    name:str = "JD Retriever Tool"
    description:str = "Search only related information on JD ,if not found do nothing"

    def _run(self,query:str):
        responsesFromVs = VectorRetriever().get_JD_retriever().invoke(query)
        print(f"Search list size from vector store : {len(responsesFromVs)}")
        info = []
        for res in responsesFromVs:
            info.append(res.page_content)
        return "\n".join(info)