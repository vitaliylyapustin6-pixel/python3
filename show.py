import sqlite3
conn = sqlite3.connect("b.db")
cur = conn.cursor()
cur.execute("INSERT INTO boook(name)VALUES('bb')")
cur.execute("SELECT name FROM boook")
print(cur.fetchall())
conn.close()
