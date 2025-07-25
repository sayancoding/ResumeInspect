from crewai import Crew,Process


from agents.ResumeParseAgent import ResumeParseAgent

class ResumeExtractCrew:
    resumeParseAgent = ResumeParseAgent()
    def __init__(self) -> None:
        self.crew = Crew(
            agents= [self.resumeParseAgent.agent],
            tasks=[self.resumeParseAgent.resume_extract_tak()],
            verbose=True 
        )