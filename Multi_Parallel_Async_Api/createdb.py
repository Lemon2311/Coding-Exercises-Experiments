import sqlite3

con = sqlite3.connect('mydatabase.db')

cur = con.cursor()

table_name = "users"

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

res = cur.fetchall()

if (table_name,) not in res:
    cur.execute(f"CREATE TABLE {table_name} (name)")
    print("Table created")
else:
    print("Table already exists")

