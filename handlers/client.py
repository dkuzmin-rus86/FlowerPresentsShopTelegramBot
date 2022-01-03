from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from telegram_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from database import db


async def shop_welcome_command(message: types.Message):
    """Приветственное сообщение бота"""
    try:
        await bot.send_message(
            message.from_user.id,
            "Привет! Я бот управления цветочным магазином",
            reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС:\nhttps://t.me/FlowerPresentsBot')


async def shop_info_command(message: types.Message):
    """ Отправляет информацию об адресе и режиме работы магазина """
    answer_message = "г. Югорск, ул Ленина 2\n\n"\
                     "ПН-ВС с 8:00 до 20:00"
    await bot.send_message(
            message.from_user.id,
            answer_message)


async def shop_menu_command(message: types.Message):
    await db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(shop_welcome_command, commands=['start', 'help'])
    dp.register_message_handler(shop_info_command, commands=['Информация'])
    dp.register_message_handler(shop_menu_command, commands=['Меню'])
