from aiogram import types
from create_bot import bot


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет!'
                                                 f'Сегодня будем делить конфеты')


# async def help(message: types.Message):
#     await bot.send_message(message.from_user.id, f'Доступные команды /n /start - начать игру /n /set - Настройки /n /help - доступные команды')

# async def help_set(message: types.Message):
#     await bot.send_message(message.from_user.id, f'Доступные команды /n /set_total_candies - установить общее число конфет /n /set_max_take - установить максимальное число конфет за 1 ход /n /set_difficult - выбрать уровень сложности')