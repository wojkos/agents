import os

from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="google_search_agent",
    model="gemini-2.0-flash",
    description="Tool agent with google search",
    instruction="""You are a helpful assistant that can use the following tools:
    - google_search: Search the web for information""",
    tools=[google_search],
)
