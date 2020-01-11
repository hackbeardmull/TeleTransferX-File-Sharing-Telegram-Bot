import sqlite3

con = sqlite3.connect("bot.db")
tbname = raw_input("Table Name: ")
cat = raw_input("Dataset:")
condition = raw_input("Condition: ")
stmnt = "UPDATE " + tbname + " SET " + cat + " WHERE " + condition + ";"
with con:
    cur = con.cursor()
    cur.execute(stmnt)
con.commit()
con.close()
