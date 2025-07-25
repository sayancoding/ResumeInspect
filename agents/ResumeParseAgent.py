from crewai import Agent,Task

from tools.CustomTool import ResumeSearchTool
from config.app_config import get_google_llm

class ResumeParseAgent:
    def __init__(self) -> None:
        self.agent = Agent(
        role="Resume Query Agent",
        goal="To extract resume information",
        backstory="You're able to query on pdf information using ResumeSearchTool",
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
        expected_output= """Give the output concise way as below example format only

        {
          "name" : "...",
          "email" : "...",
          "job_role": "...",
          "job_family": "...",
          "total_experience" : "2+ years ",
          "primary_skills": [...],
          "secondary_skills": [...],
          "current_location: "...",
          "work_experience" : [...],
          "certifications": [...]
        }
        """
        )
