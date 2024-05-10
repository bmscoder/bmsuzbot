import sqlite3

# Ma'lumotlar bazasini ochish
db = sqlite3.connect('bmsuzbot.db')
# Kursor ochish
cur = db.cursor()

# Ma'lumotlar bazasida "users" jadvalini tuzish
async def create_table_users():
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        status VARCHAR(30),
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    # O'zgarishlarni ma'lumotlar bazasiga saqlash
    db.commit()
