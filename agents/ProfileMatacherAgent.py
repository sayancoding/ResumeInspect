from crewai import Agent,Task

from config.app_config import get_google_llm

class ProfileMatcherAgent:
    llm = get_google_llm()
    
    def __init__(self) -> None:
        self.agent = Agent(
        role="Profile Matcher Agent",
        goal="""Compare given this resume and given this jd and priority primary skills , experience and job-role""",
        backstory="You're expert to match jd and resume details.",
        verbose=True,
        llm=self.llm
        )

    def matching_task(self)->Task:
        return Task( description="""Given resume {resume_output} and JD {jd_output}
                    Compare both and return details with 
                    - Score out of 100
                    - matches
                    - area of improvement
                    - Apply recommendation in 
                        - poor (if score below 50)
                        - moderate (between 50 to 75)
                        - high (above 75)
""",
        agent= self.agent,
        expected_output="""Give the output concise way as below example format
        {
          "score": "...",
          "matches": [...],
          "area_of_improvements": [...],
          "apply_recommendation"..."
        }
        """
    )