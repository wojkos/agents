"""
Twórca pytań testowych (agent 3).

Zadanie: na podstawie 'podsumowanie' stworzyć 5 pytań testowych, które sprawdzą
zrozumienie kluczowych punktów. Każde pytanie w osobnej linii, numerowane.
Format: '1) Pytanie — (A) ... (B) ... (C) ...' dla pytań wyboru lub
'1) Pytanie — Odpowiedź' dla pytań krótkiej odpowiedzi.
"""
from google.adk.agents import LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

tworca_pytan_agent = LlmAgent(
    name="TworcaPytan",
    model=GEMINI_MODEL,
    instruction="""Na podstawie podsumowania {podsumowanie} stwórz 5 pytań testowych sprawdzających
zrozumienie najważniejszych zagadnień. Każde pytanie w osobnej linii, numerowane.
Dla pytań wielokrotnego wyboru podaj opcje (A/B/C). Dla pytań otwartych podaj krótką
odpowiedź. Nie dodawaj długich wyjaśnień.
""",
    description="Generuje 5 pytań testowych z podsumowania.",
    output_key="pytania",
)
