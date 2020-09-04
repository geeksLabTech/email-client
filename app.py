from flask import Flask, request
import telegram
from telebot.credentials import URL, bot_user_name, bot_token
global bot
global TOKEN

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)