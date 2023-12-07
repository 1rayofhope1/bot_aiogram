import os
import asyncio
import logging
from sqlalchemy.ext.asyncio import AsyncEngine
from aiogram import Dispatcher, Bot
from commands import register_user_commands, bot_commands
from aiogram.types import BotCommand
from db import BaseModel, create_async_engine, proceed_schemas, get_session_maker, User
from sqlalchemy.engine import URL
from middlewares.register_check import RegisterCheck


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    dp = Dispatcher()
    dp.message.middleware(RegisterCheck)
    dp.callback_query.middleware(RegisterCheck)

    # Запуск бота
    bot = Bot(token=os.getenv('token'))
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    postgres_url = URL.create('postgresql+asyncpg',
                              username=os.getenv('db_user'),
                              password=os.getenv('db_password'),
                              port=os.getenv('db_port'),
                              host=os.getenv('db_host'),
                              database=os.getenv('db_name'))

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    #Делегировано алембику
    #await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot, session_maker=session_maker)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
