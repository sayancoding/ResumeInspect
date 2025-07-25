import asyncio

from utils.VectorStore import VectorStore
from tools.CustomTool import JDSearchTool

jd = """
    we are hiring Java developer years of experience 3-8,
    Should have Java and Spring boot, microservice
    location would be PAN India
    Aws,or any cloud is good to have
"""
async def main():
    # vs = VectorStore()
    # await vs.store_Jd_as_Vector(jd)
    # await vs.store_resume_as_Vector('./data/resume.pdf')

    from crews.ResumeExtractCrew import ResumeExtractCrew 
    resume_response = ResumeExtractCrew().crew.kickoff()
    print(resume_response)

    from crews.JdExtractCrew import JdExtractCrew
    jd_response = JdExtractCrew().crew.kickoff()
    print(jd_response) 

    from crews.MatcherCrew import MatcherCrew
    match_response = MatcherCrew().crew.kickoff(inputs={'resume_output': resume_response, 'jd_output':jd_response })
    print(match_response) 

if __name__ == "__main__":
    asyncio.run(main())



