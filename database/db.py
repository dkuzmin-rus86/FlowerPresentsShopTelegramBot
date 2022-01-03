import sqlite3
from telegram_bot import bot


def sql_start():
    global conn, cursor
    conn = sqlite3.connect('flower.db')
    cursor = conn.cursor()
    if conn:
        print('Database connect OK!')
    conn.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    conn.commit


async def sql_add_command(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        conn.commit()


async def sql_read(message):
    for ret in cursor.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}')