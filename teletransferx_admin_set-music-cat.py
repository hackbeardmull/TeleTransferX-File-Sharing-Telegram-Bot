import sqlite3

con = sqlite3.connect("bot.db")
cat = raw_input("Interpret:")
condition = raw_input("Categorie:")
stmnt = "UPDATE music SET categorie = '" + condition + "' where upper(ARTIST) GLOB upper('" + cat + "');"
with con:
    cur = con.cursor()
    cur.execute(stmnt)
con.commit()
con.close()
