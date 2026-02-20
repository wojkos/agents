"""
Moduł pomocnika nauki — eksportuje agentów:
- `zbieracz_info_agent` — zbiera informacje i tworzy podsumowanie
- `tworca_fiszek_agent` — tworzy 3 fiszki do 20 słów
- `tworca_pytan_agent` — tworzy 5 pytań testowych
"""
from .colector.collector import zbieracz_info_agent
from .flashcards.flashcards import tworca_fiszek_agent
from .quiz.quiz import tworca_pytan_agent

__all__ = [
    "zbieracz_info_agent",
    "tworca_fiszek_agent",
    "tworca_pytan_agent",
]
