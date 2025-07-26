from crewai import Crew
from agents.JDParserAgent import JDParserAgent

class JdExtractCrew:
    jdParserAgent = JDParserAgent()
    def __init__(self) -> None:
        self.crew = Crew(
            agents= [self.jdParserAgent.agent],
            tasks=[self.jdParserAgent.jd_extract_task()],
            verbose=True
            )