import os
import asyncio
import logging
from aiogram import Dispatcher, Bot
from commands import register_user_commands, bot_commands
from aiogram.types import BotCommand
from db import BaseModel, create_async__engine, proceed_schemas, get_session_maker, User
from sqlalchemy.engine import URL


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    dp = Dispatcher()
    bot = Bot(token=os.getenv('token'))
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    postgres_url = URL.create('postgresql+asyncpg')

    async_engine = create_async__engine()
    session_maker = get_session_maker(async_engine)
    with session_maker() as session:
        proceed_schemas(session, BaseModel.metadata)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
