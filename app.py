# from logging import exception

#from flask import Flask, request
import os

#import telegram

from telegram.ext import Updater, CommandHandler
import logging
from telegram.ext.callbackcontext import CallbackContext

from telegram.update import Update
from telegram.bot import Bot
from telegram.botcommand import BotCommand

from telebot.credentials import URL, bot_user_name, bot_token
#from fastapi import FastAPI, Form
#import uvicorn
#import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


#app = FastAPI()

def start(update: Update, context: CallbackContext):
    bot: Bot = context.bot
    bot.send_message(
        chat_id = update.effective_chat._id_attrs,
        text='Espero funcionar ya!!'
    )

def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(token=bot_token, use_context=True)
    PORT = int(os.environ.get('PORT', '8443'))
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=bot_token)

    updater.bot.set_webhook(URL + bot_token)
    updater.idle()

if __name__ == '__main__':
    main()
   