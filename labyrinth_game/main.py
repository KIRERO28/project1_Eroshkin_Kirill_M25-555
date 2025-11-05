# main.py
"""
Точка входа в игру «Labyrinth».
"""
from typing import Any

from labyrinth_game.constants import ROOMS
from labyrinth_game.player_actions import move_player, solve_puzzle, take_item

# Состояние игры
game_state: dict[str, Any] = {
    "player_inventory": [],
    "current_room": "entrance",
    "game_over": False,
    "steps_taken": 0,
}


def show_room(room_key: str) -> None:
    """Печатает описание комнаты."""
    room = ROOMS[room_key]
    print("\n" + room["description"])
    if room["items"]:
        print(f"Вы видите предметы: {', '.join(room['items'])}")
    exits = ", ".join(room["exits"].keys())
    print(f"Выходы: {exits}")
    if room["puzzle"]:
        print(room["puzzle"][0])  # выводим вопрос


def game_loop() -> None:
    """Простой игровой цикл."""
    while not game_state["game_over"]:
        show_room(game_state["current_room"])
        command = input("\n> ").strip().lower()

        if command in {"quit", "exit"}:
            game_state["game_over"] = True
            print("Вы вышли из игры.")
            continue

        if command.startswith("go "):
            direction = command.removeprefix("go ")
            print(move_player(game_state, direction))
            continue

        if command.startswith("take "):
            item = command.removeprefix("take ")
            print(take_item(game_state, item))
            continue

        if command.startswith("answer "):
            answer = command.removeprefix("answer ")
            print(solve_puzzle(game_state, answer))
            continue

        print("Неизвестная команда.")


if __name__ == "__main__":
    game_loop()
