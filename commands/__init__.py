from commands.start import start
from aiogram.filters import CommandStart
from aiogram import Router
__all__ = ['register_user_commands']


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
