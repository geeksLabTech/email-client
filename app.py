# from logging import exception

from flask import request
import os

import telegram

from telegram.ext import Updater, CommandHandler
import logging
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from telegram.bot import Bot
from telegram.botcommand import BotCommand
import re
from telebot.credentials import URL, bot_user_name, bot_token
from fastapi import FastAPI, Form
#import uvicorn
#import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


app = FastAPI()
bot = telegram.Bot(token=bot_token)

@app.get("/")
def hello():
    return {"message":"Funciona!"}

@app.post('/{}'.format(bot_token))
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       Veras como ahora si funciono
       """
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)


   else:
       try:
           # clear the message we got from any non alphabets
           text = re.sub(r"W", "_", text)
           # create the api link for the avatar based on http://avatars.adorable.io/
           url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
           # reply with a photo to the name the user sent,
           # note that you can send photos by url and telegram will fetch it for you
           bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
       except Exception:
           # if things went wrong
           bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

   return 'ok'

@app.get('/set_webhook')
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=bot_token))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"

#def start(update: Update, context: CallbackContext):
#    bot: Bot = context.bot
#    bot.send_message(
#        chat_id = update.effective_chat._id_attrs,
#        text='Espero funcionar ya!!'
#    )

#def help_command(update: Update, context: CallbackContext):
#    """Send a message when the command /help is issued."""
#    update.message.reply_text('Help!')

#def echo(update: Update, context: CallbackContext):
#    update.message.reply_text(update.message.text)


#def main():
#    updater = Updater(token=bot_token, use_context=True)
#    PORT = int(os.environ.get('PORT', '8443'))
#    dispatcher = updater.dispatcher
#
#    start_handler = CommandHandler('start', start)
#    help_handler = CommandHandler('help', help)
#    dispatcher.add_handler(start_handler)
#    dispatcher.add_handler(help_handler)
#
#    updater.start_webhook(listen="0.0.0.0",
#                          port=PORT,
#                          url_path=bot_token)
#
#    updater.bot.set_webhook(URL + bot_token)
#    updater.idle()


#if __name__ == '__main__':
#    main()
   