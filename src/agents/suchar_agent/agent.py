import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# https://docs.litellm.ai/docs/providers/openrouter
model = LiteLlm(
    model="openrouter/openai/gpt-4.1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def zapodaj_suchara():
    jokes = [
        "Dlaczego komputerowi jest zimno? Bo ma za dużo okien.",
        "Co mówi jedna ściana do drugiej? Spotkamy się na rogu.",
        "Dlaczego słoń nie korzysta z komputera? Bo boi się myszy.",
        "Czemu rower nie może stać sam? Bo jest dwukołowy.",
        "Co robi księżyc, gdy jest głodny? Zjada gwiazdki.",
        "Co mówi kaczka, gdy widzi rachunek? Kwaczę!",
        "Dlaczego pająk to dobry informatyk? Bo włada siecią.",
        "Co robi ślimak na wyścigu? Spóźnia się, ale z klasą.",
        "Jak nazywa się kot, który surfuje po internecie? Cyberkot.",
    ]
    return random.choice(jokes)

profil = {}

def pokaz_profil():
    """Zwraca imię, wiek i zainteresowania użytkownika."""
    profil['imie'] = "Jon"
    profil['wiek'] = 11
    profil['zainteresowania'] = ["suchary"]
    return profil

root_agent = Agent(
    name="suchar_agent",
    model=model,
    description="Agent opowiadający suchary i polecający filmy",
    instruction="""
    Opowiadaj suchary i pomagaj z wyborem filmu.
    - Suchary: użyj `zapodaj_suchara()`.
    - Pokaż profil: `pokaz_profil()`.
    - Polec filmy: gdy ktoś pyta "Jaki film mam obejrzeć?" użyj `pokaz_profil()` aby poznać zainteresowania.
    """,
    tools=[zapodaj_suchara, pokaz_profil],
)
