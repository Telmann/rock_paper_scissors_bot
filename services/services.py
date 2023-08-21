# Модуль с бизнес-логикой. В данном случае - это функция случайной генерации выбора бота
# и функция проверки кто победил - пользователь или бот.
import random

from lexicon.lexicon_ru import LEXICON_RU


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


def get_bot_choice_2() -> str:
    return random.choice(['rock', 'paper', 'scissors', 'lizzard', 'spok'])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'


# the same function just for the star trek game
def get_winner_2(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, set[str]] = {
        'rock': {'scissors', 'lizzard'},
        'spok': {'rock', 'scissors'},
        'scissors': {'paper', 'lizzard'},
        'paper': {'rock', 'spok'},
        'lizzard': {'spok', 'paper'}
    }

    if user_choice == bot_choice:
        return 'nobody_won'
    elif bot_choice in rules[user_choice]:
        return 'user_won'
    elif user_choice in rules[bot_choice]:
        return 'bot_won'
    #else:
        #return 'invalid_choice'
