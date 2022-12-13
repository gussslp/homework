import telebot
from telebot import types
import json
import requests
import youtube_dl
from PIL import Image
import os, re
from db_worker import add_video
bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Hello")


@bot.message_handler(content_types=['text'])
def func(message):
    bot.delete_message(message.chat.id, message.message_id)
    link = message.text

    if link.find('youtu')!=-1:
        try:
            ydl_opts = {
                    'outtmpl': '%(title)s.%(ext)s',
                    'format': 'bestaudio/best',
                    'noplaylist': True,
                    'writethumbnail': True,
                    'nocheckcertificate': True,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320'
                        }]
                    }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link)
            title = info['title']
            name = title.replace("/", "_").replace('"', "'")
            punct = '[---]+'
            lst = re.split(punct, title)
            if len(lst)!=1:
                performer = lst[0]
                song_title = lst[1]
            else:
                performer = info['uploader']
                song_title = title

            
            add_video(song_title,performer,link)
            k = open(name+'.mp3', 'r+b')
            try: im = Image.open(name+'.jpg')
            except: im = Image.open(name+'.webp')
            bot.send_photo(message.chat.id, im, caption='youtu.be/'+info['id'])
            bot.send_audio(message.chat.id, k, performer=performer, title=song_title)
            k.close()
            try: os.remove(name+'.jpg')
            except: os.remove(name+'.webp')
            os.remove(name+'.mp3')

        except:
            bot.send_message(message.chat.id, 'Помилка')
    else:
        bot.send_message(message.chat.id, 'Помилка, не вірне посилання')

bot.infinity_polling()

