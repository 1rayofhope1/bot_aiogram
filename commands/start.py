from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButtonPollType


async def start(message: types.Message) -> None:
    menu_bilder = ReplyKeyboardBuilder()
    menu_bilder.button(text='Помощь')
    menu_bilder.add(types.KeyboardButton(
        text='Отправить контакт', request_contact=True))
    menu_bilder.row(types.KeyboardButton(
        text='Отправить голосование', request_poll=KeyboardButtonPollType()))

    await message.answer('Привет', reply_markup=menu_bilder.as_markup(resize_keyboard=True))
