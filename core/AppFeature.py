from utils.VectorStore import VectorStore




class AppFeature:
    def __init__(self) -> None:
        pass

    async def upload_jd(self, jd:str):
        vs = VectorStore()
        await vs.store_Jd_as_Vector(jd)
        print("JD is uploaded..")

    async def upload_resume(self, jd:str):
        vs = VectorStore()
        await vs.store_resume_as_Vector('./data/resume.pdf')
        print("resume is uploaded..")