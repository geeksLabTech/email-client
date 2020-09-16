
import telebot
import datetime
import json
import flask
from flask import Flask
from flask import request

from tools.errors import LoginException
from pyrogram import Client, filters
from pyrogram.methods import password
from pyrogram.types import Message
from pyrogram.types.user_and_chats import chat
from tools.read_config import read_config

from email_client.email_send import send_mail
from email_client.email_get import recieve_mail

from model.db import *

from cryptography.fernet import Fernet
# import base64

config_data = read_config('./config/config_bot.json')


bot  = telebot.TeleBolt(config_data['bot_token'], threaded=False)
bot.set_webhook(config_data['URL'].format(secret), max_connections=1)
bot.polling(none_stop=True)

# app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'], bot_token=config_data['bot_token'])
create_db_connection('users_db')

app = Flask(__name__)

@app.route(config_data['URL'], methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.processs_new_updates([update])
        return 'OK'
    else:
        flask.abort(403)
        flask.abort(403)
    
def get_fernet():
    key = ''
    with open('./config/encrypt.key', 'r') as f:
        key = f.readline()
    f = Fernet(key)
    return f
 
# @app.on_message(filters.command('recieve'))
@bot.message_handler(command=['recieve'])
def recieve_emails(client, message: Message):
    
    bot.reply_to(message, ('getting emails') 
    
    f = get_fernet()
    
    try:
        user = UserDb.objects.get(chat_id=message.chat.id)
    except DoesNotExist:
        bot.reply_to(message, (
            '''
            Debe registrarse primero, por favor
            use el comando /register y escriba
            su nombre de usuario y contraseña
            separados por un espacio.
            '''
        )
    else:
        username = f.decrypt(user.username).decode()
        password = f.decrypt(user.password).decode()
    
        try:
            emails = recieve_mail(username, password)
        except LoginException:
            bot.reply_to(message, ('Error al loguearse, quizas deba cambiar su usuario o contraseña')
        except Exception as e:
            bot.reply_to(message, (str(e) + 
            ' Por favor reporte este error al equipo de desarrollo :)'
            )
        else:
            for i in emails:
                bot.reply_to(message, (i)

# TODO make this (send) to work with diferent messages, 
# /send triggers the action and 
# then it asks for the email of the reciever
# then the subject and finally the body of the email 

# @app.on_message(filters.command('send'))
@bot.message_handler(command=['send'])
def send_email(client,message: Message):
    
    # extract identifier fromm message (chat_id)
    try:
        user = UserDb.objects.get(chat_id=message.chat.id)
    except DoesNotExist:
        bot.reply_to(message, (
            '''
            Debe registrarse primero, por favor
            use el comando /register y escriba
            su nombre de usuario y contraseña
            separados por un espacio.
            '''
        )
    else:
        # get encryption/decryption tool load the key
        f = get_fernet()
    
        # get the email and password and decrypt it
        username = f.decrypt(user.username).decode()
        password = f.decrypt(user.password).decode()

        # get reciever email, subject and text for the email
        texts = message.text.split(" ")
        if(len(texts) < 3):
            bot.reply_to(message, (
                '''
                La estructura debe ser la siguiente:
                    *Destinatario
                    *Asunto
                    *Cuerpo
                '''
            )
        else:
            to = texts[1]
            subject = texts[2]
            
            body = ' '
            for i in texts[3:]:
                body = body+i+' '
    
            # send message and tell the user that the email is sent
            try:
                send_mail(username, password, to, subject, body)  
            except LoginException:
                bot.reply_to(message, ('Error al loguearse, quizas deba cambiar su usuario o contraseña')
            except Exception as e:
                bot.reply_to(message, (str(e) + 
                ' Por favor reporte este error al equipo de desarrollo :)'
                )  
            else: 
                bot.reply_to(message, ('Enviado!')
    
# @app.on_message(filters.command('version'))
@bot.message_handler(command=['version'])
def get_version(client, message: Message):
    bot.reply_to(message, ('V-0.2.1') 

# @app.on_message(filters.command('register'))
@bot.message_handler(command=['register'])
def register_user(client, message: Message):
    
    texts = message.text.split(" ")
    if(len(texts) != 3):
        bot.reply_to(message, ('Debe Introducir los campos usuario y contraseña separados por un espacio')
    
    else:
        username = texts[1]
        password = texts[2]
        chat_id = message.chat.id
        
        f = get_fernet()
    
        encrypted_username = f.encrypt(username.encode())
        encrypted_password = f.encrypt(password.encode())   

        try:
            user = UserDb.objects.get(chat_id=message.chat.id)
            user.username = encrypted_username
            user.password = encrypted_password
        except: 
            user = UserDb(
                chat_id=chat_id,
                username=encrypted_username, 
                password=encrypted_password
            )
    
        user.save()
        bot.reply_to(message, ('Registrado correctamente!')
        
# @app.on_message(filters.command('logout'))
@bot.message_handler(command=['logout'])
def register_user(client, message: Message):
    user = UserDb.objects.get(chat_id=message.chat.id)
    user.delete()
    bot.reply_to(message, ('logued out') 
    
# @app.on_message(filters.command('help'))
# @app.on_message(filters.command('start'))
@bot.message_handler(command=['start', 'help'])
def register_user(message: Message):
    bot.reply_to(message, ('''/register <email> <password> : register your email and password \n 
                          /logout : if you are logued in, it removes your email and password from the database  
                          /recieve : if you are registered this will send you your latest emails (unread)
                          /send <email> <subject> <body> : send to <email> a mail with the subject <subject> and with <body> as the text
                          /version : tells you the current vesion of the bot (debug purposes)  
                       ''')
    
    
# if __name__ == '__main__':
#     app.run()
    

def __ca