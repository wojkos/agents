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
    instruction="""Jesteś pomocnikiem ucznia. Najpierw zapytaj, czego chce się dowiedzieć
lub jaki jest temat najbliższej kartkówki. Zadaj do 3 krótkich pytań, aby doprecyzować
(np. poziom trudności, zakres, termin). Na końcu przygotuj krótkie podsumowanie po polsku
(maks. 60 słów).

Wyprowadź TYLKO podsumowanie jako czysty tekst (bez dodatkowych opisów).
""",
    description="Zbiera informacje i tworzy krótkie podsumowanie dla ucznia.",
    output_key="podsumowanie",
)
