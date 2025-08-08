from utils.VectorStore import VectorStore
import json

class AppFeature:
    def __init__(self) -> None:
        pass

    async def upload_jd(self, jd:str):
        vs = VectorStore()
        await vs.store_Jd_as_Vector(jd)
        print("JD is uploaded..")

    async def embedding_resume(self):
        vs = VectorStore()
        await vs.store_resume_as_Vector('./data/resume.pdf')
        print("resume is uploaded..")

    def matching_resume_jd(self):
        from core.crews import ProfileMatcherCrew
        
        match_response = ProfileMatcherCrew().crew.kickoff()
        print(str(match_response))
        # yield (match_response.raw)
        yield json.loads(match_response.raw)
    
    