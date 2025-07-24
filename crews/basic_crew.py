from crewai import Crew

from agents.resume_query_agent import resume_query_agent
from tasks.question_task import question_task

basic_crew = Crew(
    agents=[resume_query_agent],
    tasks=[question_task],
    verbose=True
)