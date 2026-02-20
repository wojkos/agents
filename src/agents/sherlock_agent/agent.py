import os

from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="sherlock_agent",
    model="gemini-2.0-flash",
    description="Agent z narzedziem google_search",
    instruction="""Jestes pomocnym asystentem ucznia odpowiadajacym jak Sherlock Holmes. Uzywaj narzedzia google_search, gdy potrzebujesz informacji z internetu.""",
    tools=[google_search],
)
