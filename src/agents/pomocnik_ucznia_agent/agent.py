"""
Pomocnik nauki — sekwencyjny agent łączący trzy sub-agenty.

Ten plik dostosowuje przykład z innego folderu do obecnego modułu `study_helper`.
Sekwencja:
1. `zbieracz_info_agent` — zbiera informacje i tworzy krótkie podsumowanie
2. `tworca_fiszek_agent` — na podstawie podsumowania tworzy 3 fiszki
3. `tworca_pytan_agent` — na podstawie podsumowania tworzy 5 pytań testowych

Uwaga: agenty są zadeklarowane w oddzielnych plikach i używają polskich
instrukcji oraz kluczy wyjściowych.
"""

from google.adk.agents import SequentialAgent

from .subagents.collector import zbieracz_info_agent
from .subagents.flashcards import tworca_fiszek_agent
from .subagents.quiz import tworca_pytan_agent


# Tworzymy sekwencyjnego agenta, który uruchamia naszych trzech pomocniczych agentów
root_agent = SequentialAgent(
    name="pomocnik_nauki_pipeline",
    sub_agents=[zbieracz_info_agent, tworca_fiszek_agent, tworca_pytan_agent],
    description=(
        "Sekwencyjny pipeline: zbiera informacje o temacie, tworzy 3 fiszki "
        "i 5 pytań testowych (instrukcje i opisy po polsku)."
    ),
)

