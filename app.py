# from logging import exception

#from flask import Flask, request
import os

#import telegram

from telegram.ext import Updater, CommandHandler
import logging
from telegram.ext.callbackcontext import CallbackContext

from telegram.update import Update
from telegram.bot import Bot

from telebot.credentials import URL, bot_user_name, bot_token
from fastapi import FastAPI, Form
import uvicorn
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = bot_token
#bot = telegram.Bot(token=TOKEN)
app = FastAPI()
updater = Updater(token=TOKEN, use_context=True)
PORT = int(os.environ.get('PORT', '8443'))
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    bot: Bot = context.bot
    bot.send_message(
        chat_id = update.effective_chat._id_attrs,
        text='Hola, espero serte util y que no te pierdas un correo de la facultad 😁'
    )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


@app.get('/')
def index():
   return 'Funciona!!'

@app.get('/set_webhook')
def set_webhook():
    try:
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)

        updater.bot.set_webhook(URL + TOKEN)
        updater.idle()
        
        return "webhook setup ok"

    except Exception:
        return "webhook setup failed"


@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

if __name__ == '__main__':
    uvicorn.run(app)
   