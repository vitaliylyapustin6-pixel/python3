import sqlite3

conn = sqlite3.connect("bbv.db")
cursor = conn.cursor()

# Создаем таблицу и добавляем данные
cursor.execute("""CREATE TABLE IF NOT EXISTS users (name TEXT)""")
cursor.execute("INSERT INTO users(name) VALUES('bober')")

# ОБЯЗАТЕЛЬНО: выполняем SELECT, чтобы забрать данные
cursor.execute("SELECT * FROM users")
b = cursor.fetchall()

print(b)  # Выведет: [('bober',)]

conn.commit()
conn.close()
