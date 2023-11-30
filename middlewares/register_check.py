from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db import User
from sqlalchemy.engine import ScalarResult
from typing import Union
from aiogram.types import CallbackQuery


class RegisterCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        session_maker: sessionmaker = data['session_maker']
        async with session_maker() as session:
            async with session.begin():
                session: AsyncSession
                result = await session.execute(select(User).where(User.id == event.from_user.id))
                result: ScalarResult
                user: User = result.one_of_none()
                if user is not None:
                    pass
                else:
                    user = User(user_id=event.from_user.id,
                                username=event.from_user.username)
                    await session.merge(user)
                    if isinstance(event, Message):
                        await event.answer('ты успешно зарегистрирован')
                    else:
                        await event.message.answer('ты успешно зарегистрирован')
        return await handler(event, data)
