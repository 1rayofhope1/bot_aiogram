from commands.start import start
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.filters import Command
from commands.help import help

__all__ = ['register_user_commands', 'bot_commands']

bot_commands = (('start', 'начать работу', 'запускаем нашего бота и начинаем работу'),
                ('help', 'помощь и справка', 'полное описание работы и функционала телеграм-бота'))


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help, Command(commands=['help']))
