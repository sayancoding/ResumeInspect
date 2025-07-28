from utils.VectorStore import VectorStore

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

    async def matching_resume_jd(self):
        from crews.JdExtractCrew import JdExtractCrew
        from crews.ResumeExtractCrew import ResumeExtractCrew 
        from crews.MatcherCrew import MatcherCrew

        """Parse / Extract info from Resume"""
        resume_response = ResumeExtractCrew().crew.kickoff()
        print(resume_response)

        """Parse / Extract info from JD"""
        jd_response = JdExtractCrew().crew.kickoff()
        print(jd_response) 
        
        """Matching both JD and resume and analyzing"""
        match_response = MatcherCrew().crew.kickoff(inputs={'resume_output': str(resume_response.raw), 
                                                    'jd_output': str(jd_response.raw) })
        return match_response.raw