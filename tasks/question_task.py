from crewai import Task

from agents.resume_query_agent import resume_query_agent

question_task = Task(
    description="{question}",
    agent= resume_query_agent,
    expected_output="Give the output concise way and be clean and clear"
)