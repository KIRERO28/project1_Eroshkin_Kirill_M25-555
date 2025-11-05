# labyrinth_game/player_actions.py
"""
Функции, отвечающие за действия игрока.
"""
from typing import Any

from .constants import ROOMS
from .utils import normalize_direction


def move_player(state: dict[str, Any], direction: str) -> str:
    """Пробует переместить игрока в указанном направлении."""
    direction = normalize_direction(direction)
    current_room = state["current_room"]

    if direction in ROOMS[current_room]["exits"]:
        next_room = ROOMS[current_room]["exits"][direction]
        state["current_room"] = next_room
        state["steps_taken"] += 1
        return f"Вы переместились в комнат
у: {next_room}"
    return "Нельзя идти туда."


def take_item(state: dict[str, Any], item: str) -> str:
    """Поднять предмет из текущей комнаты."""
    room = ROOMS[state["current_room"]]
    if item in room["items"]:
        room["items"].remove(item)
        state["player_inventory"].append(item)
        return f"Вы подобрали {item}."
    return "Здесь нет такого предмета."


def solve_puzzle(state: dict[str, Any], answer: str) -> str:
    """Проверить ответ игрока на загадку."""
    room = ROOMS[state["current_room"]]
    if room["puzzle"] is None:
        return "В этой комнате нет загадок."

    question, correct_answer = room["puzzle"]
    if answer.strip().lower() == correct_answer.strip().lower():
        room["puzzle"] = None  # Считаем загадку решённой
        return "Загадка решена!"
    return "Неверный ответ."

