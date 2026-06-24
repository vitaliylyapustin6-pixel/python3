import sqlite3 

conn = sqlite3.connect("bs.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE users (name TEXT,age INTEGER)")
cursor.execute("INSERT INTO users VALUES('Алексей',43)")

conn.commit()


cursor.execute("SELECT name "
                "FROM users")
print(cursor.fetchall())



conn.close()