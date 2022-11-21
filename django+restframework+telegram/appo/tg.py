import shutil
from db_worker import add_user, message_history
import telebot
import requests
from datetime import datetime
bot = telebot.TeleBot("token")
a = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Hello world")
    add_user(message.chat.id,message.from_user.first_name,message.from_user.username,message.from_user.language_code,datetime.now())

@bot.message_handler(content_types=['text'])
def funcc(message):
    message_history(message.message_id,message.chat.id,message.from_user.first_name,message.from_user.username,datetime.now(),message.text)
    bot.send_message(message.chat.id, text="texto")
@bot.message_handler(content_types=['photo'])
def photo(message):
    global a
    bot.send_message(message.chat.id, text="photo")
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image"+str(a)+".jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    
    src_path = r"image"+str(a)+".jpg"
    dst_path = r"../media/images"
    shutil.move(src_path, dst_path)

    a = a+1


bot.infinity_polling()