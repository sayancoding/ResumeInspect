from crewai.tools import BaseTool

from utils.retriver import get_resume_retriever

resume_retriever = get_resume_retriever()

class ResumeSearchTool(BaseTool): 
    name:str = "Resume Retriever Tool"
    description:str = "Search related information on resume"

    def _run(self,query:str):
        responsesFromVs = resume_retriever.invoke(query,k=3)
        print(f"Search list size from vector store : {len(responsesFromVs)}")
        info = []
        for res in responsesFromVs:
            info.append(res.page_content)
        return "\n".join(info)