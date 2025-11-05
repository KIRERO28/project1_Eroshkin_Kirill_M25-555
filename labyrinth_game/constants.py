# labyrinth_game/constants.py
"""
Константы и неизменяемые данные игры.
"""

ROOMS: dict[str, dict] = {
    "entrance": {
        "description": (
            "Вы в темном входе лабиринта. Стены покрыты мхом. "
            "На полу лежит старый факел."
        ),
        "exits": {"north": "hall", "east": "trap_room"},
        "items": ["torch"],
        "puzzle": None,
    },
    "hall": {
        "description": (
            "Большой зал с эхом. По центру стоит пьедестал "
            "с запечатанным сундуком."
        ),
        "exits": {
            "south": "entrance",
            "west": "library",
            "north": "treasure_room",
        },
        "items": [],
        "puzzle": (
            'На пьедестале надпись: "Назовите число, которое идет после девяти".',
            "10",
        ),
    },
    "trap_room": {
        "description": (
            "Комната с хитрой плиточной поломкой. "
            'На стене видна надпись: "Осторожно — ловушка".'
        ),
        "exits": {"west": "entrance"},
        "items": ["rusty_key"],
        "puzzle": (
            'Система плит активна. Чтобы пройти, введите "шаг шаг шаг".',
            "шаг шаг шаг",
        ),
    },
    "library": {
        "description": (
            "Пыльная библиотека. На полках старые свитки. "
            "Где-то здесь может быть ключ от сокровищницы."
        ),
        "exits": {"east": "hall", "north": "armory"},
        "items": ["ancient_book"],
        "puzzle": (
            'Загадка: "Что растет, когда его съедают?"',
            "резонанс",
        ),
    },
    "armory": {
        "description": (
            "Старая оружейная. На стене висит меч, рядом — бронзовая шкатулка."
        ),
        "exits": {"south": "library"},
        "items": ["sword", "bronze_box"],
        "puzzle": None,
    },
    "treasure_room": {
        "description": "Запертая комната с большим сундуком.",
        "exits": {"south": "hall"},
        "items": ["treasure_chest"],
        "puzzle": (
            "Дверь защищена кодом. Подсказка: 2*5 = ?",
            "10",
        ),
    },
    # Дополнительные комнаты
    "garden": {
        "description": (
            "Подземный сад с биолюминесцентными растениями. "
            "Слышно журчание воды."
        ),
        "exits": {"west": "armory"},
        "items": ["glowing_fern"],
        "puzzle": None,
    },
    "river_cave": {
        "description": (
            "Пещера с подземной рекой. Мост сломан, но рядом лодка."
        ),
        "exits": {"east": "armory"},
        "items": ["boat"],
        "puzzle": (
            'Надпись: "Я всегда в движении, но никогда не ухожу". Что это?',
            "река",
        ),
    },
}
