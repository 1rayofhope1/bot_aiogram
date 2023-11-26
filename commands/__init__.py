from commands.start import start
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.filters import Command
from commands.help import help, help_func, call_help_func
from aiogram import F
from commands.settings import settings
__all__ = ['register_user_commands', 'bot_commands']

bot_commands = (('start', 'начать работу', 'запускаем нашего бота и начинаем работу'),
                ('help', 'помощь и справка', 'полное описание работы и функционала телеграм-бота'))


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help, Command(commands=['help']))
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(settings, Command(commands=['settings']))
    router.callback_query.register(call_help_func, F.data == 'help')
