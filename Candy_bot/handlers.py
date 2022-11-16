from aiogram import types, Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.set_total_candies, commands=['set_total_candies'])
    dp.register_message_handler(commands.set_max_take, commands=['set_max_take'])
    dp.register_message_handler(commands.set_difficult, commands=['set_difficult'])
    # dp.register_message_handler(commands.set_difficult, commands=['help'])
    # dp.register_message_handler(commands.player_turn)
