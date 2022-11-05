from db_worker import add_user, message_history
import os
import random 
import telebot
import requests
from telebot import types
from datetime import datetime
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Menu 1")
    btn2 = types.KeyboardButton("Menu 2")
    btn3 = types.KeyboardButton("Menu 3")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, text="Hello world", reply_markup=markup)
    add_user(message.chat.id,message.from_user.first_name,message.from_user.username,message.from_user.language_code,datetime.now())

@bot.message_handler(content_types=['text'])
def funcc(message):
    message_history(message.message_id,message.chat.id,message.from_user.first_name,message.from_user.username,datetime.now(),message.text)

@bot.message_handler(content_types=['text'])
def func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Menu 1")
    btn2 = types.KeyboardButton("Menu 2")
    btn3 = types.KeyboardButton("Menu 3")
    markup.add(btn1, btn2, btn3)

    if message.text == 'Menu 1':
        markup_menu2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1_menu2 = types.KeyboardButton("Back")
        btn2_menu2 = types.KeyboardButton("Button 1 Menu 1")
        btn3_menu2 = types.KeyboardButton("Button 2 Menu 1")
        markup_menu2.add(btn1_menu2, btn2_menu2, btn3_menu2)

        bot.send_message(message.chat.id, text="Menu 1", reply_markup=markup_menu2)

    elif message.text == 'Menu 2':
        markup_menu3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1_menu3 = types.KeyboardButton("Back")
        btn2_menu3 = types.KeyboardButton("Button 1 Menu 2")
        btn3_menu3 = types.KeyboardButton("Button 2 Menu 2")
        markup_menu3.add(btn1_menu3, btn2_menu3, btn3_menu3)

        bot.send_message(message.chat.id, text="Menu 2", reply_markup=markup_menu3)
    
    elif message.text == 'Menu 3':
        markup_menu4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1_menu4 = types.KeyboardButton("Back")
        btn2_menu4 = types.KeyboardButton("Button 1 Menu 3")
        btn3_menu4 = types.KeyboardButton("Button 2 Menu 3")
        markup_menu4.add(btn1_menu4, btn2_menu4, btn3_menu4)

        bot.send_message(message.chat.id, text="Menu 3", reply_markup=markup_menu4)

    elif message.text == 'Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Menu 1")
        btn2 = types.KeyboardButton("Menu 2")
        btn3 = types.KeyboardButton("Menu 3")
        markup.add(btn1, btn2,btn3)

        bot.send_message(message.chat.id, text="Hello world", reply_markup=markup)

bot.infinity_polling()