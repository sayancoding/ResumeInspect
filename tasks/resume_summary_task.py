from crewai import Task

from agents.resume_query_agent import resume_query_agent

resume_summary_task = Task(
    description="Extract candidate-name, total years of experience, skill-sets, project work experience, certificate or awards if any, based on guess roles title",
    agent= resume_query_agent,
    expected_output="Give the output concise way as json format"
)