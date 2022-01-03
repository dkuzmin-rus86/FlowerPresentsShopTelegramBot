"""Сервер Telegram бота """
import logging
import sqlite3
from aiogram import executor
from telegram_bot import dp
from handlers import client, admin, other
from database import db


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

client.register_handlers_client(dp)
admin.register_handlers_client(dp)

async def on_startup(_):
    print('Бот в онлайне')
    db.sql_start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
