# модуль с обработчиками апдейтов от пользователя, предусмотренных логикой бота
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb, first_second_kb, game_kb_startrek
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_bot_choice_2, get_winner, get_winner_2

router: Router = Router()

users: dict = {}


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)
    # Если пользователь только запустил бота и его нет в словаре '
    # 'users - добавляем его в словарь
    if message.from_user.id not in users:
        users[message.from_user.id] = {'total_games': 0,
                                       'wins': 0}
        user_id = message.from_user.id


def us_id():
    global user_id
    users[user_id]["wins"] += 1


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=first_second_kb)
    # users[message.from_user.id]['total_games'] += 1


@router.message(F.text == LEXICON_RU['first_game'])
async def process_first_game_choice(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

    @router.message(F.text.in_([LEXICON_RU['rock'],
                                LEXICON_RU['paper'],
                                LEXICON_RU['scissors']]))
    async def process_game_button(message: Message):
        bot_choice = get_bot_choice()
        await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                                  f'- {LEXICON_RU[bot_choice]}')
        winner = get_winner(message.text, bot_choice)
        await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_RU['second_game'])
async def process_first_game_choice(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb_startrek)

    @router.message(F.text.in_([LEXICON_RU['rock'],
                                LEXICON_RU['paper'],
                                LEXICON_RU['scissors'],
                                LEXICON_RU['lizzard'],
                                LEXICON_RU['spok']]))
    async def process_game_button_2(message: Message):
        bot_choice = get_bot_choice_2()
        await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                                  f'- {LEXICON_RU[bot_choice]}')
        winner = get_winner_2(message.text, bot_choice)
        await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


# Этот хэндлер срабатывает на любую из игровых кнопок


# Этот хэндлер будет срабатывать на команду "/stat"
@router.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(
        f'Всего игр сыграно: '
        f'{users[message.from_user.id]["total_games"]}\n'
        f'Игр выиграно: {users[message.from_user.id]["wins"]}')
