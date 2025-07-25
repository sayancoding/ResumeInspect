from crewai import Crew
from agents.ProfileMatacherAgent import ProfileMatcherAgent 

class MatcherCrew:
    matcherAgemt = ProfileMatcherAgent()
    def __init__(self) -> None:
        self.crew = Crew(
            agents= [self.matcherAgemt.agent],
            tasks=[self.matcherAgemt.matching_task()],
            verbose=True 
        )