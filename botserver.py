from pyrogram import Client
from pyrogram import Filters, MessageHandler
import sqlite3
result = None
api_id = 
api_hash = ""

#with Client("my_account", api_id, api_hash) as app:
#    app.send_message("teletransferxgroup", "Greetings from an CLIENT **BOT**!")
#@app.on_message(Filters.document)
#def my_handler(client, message):
#    print(messag

#from pyrogram import Client

app = Client("my_account", api_id, api_hash)
def download(message):
	message.download(block=True)
	file = message.download(block=True)
	global result
	result = 1
	return file

#@app.on_message()
#def my_handler(client, message):
#    print("Get Message")

@app.on_message(Filters.video)
def my_handler(client, message):
   file = download(message)
   while result is None:
     print("None")
     pass
   if result > 0:
     path = str(file)
     path = path.replace("./static/", "")
     movietitle = str(file)
     movietitle = movietitle[:-4]
     movietitle = movietitle.replace("./static/downloads/", "")
     con = sqlite3.connect("vid.db")
     with con:
       cursor = con.cursor()
       cursor.execute("INSERT INTO mp4 (ID, NAME, PATH) VALUES (NULL, ?, ?)",(movietitle, path))
   con.commit()
   con.close()
app.run()
