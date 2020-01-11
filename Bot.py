# -*- coding: utf-8 -*-
from telegram import Bot, MessageEntity, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
						  Dispatcher, CallbackQueryHandler, RegexHandler)
import logging
import random
import requests
import time
import json, re
import telegram
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from tinytag import TinyTag
import sqlite3
import zipfile
from lxml import etree
import sys
import magic
import os 
import eyed3
import eyed3.id3
import tagpy
import urllib
import subprocess
#reload(sys)
#sys.setdefaultencoding('utf8')
URL = "https://api.telegram.org/bot{}/".format('<your bot id>')
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update, args):
    bot.send_message(update.message.chat_id, 
                 text='<b>TeleTransferX</b> \n <i>Version 2.0 </i> \n (C) 2019 TeleTransferX Team.\n All rights reserved.\n For Support: https://t.me/teletransferxgroup \n For Help /help \n Kodi User ? Try Ghost Repo http://ghost-repo.de ', 
                 parse_mode=telegram.ParseMode.HTML)
    buffer = '' + ' '.join(str(e) for e in args)
    print(buffer)
    if buffer:
      massids = ''.join(buffer) 
      massids = massids[6:]
      massids = massids.split("-")
      buffer = buffer.split("-")
      print(buffer[0])
      if buffer[0] == "music":
        if len(massids) > 0:
          con = sqlite3.connect("bot.db")
          cur = con.cursor()
          with con:
            for items in massids:
              cur = con.cursor()
              cur.execute("SELECT PATH FROM music WHERE ID = ?;",(items,))
              rows = cur.fetchall()
              fpath = ''.join(str(rows))
              fpath = fpath.replace("[(u'", "")
              fpath = fpath.replace("',)]", "")
              bot.send_document(update.message.chat_id, document=open(fpath, 'rb'))
          con.close()
        else:
          con = sqlite3.connect("bot.db")
          cur = con.cursor()
          with con:
            cur = con.cursor()
            cur.execute("SELECT PATH FROM music WHERE ID = ?;",(buffer[1],))
            rows = cur.fetchall()
            fpath = ''.join(str(rows))
            fpath = fpath.replace("[(u'", "")
            fpath = fpath.replace("',)]", "")
          con.close()
          bot.send_document(update.message.chat_id, document=open(fpath, 'rb'))
      elif buffer[0] == "books":
        if len(massids) > 0:
          con = sqlite3.connect("bot.db")
          cur = con.cursor()
          with con:
            for items in massids:
              cur = con.cursor()
              cur.execute("SELECT path FROM books WHERE id = ?;",(items,))
              rows = cur.fetchall()
              fpath = ''.join(str(rows))
              fpath = fpath.replace("[(u'", "")
              fpath = fpath.replace("',)]", "")
              bot.send_document(update.message.chat_id, document=open(fpath, 'rb'))
          con.close()
        else:
          con = sqlite3.connect("bot.db")
          cur = con.cursor()
          with con:
            cur = con.cursor()
            cur.execute("SELECT path FROM books WHERE id = ?;", (buffer[1],))
            rows = cur.fetchall()
            fpath = ''.join(str(rows))
            fpath = fpath.replace("[(u'", "")
            fpath = fpath.replace("',)]", "")
          con.close()
          bot.send_document(update.message.chat_id, document=open(fpath, 'rb'))
      elif buffer[0] == "file":
        con = sqlite3.connect("bot.db")
        cur = con.cursor()
        with con:
          cur = con.cursor()
          cur.execute("SELECT FILEID FROM files WHERE ID = ?;", (buffer[1],))
          rows = cur.fetchall()
          fpath = ''.join(str(rows))
          fpath = fpath.replace("[(u'", "")
          fpath = fpath.replace("',)]", "")
        con.close()
        bot.send_document(update.message.chat_id, document=fpath)


def helper(bot, update):
  helper = '<b> HELP </b> \n /searchmusicartist - Search for music of an artist (searchpattern)  \n /searchmusictitle - Search for music title (searchpattern) \n /streammusic - Stream music (File UID, random) \n /downloadmusic - Download music (File UID) \n /searchbookauthor - Search books of author (searchpattern) \n /searchbooktitle - Search book by title (searchpattern) \n /downloadbook - Download book (File UID) \n /searchflac - Search for music title -flac- (searchpattern) \n /streamflac - Stream  music title flac (Title ID) \n /countdbflac - Count flac DB \n /version - Show bot version and copyright'
  bot.send_message(update.message.chat_id, 
                 text=helper, 
                 parse_mode=telegram.ParseMode.HTML)

def version(bot, update):
		bot.send_message(update.message.chat_id, 
                 text='<b>TeleTransferX</b> \n <i>Version 1.1 "M4A1"</i> \n (C) 2019 TeleTransferX Team. \n ', 
                 parse_mode=telegram.ParseMode.HTML)
                 
def chatid(bot, update):
		chatid = update.message.chat_id
		chatid = str(chatid)
		message = "<b>CHAT ID INFORMATION</b> \n Your CHAT ID is: " + chatid
		bot.send_message(update.message.chat_id, 
                 text=message, 
                 parse_mode=telegram.ParseMode.HTML)
                 
                               

def tstfile(bot, update):
	
	bot.send_photo(update.message.chat_id, document=open('test/1.jpg', 'rb'))

def gvu(bot, update):
	bot.send_photo(update.message.chat_id, photo=open('botpic/gvu.jpg', 'rb'))
	
def ddos(bot, update):
	bot.send_photo(update.message.chat_id, photo=open('botpic/ddos.jpg', 'rb'))
	
def gema(bot, update):
	bot.send_photo(update.message.chat_id, photo=open('botpic/gema.jpg', 'rb'))
	
def riaa(bot, update):
	bot.send_photo(update.message.chat_id, photo=open('botpic/riaa.jpg', 'rb'))

def echo(bot, update):
    """Echo the user message."""

def searchbooktitle(bot, update, args):
		userid = update.message.chat_id
		userid = str(userid)
		print(userid)
		print("test")
		conu = sqlite3.connect("/userlog.db")
		curu = conu.cursor()
		with conu:
			#curu = conu.cursor()
			curu.execute("SELECT userid FROM users WHERE userid = ?;",(userid,))
			rowus = curu.fetchall()
		useridbuffer = str(rowus)
		useridbuffer = useridbuffer.replace("[(", "")
		useridbuffer = useridbuffer.replace(",)]", "")
		useridbuffer = useridbuffer.replace("u'", "")
		useridbuffer = useridbuffer.replace("'", "")
		conu.close()
		print(useridbuffer)
		if useridbuffer == userid:
			con = sqlite3.connect("bot.db")
			cur = con.cursor()
			with con:
				buffer = '' + ' '.join(str(e) for e in args)
				buffer = "*" + safeStr(buffer) + "*"
				cur = con.cursor()
				cur.execute("SELECT * FROM books WHERE upper(TITLE) GLOB upper(?);",(buffer,))
				rows = cur.fetchall()
				countm = 1
				bookbuffer = ""
				for row in rows:
					if countm < 22:
						 bookbuffer = bookbuffer + "\n <b> FILE-ID: " + str(row) + "\n </b>"
						 bookbuffer = bookbuffer.replace("(", " ")
						 bookbuffer = bookbuffer.replace("u'", " ")
						 bookbuffer = bookbuffer.replace('u"', '' )
						 bookbuffer = bookbuffer.replace(")'", " ")
						 bookbuffer = bookbuffer.replace("',", " ")
						 countm +=1
					if countm == 22:
						 bot.send_message(update.message.chat_id, 
               text=bookbuffer, 
               parse_mode=telegram.ParseMode.HTML)
						 bookbuffer = ""
						 countm = 1
				
				con.close()
				bot.send_message(update.message.chat_id, 
                    text=bookbuffer, 
                   parse_mode=telegram.ParseMode.HTML)
		elif useridbuffer != userid :
			bot.send_message(update.message.chat_id, 
                  text=" You need an Account to use TeleTransferX.\n Register an Account with your Chat ID on teletransferx.com\n Send /chatid to get your Chat ID", 
                  parse_mode=telegram.ParseMode.HTML)
		
def searchmovie(bot, update, args):
		con = sqlite3.connect("bot.db")
		cur = con.cursor()
		buffer = '' + ' '.join(str(e) for e in args)
		buffer = "*" + safeStr(buffer) + "*"	
		cur = con.cursor()
		cur.execute("SELECT * FROM videos WHERE upper(TITLE) GLOB upper(?);",(buffer,))
		rows = cur.fetchall()
		countm = 1
		videobuffer = ""
		for row in rows:
			if countm < 22:
					videobuffer = videobuffer + "\n <b> FILE-ID: " + str(row) + "\n </b>"
					videobuffer = videobuffer.replace("(", " ")
					videobuffer = videobuffer.replace("u'", " ")
					videobuffer = videobuffer.replace('u"', '' )
					videobuffer = videobuffer.replace(")'", " ")
					videobuffer = videobuffer.replace("',", " ")
					countm +=1
			if countm == 22:
				bot.send_message(update.message.chat_id, 
				text=videobuffer, 
				parse_mode=telegram.ParseMode.HTML)
				videobuffer = ""
				countm = 1
		con.close()
		bot.send_message(update.message.chat_id, 
                 text=videobuffer, 
                 parse_mode=telegram.ParseMode.HTML)
		
		
		
		
		

def searchauthor(bot, update, args):
		con = sqlite3.connect("bot.db")
		cur = con.cursor()
		buffer = '' + ' '.join(str(e) for e in args)
		buffer = "*" + safeStr(buffer) + "*"
		print(buffer)
		authorbuffer = ""
		with con:
			cur = con.cursor()
			cur.execute("SELECT * FROM books WHERE upper(AUTHOR) GLOB upper(?);",(buffer,))
			rows = cur.fetchall()
			countm = 1
			for row in rows:
				if countm < 22:
					authorbuffer = authorbuffer + "\n <b> FILE-ID: " + str(row) + "\n </b>"
					authorbuffer = authorbuffer.replace("(", " ")
					authorbuffer = authorbuffer.replace("u'", " ")
					authorbuffer = authorbuffer.replace('u"', '' )
					authorbuffer = authorbuffer.replace(")'", " ")
					authorbuffer = authorbuffer.replace("',", " ")
					countm +=1
				if countm == 22:
					bot.send_message(update.message.chat_id, 
                 text=authorbuffer, 
                 parse_mode=telegram.ParseMode.HTML)
					authorbuffer = ""
					countm = 1
		con.close()
		bot.send_message(update.message.chat_id, 
                 text=authorbuffer, 
                 parse_mode=telegram.ParseMode.HTML)

def download(bot, update, args):
		userid = update.message.chat_id
		userid = str(userid)
		print(userid)
		print("test")
		conu = sqlite3.connect("/userlog.db")
		curu = conu.cursor()
		with conu:
			#curu = conu.cursor()
			curu.execute("SELECT userid FROM users WHERE userid = ?;",(userid,))
			rowus = curu.fetchall()
		useridbuffer = str(rowus)
		useridbuffer = useridbuffer.replace("[(", "")
		useridbuffer = useridbuffer.replace(",)]", "")
		useridbuffer = useridbuffer.replace("u'", "")
		useridbuffer = useridbuffer.replace("'", "")
		conu.close()
		print(useridbuffer)
		if useridbuffer == userid:
			userid = update.message.chat_id
			userid = str(userid)
			print(userid)
			print("test")
			conu = sqlite3.connect("/userlog.db")
			curu = conu.cursor()
			with conu:
			#curu = conu.cursor()
				curu.execute("SELECT premium FROM users WHERE userid = ?;",(userid,))
				rowus = curu.fetchall()
			premiumbuffer = str(rowus)
			premiumbuffer = premiumbuffer.replace("[(", "")
			premiumbuffer = premiumbuffer.replace(",)]", "")
			premiumbuffer = premiumbuffer.replace("u'", "")
			premiumbuffer = premiumbuffer.replace("'", "")
			conu.close()
			print(premiumbuffer)
			if premiumbuffer == 'premium':
				con = sqlite3.connect("bot.db")
				cur = con.cursor()
				buffer = '' + ' '.join(str(e) for e in args)
				print(buffer)
				with con:
					cur = con.cursor()
					cur.execute("SELECT PATH FROM books WHERE ID = ?;",(buffer,))
					rows = cur.fetchall()
					fpath = ''.join(str(rows))
					fpath = fpath.replace("[(u'", "")
					fpath = fpath.replace("',)]", "")
				con.close()	
				bot.send_document(update.message.chat_id, document=open(fpath, 'rb'))
				print("## Downloaded ->"+ fpath)
			else:
				bot.send_message(update.message.chat_id, 
                  text="You need an Premium account to download or stream.\nGet Premium on teletransferx.com\nFree unlimited Music Streaming and unlimited File Downloads: https://t.me/Music_Streaming", 
                  parse_mode=telegram.ParseMode.HTML)
		else:
			bot.send_message(update.message.chat_id, 
                  text=" You need an Account to use TeleTransferX.\n Register an Account with your Chat ID on teletransferx.com\n Send /chatid to get your Chat ID", 
                  parse_mode=telegram.ParseMode.HTML)	

def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def file_handler(bot, update):
  #file = bot.getFile(update.message.document.file_id)
  rande = random.randint(1,999999)
  #fpathbuffer = "buffer/" + str(rande) + str(update.message.document.file_name)
  #fpathbuffer = fpathbuffer.replace(" ", "")
  #file.download(fpathbuffer)
  #mime = magic.Magic(mime=True)
  #filetype = mime.from_file(fpathbuffer)
  #print(filetype)
  filetype = str(update.message.document.mime_type)
  print("File Handler: " + filetype)
  if filetype == "application/epub+zip":
    file = bot.getFile(update.message.document.file_id)
    fpathbuffer = "books/" + str(rande) + str(update.message.document.file_name)
    fpathbuffer = fpathbuffer.replace(" ", "")
    file.download(fpathbuffer)
    ns = {'n':'urn:oasis:names:tc:opendocument:xmlns:container','pkg':'http://www.idpf.org/2007/opf','dc':'http://purl.org/dc/elements/1.1/'}
    zip = zipfile.ZipFile(fpathbuffer)
    txt = zip.read('META-INF/container.xml')
    tree = etree.fromstring(txt)
    cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path',namespaces=ns)[0]
    cf = zip.read(cfname)
    tree = etree.fromstring(cf)
    p = tree.xpath('/pkg:package/pkg:metadata',namespaces=ns)[0]
    res = {}
    for s in ['title','creator','date']:
      res[s] = p.xpath('dc:%s/text()'%(s),namespaces=ns)[0]
    print(res['creator'])
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    titles = safeStr(res['title'])
    titles = titles.encode('utf-8')
    creator = safeStr(res['creator'])
    creator = creator.encode('utf-8')
    tdate = safeStr(res['date'])
    tdate = tdate.encode('utf-8')
    cursor.execute("INSERT INTO books (id, title, author, year, filetype, path) VALUES (NULL, ?, ?, ?, 'epub', ?)",(titles, creator, tdate, fpathbuffer))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + titles + " from " + creator)
    
  elif filetype == "video/x-matroska":
    fileid = safeStr(str(update.message.document.file_id))
    movietitle =str(update.message.document.file_name)
    movietitle = movietitle[:-4]
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO videos (ID, TITLE, FILEID, FILETYPE) VALUES (NULL, ?, ?, ?)",(movietitle, fileid, filetype))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + movietitle)
        
  elif filetype == "video/x-msvideo":
    fileid = safeStr(str(update.message.document.file_id))
    movietitle =str(update.message.document.file_name)
    movietitle = movietitle[:-4]
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO videos (ID, TITLE, FILEID, FILETYPE) VALUES (NULL, ?, ?, ?)",(movietitle, fileid, filetype))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + movietitle)
    
  elif filetype == "video/quicktime":
    fileid = safeStr(str(update.message.document.file_id))
    movietitle =str(update.message.document.file_name)
    movietitle = movietitle[:-4]
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO videos (ID, TITLE, FILEID, FILETYPE) VALUES (NULL, ?, ?, ?)",(movietitle, fileid, filetype))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + movietitle)

  elif filetype == "video/x-ms-wmv":
    fileid = safeStr(str(update.message.document.file_id))
    movietitle =str(update.message.document.file_name)
    movietitle = movietitle[:-4]
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO videos (ID, TITLE, FILEID, FILETYPE) VALUES (NULL, ?, ?, ?)",(movietitle, fileid, filetype))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + movietitle)    
  elif filetype == "audio/x-flac":
    fileid = safeStr(str(update.message.audio.file_id))
    musictitle = str(update.message.audio.file_name)
    musictitle = musictitle[:-5]
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO flac (id, title, fileid) VALUES (NULL, ?, ?)",(musictitle, fileid))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + musictitle)
  else:
    fpathbuffer = "files/" + str(rande) + str(update.message.document.file_name)
    print(str(update.message.document.file_id))
    name =str(update.message.document.file_name)
    fileid = str(update.message.document.file_id)
    fileid = safeStr(fileid)
    print(fileid)
    name = name[:-4]
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO files (ID, NAME, FILEID, FILETYPE) VALUES (NULL, ?, ?, ?)",(name, fileid, filetype))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + name)
   
def audio_handler(bot, update):
  audiomime = str(update.message.audio.mime_type)
  print("Audio Handler: " + audiomime)
  if audiomime == "audio/flac":
    fileid = safeStr(str(update.message.audio.file_id))
    musictitle = safeStr(str(update.message.audio.title))
    artist = safeStr(str(update.message.audio.performer))
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO flac (id, title, artist, fileid) VALUES (NULL, ?, ?, ?)",(musictitle, artist, fileid))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + musictitle)
  file = bot.getFile(update.message.audio.file_id)
  rande = random.randint(15,50)
  fpathbuffer = "music/" + str(rande) + str(update.message.audio.file_id)
  fpathbuffer = fpathbuffer.replace(" ", "")
  file.download(fpathbuffer)
  mime = magic.Magic(mime=True)
  filetype = mime.from_file(fpathbuffer)
  
  
  if filetype == "audio/mpeg":
    os.remove(fpathbuffer)
    fpathbuffer = fpathbuffer + ".mp3"
    file.download(fpathbuffer)
    print("saved:" + fpathbuffer)
    rtag = tagpy.FileRef(fpathbuffer)
    tag = rtag.tag()
    print(tag.artist)
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO music (ID, TITLE, ARTIST, ALBUM, PATH, YEAR) VALUES (NULL, ?, ?, ?, ?, ?)",(safeStr(tag.title), safeStr(tag.artist), safeStr(tag.album), fpathbuffer, tag.year))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + safeStr(tag.title) + " from " + safeStr(tag.artist))
    print("## Uploaded:" + safeStr(tag.title) + " from: " + safeStr(tag.artist) + " -- Uploaded from: " + str(update.message.chat_id))
    
  if filetype == "audio/mp4a-latm":
    os.remove(fpathbuffer)
    fpathbuffer = fpathbuffer + ".m4a"
    file.download(fpathbuffer)
    print("saved:" + fpathbuffer)
    rtag = TinyTag.get(fpathbuffer)
    print(rtag.artist)
    db = sqlite3.connect("bot.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO music (ID, TITLE, ARTIST, ALBUM, PATH, YEAR) VALUES (NULL, ?, ?, ?, ?, ?)",(safeStr(rtag.title), safeStr(rtag.artist), safeStr(rtag.album), fpathbuffer, rtag.year))
    db.commit()
    db.close()
    update.message.reply_text('Hey ' + str(update.message.chat_id) + "\n"  'Your Uploaded: ' + safeStr(rtag.title) + " from " + safeStr(rtag.artist))  

  
def searchmusictitle(bot, update, args):
		con = sqlite3.connect("bot.db")
		cur = con.cursor()
		buffer = '' + ' '.join(str(e) for e in args)
		buffer = "*" + safeStr(buffer) + "*"
		titlebuffer = ""
		with con:
			cur = con.cursor()
			cur.execute("SELECT ID, ARTIST, TITLE, ALBUM, YEAR FROM music WHERE upper(TITLE) GLOB upper(?);",(buffer,))
			rows = cur.fetchall()
			countm = 1
			for row in rows:
				if countm < 22:
					titlebuffer = titlebuffer + "\n <b> Song ID: " + str(row) + "\n </b>"
					titlebuffer = titlebuffer.replace("(", " ")
					titlebuffer = titlebuffer.replace("u'", " ")
					titlebuffer = titlebuffer.replace('u"', '' )
					titlebuffer = titlebuffer.replace(")'", " ")
					titlebuffer = titlebuffer.replace("',", " ")
					countm +=1
				if countm == 22:
					bot.send_message(update.message.chat_id, 
                 text=titlebuffer, 
                 parse_mode=telegram.ParseMode.HTML)
					titlebuffer = ""
					countm = 1
		print("## Searched for: " + str(buffer))
		con.close()
		bot.send_message(update.message.chat_id, 
                 text=titlebuffer, 
                 parse_mode=telegram.ParseMode.HTML)

def searchmusicartist(bot, update, args):
		con = sqlite3.connect("bot.db")
		cur = con.cursor()
		buffer = '' + ' '.join(str(e) for e in args)
		buffer = "*" + buffer + "*"
		print(buffer)
		artistbuffer = ""
		with con:
			cur = con.cursor()
			cur.execute("SELECT ID, ARTIST, TITLE, ALBUM, YEAR FROM music WHERE upper(ARTIST) GLOB upper(?);",(buffer,))
			rows = cur.fetchall()
			countm = 1
			for row in rows:
				if countm < 22:
					artistbuffer = artistbuffer + "\n <b> Song ID: " + str(row) + "\n </b>"
					artistbuffer = artistbuffer.replace("(", " ")
					artistbuffer = artistbuffer.replace("u'", " ")
					artistbuffer = artistbuffer.replace('u"', '' )
					artistbuffer = artistbuffer.replace(")'", " ")
					artistbuffer = artistbuffer.replace("',", " ")
					countm +=1
				if countm == 22:
					bot.send_message(update.message.chat_id, 
                 text=artistbuffer, 
                 parse_mode=telegram.ParseMode.HTML)
					artistbuffer = ""
		print("## Searched for: " + str(buffer))
		con.close()
		bot.send_message(update.message.chat_id, 
                 text=artistbuffer, 
                 parse_mode=telegram.ParseMode.HTML)
                 
                 
def searchflac(bot, update, args):
		con = sqlite3.connect("bot.db")
		cur = con.cursor()
		buffer = '' + ' '.join(str(e) for e in args)
		buffer = "*" + buffer + "*"
		print(buffer)
		artistbuffer = ""
		with con:
			cur = con.cursor()
			cur.execute("SELECT ID, TITLE, ARTIST FROM flac WHERE (upper(TITLE) GLOB upper(?)) OR (upper(ARTIST) GLOB upper(?));",(buffer, buffer))
			rows = cur.fetchall()
			countm = 1
			for row in rows:
				if countm < 22:
					artistbuffer = artistbuffer + "\n <b> Song ID: " + str(row) + "\n </b>"
					artistbuffer = artistbuffer.replace("(", " ")
					artistbuffer = artistbuffer.replace("u'", " ")
					artistbuffer = artistbuffer.replace('u"', '' )
					artistbuffer = artistbuffer.replace(")'", " ")
					artistbuffer = artistbuffer.replace("',", " ")
					countm +=1
				if countm == 22:
					bot.send_message(update.message.chat_id, 
                 text=artistbuffer, 
                 parse_mode=telegram.ParseMode.HTML)
					artistbuffer = ""
		print("## Searched for: " + str(buffer))
		con.close()
		bot.send_message(update.message.chat_id, 
                 text=artistbuffer, 
                 parse_mode=telegram.ParseMode.HTML)
                 
def searchmusicalbum(bot, update, args):
		con = sqlite3.connect("bot.db")
		cur = con.cursor()
		buffer = '' + ' '.join(str(e) for e in args)
		buffer = "*" + buffer + "*"
		print(buffer)
		artistbuffer = ""
		with con:
			cur = con.cursor()
			cur.execute("SELECT ID, ARTIST, TITLE, ALBUM, YEAR FROM music WHERE upper(ALBUM) GLOB upper(?);",(buffer,))
			rows = cur.fetchall()
			countm = 1
			for row in rows:
				if countm < 22:
					artistbuffer = artistbuffer + "\n <b> Song ID: " + str(row) + "\n </b>"
					artistbuffer = artistbuffer.replace("(", " ")
					artistbuffer = artistbuffer.replace("u'", " ")
					artistbuffer = artistbuffer.replace('u"', '' )
					artistbuffer = artistbuffer.replace(")'", " ")
					artistbuffer = artistbuffer.replace("',", " ")
					countm +=1
				if countm == 22:
					bot.send_message(update.message.chat_id, 
                 text=artistbuffer, 
                 parse_mode=telegram.ParseMode.HTML)
					artistbuffer = ""
					countm = 1
		print("## Searched for: " + str(buffer))
		con.close()
		bot.send_message(update.message.chat_id, 
                 text=artistbuffer, 
                 parse_mode=telegram.ParseMode.HTML)

def downloadmusic(bot, update, args):
		userid = update.message.chat_id
		userid = str(userid)
		print(userid)
		print("test")
		conu = sqlite3.connect("/userlog.db")
		curu = conu.cursor()
		with conu:
			#curu = conu.cursor()
			curu.execute("SELECT userid FROM users WHERE userid = ?;",(userid,))
			rowus = curu.fetchall()
		useridbuffer = str(rowus)
		useridbuffer = useridbuffer.replace("[(", "")
		useridbuffer = useridbuffer.replace(",)]", "")
		useridbuffer = useridbuffer.replace("u'", "")
		useridbuffer = useridbuffer.replace("'", "")
		conu.close()
		print(useridbuffer)
		if useridbuffer == userid:
			userid = update.message.chat_id
			userid = str(userid)
			print(userid)
			print("test")
			conu = sqlite3.connect("/userlog.db")
			curu = conu.cursor()
			with conu:
			#curu = conu.cursor()
				curu.execute("SELECT premium FROM users WHERE userid = ?;",(userid,))
				rowus = curu.fetchall()
			premiumbuffer = str(rowus)
			premiumbuffer = premiumbuffer.replace("[(", "")
			premiumbuffer = premiumbuffer.replace(",)]", "")
			premiumbuffer = premiumbuffer.replace("u'", "")
			premiumbuffer = premiumbuffer.replace("'", "")
			conu.close()
			print(premiumbuffer)
			if premiumbuffer == 'premium':
				con = sqlite3.connect("bot.db")
				cur = con.cursor()
				buffer = '' + ' '.join(str(e) for e in args)
				cur = con.cursor()
				cur.execute("SELECT count(ID) FROM music;")
				rows = cur.fetchall()
				for row in rows:
					row = row
				rowb = str(row)
				rowb = rowb.replace("(", "")
				rowb = rowb.replace(",)", "")
				counter = int(rowb)
				print(buffer)
				if buffer:
						if isinstance(int(buffer), int) == True and int(str(buffer)) > counter:
							messagebuffer = "Error -> ID: " + str(buffer) + " is to high. \n We have " + str(counter) + " titles in the Database"
							update.message.reply_text(messagebuffer)
						else:
							with con:
								cur = con.cursor()
								cur.execute("SELECT PATH FROM music WHERE ID = ?;",(buffer,))
								rows = cur.fetchall()
								fpath = ''.join(str(rows))
								fpath = fpath.replace("[(u'", "")
								fpath = fpath.replace("',)]", "")
							con.close()
							bot.send_document(update.message.chat_id, document=open(fpath, 'rb'))
							print("## Downloaded: " + fpath + " from: " + str(update.message.chat_id))	
				if not buffer:
					update.message.reply_text("Error --> I need an File ID!")
			else:
				bot.send_message(update.message.chat_id, 
                  text="You need an Premium account to download or stream.\nGet Premium on teletransferx.com\nFree unlimited Music Streaming and unlimited File Downloads: https://t.me/Music_Streaming", 
                  parse_mode=telegram.ParseMode.HTML)
		else:
			bot.send_message(update.message.chat_id, 
                  text=" You need an Account to use TeleTransferX.\n Register an Account with your Chat ID on teletransferx.com\n Send /chatid to get your Chat ID", 
                  parse_mode=telegram.ParseMode.HTML)	
			
def downloadmovie(bot, update, args):
		userid = update.message.chat_id
		userid = str(userid)
		print(userid)
		print("test")
		conu = sqlite3.connect("/userlog.db")
		curu = conu.cursor()
		with conu:
			#curu = conu.cursor()
			curu.execute("SELECT userid FROM users WHERE userid = ?;",(userid,))
			rowus = curu.fetchall()
		useridbuffer = str(rowus)
		useridbuffer = useridbuffer.replace("[(", "")
		useridbuffer = useridbuffer.replace(",)]", "")
		useridbuffer = useridbuffer.replace("u'", "")
		useridbuffer = useridbuffer.replace("'", "")
		conu.close()
		print(useridbuffer)
		if useridbuffer == userid:
			userid = update.message.chat_id
			userid = str(userid)
			print(userid)
			print("test")
			conu = sqlite3.connect("/userlog.db")
			curu = conu.cursor()
			with conu:
			#curu = conu.cursor()
				curu.execute("SELECT premium FROM users WHERE userid = ?;",(userid,))
				rowus = curu.fetchall()
			premiumbuffer = str(rowus)
			premiumbuffer = premiumbuffer.replace("[(", "")
			premiumbuffer = premiumbuffer.replace(",)]", "")
			premiumbuffer = premiumbuffer.replace("u'", "")
			premiumbuffer = premiumbuffer.replace("'", "")
			conu.close()
			print(premiumbuffer)
			if premiumbuffer == 'premium':
				con = sqlite3.connect("bot.db")
				cur = con.cursor()
				buffer = '' + ' '.join(str(e) for e in args)
				cur = con.cursor()
				cur.execute("SELECT count(ID) FROM videos;")
				rows = cur.fetchall()
				for row in rows:
					row = row
				rowb = str(row)
				rowb = rowb.replace("(", "")
				rowb = rowb.replace(",)", "")
				counter = int(rowb)
				print(buffer)
				if buffer:
					if isinstance(int(buffer), int) == True and int(str(buffer)) > counter:
						messagebuffer = "Error -> ID: " + str(buffer) + " is to high. \n We have " + str(counter) + " movie titles in the Database"
						update.message.reply_text(messagebuffer)
					else:
						with con:
							cur = con.cursor()
							cur.execute("SELECT FILEID FROM videos WHERE ID = ?;",(buffer,))
							rows = cur.fetchall()
							fpath = ''.join(str(rows))
							fpath = fpath.replace("[(u'", "")
							fpath = fpath.replace("',)]", "")
						con.close()
						bot.send_document(update.message.chat_id, document=fpath)
						print("## Downloaded: " + str(fpath) + " from: " + str(update.message.chat_id))
				if not buffer:
					update.message.reply_text("Error --> I need an File ID!")
			else:
				bot.send_message(update.message.chat_id, 
                  text="You need an Premium account to download or stream.\nGet Premium on teletransferx.com\nFree unlimited Music Streaming and unlimited File Downloads: https://t.me/Music_Streaming", 
                  parse_mode=telegram.ParseMode.HTML)
		else:
			bot.send_message(update.message.chat_id, 
                  text=" You need an Account to use TeleTransferX.\n Register an Account with your Chat ID on teletransferx.com\n Send /chatid to get your Chat ID", 
                  parse_mode=telegram.ParseMode.HTML)	
			
def streammovie(bot, update, args):
		con = sqlite3.connect("bot.db")
		cur = con.cursor()
		buffer = '' + ' '.join(str(e) for e in args)
		cur = con.cursor()
		cur.execute("SELECT count(ID) FROM videos;")
		rows = cur.fetchall()
		for row in rows:
			row = row
		rowb = str(row)
		rowb = rowb.replace("(", "")
		rowb = rowb.replace(",)", "")
		counter = int(rowb)
		print(buffer)
		if buffer:
			if isinstance(int(buffer), int) == True and int(str(buffer)) > counter:
				messagebuffer = "Error -> ID: " + str(buffer) + " is to high. \n We have " + str(counter) + " movie titles in the Database"
				update.message.reply_text(messagebuffer)
			else:
				with con:
					cur = con.cursor()
					cur.execute("SELECT FILEID FROM videos WHERE ID = ?;",(buffer,))
					rows = cur.fetchall()
					fpath = ''.join(str(rows))
					fpath = fpath.replace("[(u'", "")
					fpath = fpath.replace("',)]", "")
				con.close()
				bot.send_video(update.message.chat_id, video=fpath, supports_streaming=True)
				print("## Streamed: " + str(fpath) + " from: " + str(update.message.chat_id))
			
		if not buffer:
			update.message.reply_text("Error --> I need an File ID!")
		
def streammusic(bot, update, args):
		userid = update.message.chat_id
		userid = str(userid)
		print(userid)
		print("test")
		conu = sqlite3.connect("/userlog.db")
		curu = conu.cursor()
		with conu:
			#curu = conu.cursor()
			curu.execute("SELECT userid FROM users WHERE userid = ?;",(userid,))
			rowus = curu.fetchall()
		useridbuffer = str(rowus)
		useridbuffer = useridbuffer.replace("[(", "")
		useridbuffer = useridbuffer.replace(",)]", "")
		useridbuffer = useridbuffer.replace("u'", "")
		useridbuffer = useridbuffer.replace("'", "")
		conu.close()
		print(useridbuffer)
		if useridbuffer == userid:
			userid = update.message.chat_id
			userid = str(userid)
			print(userid)
			print("test")
			conu = sqlite3.connect("/userlog.db")
			curu = conu.cursor()
			with conu:
			#curu = conu.cursor()
				curu.execute("SELECT premium FROM users WHERE userid = ?;",(userid,))
				rowus = curu.fetchall()
				premiumbuffer = str(rowus)
				premiumbuffer = premiumbuffer.replace("[(", "")
				premiumbuffer = premiumbuffer.replace(",)]", "")
				premiumbuffer = premiumbuffer.replace("u'", "")
				premiumbuffer = premiumbuffer.replace("'", "")
			conu.close()
			print(premiumbuffer)
			if premiumbuffer == 'premium':
				con = sqlite3.connect("bot.db")
				cur = con.cursor()
				buffer = '' + ' '.join(str(e) for e in args)
				print(buffer)
				if buffer == "random":
						cur = con.cursor()
						cur.execute("SELECT count(ID) FROM music;")
						rows = cur.fetchall()
						for row in rows:
							row = row
						rowb = str(row)
						rowb = rowb.replace("(", "")
						rowb = rowb.replace(",)", "")
						print(rowb)
						sum = int(rowb)
						rand = random.randint(1,sum)
						cur.execute("SELECT PATH FROM music WHERE ID = ?;",(rand,))
						rows = cur.fetchall()
						fpath = ''.join(str(rows))
						fpath = fpath.replace("[(u'", "")
						fpath = fpath.replace("',)]", "")
						with con:
							cur = con.cursor()
							cur.execute("SELECT * FROM music WHERE ID GLOB ?;",(rand,))
							rowd = cur.fetchall()
							for rowb in rowd:
								rowb = rowb
						con.close()
						rowb = str(rowb)
						rowb = rowb.replace("u'", "")
						rowb = rowb.replace("(", "")
						rowb = rowb.replace(")", "")
						rowb = rowb.replace("'", "")
						actitle = "<b> INFORMATION \nYou are now listen to Title No: " + str(rand) + " Title Info:</b> \n" + str(rowb)
						imagetg = TinyTag.get(fpath, image=True)
						image_data = imagetg.get_image()
						if image_data:
							#bot.send_photo(update.message.chat_id, photo=image_data)
							file = open("cv.jpg", "w")
							file.write(image_data)
							file.close()
							bot.send_photo(update.message.chat_id, photo=open('cv.jpg', 'rb'))
						bot.send_message(update.message.chat_id, 
                 text=actitle, 
                 parse_mode=telegram.ParseMode.HTML)
						bot.send_voice(update.message.chat_id, voice=open(fpath, 'rb'))
						print("## Streamed ->"+ fpath)
				else:
					cur = con.cursor()
					cur.execute("SELECT count(ID) FROM music;")
					rows = cur.fetchall()
					for row in rows:
						row = row
						rowb = str(row)
						rowb = rowb.replace("(", "")
						rowb = rowb.replace(",)", "")
					counter = int(rowb)
					print(buffer)
					if buffer:
						if isinstance(int(buffer), int) == True and int(str(buffer)) > counter:
							messagebuffer = "Error -> ID: " + str(buffer) + " is to high. \n We have " + str(counter) + " titles in the Database"
							update.message.reply_text(messagebuffer)
						else:
							with con:
								cur = con.cursor()
								cur.execute("SELECT PATH FROM music WHERE ID = ?;",(buffer,))
								rows = cur.fetchall()
								fpath = ''.join(str(rows))
								fpath = fpath.replace("[(u'", "")
								fpath = fpath.replace("',)]", "")
							with con:
								cur = con.cursor()
								cur.execute("SELECT * FROM music WHERE ID GLOB ?;",(buffer,))
								rowd = cur.fetchall()
								for rowb in rowd:
									rowb = rowb
							con.close()
							actitle = "<b> INFORMATION \nYou are now listen to Title No: " + str(buffer) + " Title Info:</b> \n" + str(rowb)
							imagetg = TinyTag.get(fpath, image=True)
							image_data = imagetg.get_image()
							#bot.send_photo(update.message.chat_id, photo=image_data)
							if image_data:
								#bot.send_photo(update.message.chat_id, photo=image_data)
								print(image_data)
								file = open("cv.jpg", "w")
								file.write(image_data)
								file.close()
								bot.send_photo(update.message.chat_id, photo=open('cv.jpg', 'rb'))
							bot.send_message(update.message.chat_id, 
          	 	      text=actitle, 
            	     parse_mode=telegram.ParseMode.HTML)
							bot.send_voice(update.message.chat_id, voice=open(fpath, 'rb'))
							print("## Streamed ->"+ fpath)
							#bot.send_voice(update.message.chat_id, voice=open(fpath, 'rb'))
					if not buffer:
						update.message.reply_text("Error --> I need an File ID!")
			else:
				bot.send_message(update.message.chat_id, 
                  text="You need an Premium account to download or stream.\nGet Premium on teletransferx.com\nFree unlimited Music Streaming and unlimited File Downloads: https://t.me/Music_Streaming", 
                  parse_mode=telegram.ParseMode.HTML)
		else:
				bot.send_message(update.message.chat_id, 
                  text=" You need an Account to use TeleTransferX.\n Register an Account with your Chat ID on teletransferx.com\n Send /chatid to get your Chat ID", 
                  parse_mode=telegram.ParseMode.HTML)		
			
def video_handler(bot, update):
    serverid = 859182254
    bot.send_video(serverid, video=update.message.video.file_id)
    update.message.reply_text("Thank, wie recieved your MP4")
    
  

  
  
def safeStr(obj):
  try: return str(obj)
  except UnicodeEncodeError:
    return obj.encode('ascii', 'ignore').decode('ascii')
  except: return ""
  	
def countdbmusic(bot, update):
	con = sqlite3.connect("bot.db")
	cur = con.cursor()
	cur = con.cursor()
	cur.execute("SELECT count(ID) FROM music;")
	rows = cur.fetchall()
	for row in rows:
		row = row
	rowb = str(row)
	rowb = rowb.replace("(", "")
	rowb = rowb.replace(",)", "")
	counter = int(rowb)
	counterstring = "<b> INFORMATION </b> \nWe have " + str(counter) + " titles in the Database"
	bot.send_message(update.message.chat_id, 
                 text=counterstring, 
                 parse_mode=telegram.ParseMode.HTML)
                 
def countdbflac(bot, update):
	con = sqlite3.connect("bot.db")
	cur = con.cursor()
	cur = con.cursor()
	cur.execute("SELECT count(ID) FROM flac;")
	rows = cur.fetchall()
	for row in rows:
		row = row
	rowb = str(row)
	rowb = rowb.replace("(", "")
	rowb = rowb.replace(",)", "")
	counter = int(rowb)
	counterstring = "<b> INFORMATION </b> \nWe have " + str(counter) + " titles in the Database"
	bot.send_message(update.message.chat_id, 
                 text=counterstring, 
                 parse_mode=telegram.ParseMode.HTML)
                 
def countdbfiles(bot, update):
	con = sqlite3.connect("bot.db")
	cur = con.cursor()
	cur = con.cursor()
	cur.execute("SELECT count(ID) FROM files;")
	rows = cur.fetchall()
	for row in rows:
		row = row
	rowb = str(row)
	rowb = rowb.replace("(", "")
	rowb = rowb.replace(",)", "")
	counter = int(rowb)
	counterstring = "<b> INFORMATION </b> \nWe have " + str(counter) + " Files in the Database"
	bot.send_message(update.message.chat_id, 
                 text=counterstring, 
                 parse_mode=telegram.ParseMode.HTML)
                 
def countdbbooks(bot, update):
	con = sqlite3.connect("bot.db")
	cur = con.cursor()
	cur = con.cursor()
	cur.execute("SELECT count(ID) FROM books;")
	rows = cur.fetchall()
	for row in rows:
		row = row
	rowb = str(row)
	rowb = rowb.replace("(", "")
	rowb = rowb.replace(",)", "")
	counter = int(rowb)
	counterstring = "<b> INFORMATION </b> \nWe have " + str(counter) + " books in the Database"
	bot.send_message(update.message.chat_id, 
                 text=counterstring, 
                 parse_mode=telegram.ParseMode.HTML)
                 
def countdbmovies(bot, update):
	con = sqlite3.connect("bot.db")
	cur = con.cursor()
	cur = con.cursor()
	cur.execute("SELECT count(ID) FROM videos;")
	rows = cur.fetchall()
	for row in rows:
		row = row
	rowb = str(row)
	rowb = rowb.replace("(", "")
	rowb = rowb.replace(",)", "")
	counter = int(rowb)
	counterstring = "<b> INFORMATION </b> \nWe have " + str(counter) + " titles in the Database"
	bot.send_message(update.message.chat_id, 
                 text=counterstring, 
                 parse_mode=telegram.ParseMode.HTML)
	

def callback_handler(bot, update):
	print(str(update.callback_query.data))
													
def musicmemory(bot, update):
	path = 'music'
	size = subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
	musicfoldersize = "<b> INFORMATION </b> \n <i>Music DB size: " + size +"B </i>"
	bot.send_message(update.message.chat_id, 
														text=musicfoldersize, 
														parse_mode=telegram.ParseMode.HTML)
def filesmemory(bot, update):
	path = 'files'
	size = subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
	musicfoldersize = "<b> INFORMATION </b> \n <i>Music DB size: " + size +"B </i>"
	bot.send_message(update.message.chat_id, 
														text=musicfoldersize, 
														parse_mode=telegram.ParseMode.HTML)
	
def downloadfile(bot, update, args):
		userid = update.message.chat_id
		userid = str(userid)
		print(userid)
		print("test")
		conu = sqlite3.connect("/userlog.db")
		curu = conu.cursor()
		with conu:
			#curu = conu.cursor()
			curu.execute("SELECT userid FROM users WHERE userid = ?;",(userid,))
			rowus = curu.fetchall()
		useridbuffer = str(rowus)
		useridbuffer = useridbuffer.replace("[(", "")
		useridbuffer = useridbuffer.replace(",)]", "")
		useridbuffer = useridbuffer.replace("u'", "")
		useridbuffer = useridbuffer.replace("'", "")
		conu.close()
		print(useridbuffer)
		if useridbuffer == userid:
			userid = update.message.chat_id
			userid = str(userid)
			print(userid)
			print("test")
			conu = sqlite3.connect("/userlog.db")
			curu = conu.cursor()
			with conu:
			#curu = conu.cursor()
				curu.execute("SELECT premium FROM users WHERE userid = ?;",(userid,))
				rowus = curu.fetchall()
			premiumbuffer = str(rowus)
			premiumbuffer = premiumbuffer.replace("[(", "")
			premiumbuffer = premiumbuffer.replace(",)]", "")
			premiumbuffer = premiumbuffer.replace("u'", "")
			premiumbuffer = premiumbuffer.replace("'", "")
			conu.close()
			print(premiumbuffer)
			if premiumbuffer == 'premium':
				con = sqlite3.connect("bot.db")
				cur = con.cursor()
				buffer = '' + ' '.join(str(e) for e in args)
				cur = con.cursor()
				cur.execute("SELECT count(ID) FROM files;")
				rows = cur.fetchall()
				for row in rows:
					row = row
				rowb = str(row)
				rowb = rowb.replace("(", "")
				rowb = rowb.replace(",)", "")
				counter = int(rowb)
				print(buffer)
				if buffer:
					fileuids = buffer.split(",")
					for fileuid in fileuids:
						with con:
							cur = con.cursor()
							cur.execute("SELECT FILEID FROM files WHERE ID = ?;",(fileuid,))
							rows = cur.fetchall()
							fpath = ''.join(str(rows))
							fpath = fpath.replace("[(u'", "")
							fpath = fpath.replace("',)]", "")
						bot.send_document(update.message.chat_id, document=fpath)
					con.close()	
				if not buffer:
					update.message.reply_text("Error --> I need an File ID!")
			else:
				bot.send_message(update.message.chat_id, 
                  text="You need an Premium account to download or stream.\nGet Premium on teletransferx.com\nFree unlimited Music Streaming and unlimited File Downloads: https://t.me/Music_Streaming", 
                  parse_mode=telegram.ParseMode.HTML)
		else:
			bot.send_message(update.message.chat_id, 
                  text=" You need an Account to use TeleTransferX.\n Register an Account with your Chat ID on teletransferx.com\n Send /chatid to get your Chat ID", 
                  parse_mode=telegram.ParseMode.HTML)		

def searchfile(bot, update, args):
		userid = update.message.chat_id
		userid = str(userid)
		print(userid)
		print("test")
		conu = sqlite3.connect("/userlog.db")
		curu = conu.cursor()
		with conu:
			#curu = conu.cursor()
			curu.execute("SELECT userid FROM users WHERE userid = ?;",(userid,))
			rowus = curu.fetchall()
		useridbuffer = str(rowus)
		useridbuffer = useridbuffer.replace("[(", "")
		useridbuffer = useridbuffer.replace(",)]", "")
		useridbuffer = useridbuffer.replace("u'", "")
		useridbuffer = useridbuffer.replace("'", "")
		conu.close()
		print(useridbuffer)
		if useridbuffer == userid:
			con = sqlite3.connect("bot.db")
			cur = con.cursor()
			buffer = '' + ' '.join(str(e) for e in args)
			buffer = "*" + buffer + "*"
			print(buffer)
			artistbuffer = ""
			with con:
				cur = con.cursor()
				cur.execute("SELECT ID, NAME, FILETYPE FROM files WHERE upper(NAME) GLOB upper(?);",(buffer,))
				rows = cur.fetchall()
				countm = 1
				for row in rows:
					if countm < 22:
						artistbuffer = artistbuffer + "\n <b> FILE-ID: " + str(row) + "\n </b>"
						artistbuffer = artistbuffer.replace("(", " ")
						artistbuffer = artistbuffer.replace("u'", " ")
						artistbuffer = artistbuffer.replace('u"', '' )
						artistbuffer = artistbuffer.replace(")'", " ")
						artistbuffer = artistbuffer.replace("',", " ")
						countm +=1
					if countm == 22:
						bot.send_message(update.message.chat_id, 
               text=artistbuffer, 
                parse_mode=telegram.ParseMode.HTML)
						artistbuffer = ""
						countm = 1
			print("## Searched for: " + str(buffer))
			con.close()
			bot.send_message(update.message.chat_id, 
                 text=artistbuffer, 
                 parse_mode=telegram.ParseMode.HTML)
		else:
			bot.send_message(update.message.chat_id, 
                  text=" You need an Account to use TeleTransferX.\n Register an Account with your Chat ID on teletransferx.com\n Send /chatid to get your Chat ID", 
                  parse_mode=telegram.ParseMode.HTML)		



def streamflac(bot, update, args):
	con = sqlite3.connect("bot.db")
	cur = con.cursor()
	cur.execute("SELECT count(ID) FROM flac;")
	rows = cur.fetchall()
	for row in rows:
		row = row
		rowb = str(row)
		rowb = rowb.replace("(", "")
		rowb = rowb.replace(",)", "")
		counter = int(rowb)
	buffer = '' + ' '.join(str(e) for e in args)
	print(buffer)
	if buffer:
		if isinstance(int(buffer), int) == True and int(str(buffer)) > counter:
			messagebuffer = "Error -> ID: " + str(buffer) + " is to high. \n We have " + str(counter) + " titles in the Database"
			update.message.reply_text(messagebuffer)
		else:
			with con:
				cur = con.cursor()
				cur.execute("SELECT fileid FROM flac WHERE ID = ?;",(buffer,))
				rows = cur.fetchall()
				fpath = ''.join(str(rows))
				fpath = fpath.replace("[(u'", "")
				fpath = fpath.replace("',)]", "")
				with con:
					cur = con.cursor()
					cur.execute("SELECT * FROM flac WHERE ID GLOB ?;",(buffer,))
					rowd = cur.fetchall()
					for rowb in rowd:
						rowb = rowb
					actitle = "<b> INFORMATION \nYou are now listen to Title No: " + str(buffer) + " Title Info:</b> \n" + str(rowb)
							
					bot.send_message(update.message.chat_id, 
          	 	      text=actitle, 
            	     parse_mode=telegram.ParseMode.HTML)
					bot.send_document(update.message.chat_id, document=fpath)
					print("## Streamed ->"+ fpath)
						#bot.send_voice(update.message.chat_id, voice=open(fpath, 'rb'))
					con.close()
	if not buffer:
		update.message.reply_text("Error --> I need an File ID!")
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("<your bot id>")
    updater.dispatcher.add_handler(RegexHandler('^(/searchbooktitle_[\d]+)$', searchbooktitle))
    updater.dispatcher.add_handler(MessageHandler(Filters.document,file_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.audio,audio_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.video, video_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(pattern="1", callback=gvu))
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start, pass_args=True))
    dp.add_handler(CommandHandler("help", helper))
    dp.add_handler(CommandHandler("info", version))
    dp.add_handler(CommandHandler("searchbooktitle", searchbooktitle, pass_args=True))
    dp.add_handler(CommandHandler("countdbmusic", countdbmusic))
    dp.add_handler(CommandHandler("countdbflac", countdbflac))
    dp.add_handler(CommandHandler("countdbfiles", countdbfiles))
    dp.add_handler(CommandHandler("countdbmovies", countdbmovies))
    dp.add_handler(CommandHandler("countdbbooks", countdbbooks))
    dp.add_handler(CommandHandler("downloadbook", download, pass_args=True))
    dp.add_handler(CommandHandler("searchbookauthor", searchauthor, pass_args=True))
    dp.add_handler(CommandHandler("downloadmusic", downloadmusic, pass_args=True))
    dp.add_handler(CommandHandler("searchmusicartist", searchmusicartist, pass_args=True))
    dp.add_handler(CommandHandler("searchmusictitle", searchmusictitle, pass_args=True))
    dp.add_handler(CommandHandler("searchmusicalbum", searchmusicalbum, pass_args=True))
    dp.add_handler(CommandHandler("searchflac", searchflac, pass_args=True))
    dp.add_handler(CommandHandler("streamflac", streamflac, pass_args=True))
    dp.add_handler(CommandHandler("streammusic", streammusic, pass_args=True))
    dp.add_handler(CommandHandler("streammovie", streammovie, pass_args=True))
    dp.add_handler(CommandHandler("gvu", gvu))
    dp.add_handler(CommandHandler("gema", gema))
    dp.add_handler(CommandHandler("ddos", ddos))
    dp.add_handler(CommandHandler("riaa", riaa))
    dp.add_handler(CommandHandler("chatid", chatid))
    dp.add_handler(CommandHandler("searchmovie", searchmovie, pass_args=True))
    dp.add_handler(CommandHandler("downloadfile", downloadfile, pass_args=True))
    dp.add_handler(CommandHandler("searchfile", searchfile, pass_args=True))
    dp.add_handler(CommandHandler("downloadmovie", downloadmovie, pass_args=True))
    dp.add_handler(CallbackQueryHandler(callback_handler, pass_chat_data=False))
    dp.add_handler(CommandHandler("musicmemory", musicmemory))
    dp.add_handler(CommandHandler("filesmemory", filesmemory))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling(timeout=360)

    # Run the bot until you press Ctrl-C or the process receives 4SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()