from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton(text='/Информация')
b2 = KeyboardButton(text='/Меню')
# b3 = KeyboardButton(text='Поделиться номером', request_contact=True)
# b4 = KeyboardButton(text='Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2)
