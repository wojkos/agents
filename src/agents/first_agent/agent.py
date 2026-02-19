from google.adk.agents import Agent

root_agent = Agent(
    name="first_agent",
    model="gemini-2.0-flash",
    description="My first agent",
    instruction="""Jestes pomocnym asystentem ucznia odpowiadajacym jak ..."""
)
