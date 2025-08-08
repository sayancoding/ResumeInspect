from crewai import Agent,Task

from config.app_config import get_google_llm

from core.tools import JDSearchTool
from core.tools import ResumeSearchTool

from core.CustomType import ProfileMatchingReport
from core.CustomType import JobRequirementInfo
from core.CustomType import ResumeInfo 

class ProfileMatcherAgent:
    llm = get_google_llm()

    def __init__(self) -> None:
        self.agent = Agent(
        role="Profile Matcher Agent",
        goal="Compare the extracted resume and job description data to determine a match score and analysis",
        tools=[ResumeSearchTool(),JDSearchTool()],
        backstory="A senior analyst who good at comparing resume and job requirements",
        verbose=True,
        llm=self.llm
        )      

    def matching_task(self)->Task:
        return Task( description=f"""Extract and compare the resume and job description(JD) using provided tools,
    compare on below information - 
        Candidate Experience and Required Experience in Years and Months (Hight Priority)
        Primary or required Skills, (Hight Priority)
        Secondary and Good to have skills, (medium priority)
        Location (very low priority)
    Calculate a match score (from 0 to 100).
    Provide a detailed of the match and area of improvement.
    Apply recommendation in 
        - poor (if score below 50)
        - moderate (between 50 to 75)
        - high (above 75)
    score calculation breakdown insight
                    """,
        agent= self.agent,
        expected_output="""Give the output concise way as JSON""",
        output_pydantic=ProfileMatchingReport
    )

class ResumeParseAgent:
    def __init__(self) -> None:
        self.agent = Agent(
        role="Resume Query Agent",
        goal="To extract resume information",
        backstory="You're able to query on pdf information using ResumeSearchTool, always first consolidated queries and then call the tools",
        tools=[ResumeSearchTool()],
        verbose=True,
        llm=get_google_llm()
        )
    
    def resume_extract_tak(self) -> Task:
        return Task(
        description="""
            extract below details from resume - 
            Name of Candidate, 
            Total years of experience, 
            Skill sets (Primary & Secondary),
            If have any certification
            Work or project experience
        """,
        agent= self.agent,
        expected_output= """Give the output concise way as only specified format""",
        output_pydantic=ResumeInfo
        )

class JDParserAgent:
    llm = get_google_llm()
    
    def __init__(self) -> None:
        self.agent = Agent(
        role="JD Parser Agent",
        goal="To extract JD information",
        backstory="You're able to query on jd information using JDSearchTool, always first consolidated queries and then call the tools",
        tools=[JDSearchTool()],
        verbose=True,
        llm=self.llm
        )
    
    def jd_extract_task(self) -> Task:
        return Task( description="""Extract job-title, Role family, Total years of experience, Required (primary) skills, Secondary skills are good to have, Location from given JD only,
                    if any not found, kept it blank and extract skills from only Specified on JD, Don't overthink or assume
                    """,
        agent= self.agent,
        expected_output="Give the output concise way as specified json format",
        output_pydantic= JobRequirementInfo
    )