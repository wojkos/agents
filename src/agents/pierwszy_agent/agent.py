from google.adk.agents import Agent

root_agent = Agent(
    name="pierwszy_agent",
    model="gemini-2.0-flash",
    description="Mój pierwszy agent",
    instruction="""Jestes pomocnym asystentem ucznia odpowiadajacym jak ..."""
)
