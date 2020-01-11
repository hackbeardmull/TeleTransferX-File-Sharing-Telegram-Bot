import sqlite3

con = sqlite3.connect("bot.db")
tbname = raw_input("Table Name: ")
cat = raw_input("Column Name: ")
typed = raw_input("Data Type: ")
stmnt = "ALTER TABLE " + tbname + " ADD COLUMN " + cat + " " + typed + ";"
with con:
    cur = con.cursor()
    cur.execute(stmnt)
con.commit()
con.close()
