# -*- coding: UTF-8 -*-

import requests
import telebot
import tmdbsimple as tmbd
from tokens import *

bot = telebot.TeleBot(TOKEN)
tmbd.API_KEY = API_KEY_TMBD

@bot.message_handler(commands=["start"])
def start_handler(m):

    bot.send_message(m.chat.id, " Bienvenido ")
    bot.send_message(m.chat.id, "   My Peliculas List   :D   ")


@bot.message_handler(commands=["valoradas"])
def search(m):
    url = "https://api.themoviedb.org/3/movie/top_rated?language=es-ES&api_key=" + API_KEY_TMBD
    response = requests.get(url)
    data = response.json()['results']
    for f in data[:10]:
        bot.send_message(m.chat.id, f['title'])


@bot.message_handler(commands=["populares"])
def search(m):
    url = "https://api.themoviedb.org/3/movie/popular?language=es-ES&api_key=" + API_KEY_TMBD
    response = requests.get(url)
    data = response.json()['results']
    for f in data[:10]:
        bot.send_message(m.chat.id, f['title'])



bot.polling()


