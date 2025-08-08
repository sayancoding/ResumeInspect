
from core.agents import ProfileMatcherAgent 
from crewai import Crew

class ProfileMatcherCrew:
    profileMatcherAgent = ProfileMatcherAgent().agent
    profileMatcherTask = ProfileMatcherAgent().matching_task()

    def __init__(self) -> None:
        self.crew = Crew(
            agents= [self.profileMatcherAgent],
            tasks=[self.profileMatcherTask],
            verbose=True 
        )