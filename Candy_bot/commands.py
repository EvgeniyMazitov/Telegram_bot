import asyncio
import random

import view
from create_bot import dp
from aiogram import types

import model
from create_bot import bot


async def start(message: types.Message):
    player = message.from_user
    model.set_player(player)
    await view.hello(message)
    await asyncio.sleep(3)
    dp.register_message_handler(player_turn)
    first_turn = random.randint(0, 1)
    if first_turn:
        await await_player(player)
    else:
        await enemy_turn(player)


async def player_turn(message: types.Message):
    player = message.from_user
    max_take = model.get_max_take()
    model.set_player(player)
    if (message.text).isdigit():
        if 0 < int(message.text) <= max_take:
            total_count = model.get_total_candies()
            player_take = int(message.text)
            total = total_count - player_take
            await bot.send_message(player.id, f'{player.first_name} взял {player_take} конфет, '
                                              f'и на столе осталось {total}')
            if model.check_win(total):
                await bot.send_message(player.id, f'Победил {player.first_name}')
                return
            model.set_total_candies(total)
            await enemy_turn(player)

        else:
            await bot.send_message(message.from_user.id, 'А не многовато ли взял')
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                     f'вообще-то мы конфеты считаем в цифрах')


async def enemy_turn(player):
    total_count = model.get_total_candies()
    max_take = model.get_max_take()
    difficult = model.get_difficult()
    if total_count <= max_take:
        enemy_take = total_count
    else:
        if difficult == 1:
            enemy_take = (total_count - 1) % max_take
        else:
            enemy_take = random.randint(1, max_take)
    total = total_count - enemy_take
    await bot.send_message(player.id, f'Бот взял {enemy_take} конфет, '
                                      f'и на столе осталось {total}')
    if model.check_win(total):
        await bot.send_message(player.id, f'{player.first_name} ты проиграл,'
                                          f'тебя дёрнула железяка')
        return
    model.set_total_candies(total)
    await asyncio.sleep(1)
    await await_player(player)


async def await_player(player):
    max_take = model.get_max_take()
    await bot.send_message(player.id,
                           f'{player.first_name}, бери конфеты, но не больше {max_take}')


async def set_total_candies(message: types.Message):

    count = int((message.text).split(" ")[1])
    model.set_total_candies(count)
    await bot.send_message(message.from_user.id, f'Максимально количество конфет изменили на'
                                                 f' {count}')


async def set_max_take(message: types.Message):

    count = int((message.text).split(" ")[1])
    model.set_max_take(count)
    await bot.send_message(message.from_user.id, f'Максимально количество конфет за ход изменили на'
                                                 f' {count}')


async def set_difficult(message: types.Message):

    count = int((message.text).split(" ")[1])
    model.set_difficult(count)
    await bot.send_message(message.from_user.id, f'Сложность изменили на'
                                                 f' {count}')

# async def help(message: types.Message):
#     await view.help(message)
