from crewai import Agent,Task

from tools.CustomTool import JDSearchTool
from config.app_config import get_google_llm

class JDParserAgent:
    llm = get_google_llm()
    
    def __init__(self) -> None:
        self.agent = Agent(
        role="JD Parser Agent",
        goal="To extract JD information",
        backstory="You're able to query on jd information using JDSearchTool",
        tools=[JDSearchTool()],
        verbose=True,
        llm=self.llm
        )
    
    def jd_extract_task(self) -> Task:
        return Task( description="""Extract job-title or Role family, Total years of experience, Required (primary) skills, Secondary skills are good to have, Location from given JD only, 
                    if any not found, kept it blank and extract skills from only Specified on JD, Don't overthink or assume
                    """,
        agent= self.agent,
        expected_output="Give the output concise way as only bullet points"
    )