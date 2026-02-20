"""
Twórca fiszek (agent 2).

Zadanie: na podstawie 'podsumowanie' stworzyć dokładnie 3 fiszki, każda maksymalnie 20 słów.
Format wyjścia: każda fiszka w osobnej linii, numerowana, dokładnie tak:
"1) Pytanie — Odpowiedź". Nie dodawać nic poza trzema liniami z fiszkami.
"""
from google.adk.agents import LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

tworca_fiszek_agent = LlmAgent(
    name="TworcaFiszki",
    model=GEMINI_MODEL,
    instruction="""Na podstawie otrzymanego podsumowania przygotuj dokładnie 3 fiszki.
Każda fiszka ma mieć maksymalnie 20 słów. Format wyjścia: każda fiszka w osobnej linii,
numerowana, dokładnie tak: '1) Pytanie — Odpowiedź'. Nie dodawaj nic poza trzema liniami
z fiszkami. Użyj prostego języka zrozumiałego dla ucznia 7. klasy.
""",
    description="Tworzy 3 fiszki (do 20 słów każda).",
    output_key="fiszki",
)
