from aiogram import types
from aiogram.filters import CommandObject
from commands.bot_commands import bot_commands


async def help(message: types.Message, command: CommandObject) -> None:
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
                )
        else:
            return message.answer('Команда не найдена')
    return message.answer('Помощь и справка о боте\n'
                          'Для информации о команде, напишите /help <команда>')


async def help_func(message: types.Message):
    return message.answer('Помощь и справка о боте\n'
                          'Для информации о команде, напишите /help <команда>')


async def call_help_func(call: types.CallbackQuery):
    return call.message.edit_text('Помощь и справка о боте\n'
                                  'Для информации о команде, напишите /help <команда>',
                                  reply_markup=call.message.reply_markup)
