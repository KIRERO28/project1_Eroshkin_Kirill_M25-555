# labyrinth_game/utils.py
"""
Вспомогательные функции, не относящиеся напрямую к логике игрока.
"""


def normalize_direction(direction: str) -> str:
    """Приводит направление к нижнему регистру и убирает пробелы."""
    return direction.strip().lower()
