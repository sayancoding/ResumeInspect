from crewai import Agent

from tools.ResumeSearchTool import ResumeSearchTool
from config.app_config import get_google_llm

llm = get_google_llm()

resume_query_agent = Agent(
    role="Resume Query Agent",
    goal="To Query vector store where resume information is embedded",
    backstory="You're able to query on pdf information using ResumeSearchTool",
    tools=[ResumeSearchTool()],
    verbose=True,
    llm=llm
)