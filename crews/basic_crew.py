from crewai import Crew

from agents.resume_query_agent import resume_query_agent
from tasks.resume_summary_task import resume_summary_task

basic_crew = Crew(
    agents=[resume_query_agent],
    tasks=[resume_summary_task],
    verbose=True
)