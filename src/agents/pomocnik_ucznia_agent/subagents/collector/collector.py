"""
Zbieracz informacji o temacie nauki (agent 1).

Zadanie: zapytać ucznia, czego chce się dowiedzieć (lub temat kartkówki), doprecyzować
kilkoma prostymi pytaniami i zwrócić krótkie podsumowanie po polsku.
"""
from google.adk.agents import LlmAgent

# --- Stała modelu (można dostosować) ---
GEMINI_MODEL = "gemini-2.0-flash"

zbieracz_info_agent = LlmAgent(
    name="ZbieraczInfo",
    model=GEMINI_MODEL,
    instruction="""Jesteś pomocnikiem ucznia. pomagasz w przygotowaniu do kartkówki wyszukaj informacje i przekaz je dalej.
""",
    description="Zbiera informacje i tworzy krótkie podsumowanie dla ucznia.",
    output_key="podsumowanie",
)
