import sqlite3

con = sqlite3.connect("bot.db")
cat = input("Table: ")
delid = input("ID: ")
stmnt = "delete from " + cat + " where ID = ?;"
with con:
    cur = con.cursor()
    cur.execute(stmnt,(delid))
con.commit()
con.close()
