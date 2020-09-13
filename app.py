
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

app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'], bot_token=config_data['bot_token'])
create_db_connection('users_db')

# app = appl.run
# app()

def get_fernet():
    key = ''
    with open('./config/encrypt.key', 'r') as f:
        key = f.readline()
    f = Fernet(key)
    return f
 
@app.on_message(filters.command('recieve'))
def recieve_emails(client, message: Message):
    
    message.reply_text('getting emails') 
    
    f = get_fernet()
    
    try:
        user = UserDb.objects.get(chat_id=message.chat.id)
    except DoesNotExist:
        message.reply_text(
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
            message.reply_text('Error al loguearse, quizas deba cambiar su usuario o contraseña')
        except Exception as e:
            message.reply_text(str(e) + 
            ' Por favor reporte este error al equipo de desarrollo :)'
            )
        else:
            for i in emails:
                message.reply_text(i)

# TODO make this (send) to work with diferent messages, 
# /send triggers the action and 
# then it asks for the email of the reciever
# then the subject and finally the body of the email 

@app.on_message(filters.command('send'))
def send_email(client,message: Message):
    
    # extract identifier fromm message (chat_id)
    try:
        user = UserDb.objects.get(chat_id=message.chat.id)
    except DoesNotExist:
        message.reply_text(
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
            message.reply_text(
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
                message.reply_text('Error al loguearse, quizas deba cambiar su usuario o contraseña')
            except Exception as e:
                message.reply_text(str(e) + 
                ' Por favor reporte este error al equipo de desarrollo :)'
                )  
            else: 
                message.reply_text('Enviado!')
    
@app.on_message(filters.command('version'))
def get_version(client, message: Message):
    message.reply_text('V-0.2') 

@app.on_message(filters.command('register'))
def register_user(client, message: Message):
    
    texts = message.text.split(" ")
    if(len(texts) != 3):
        message.reply_text('Debe Introducir los campos usuario y contraseña separados por un espacio')
    
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
        message.reply_text('Registrado correctamente!')
        
@app.on_message(filters.command('logout'))
def register_user(client, message: Message):
    user = UserDb.objects.get(chat_id=message.chat.id)
    user.delete()
    message.reply_text('logued out') 
    
@app.on_message(filters.command('help'))
@app.on_message(filters.command('start'))
def register_user(client, message: Message):
    message.reply_text('''/register <email> <password> : register your email and password \n 
                          /logout : if you are logued in, it removes your email and password from the database  
                          /recieve : if you are registered this will send you your latest emails (unread)
                          /send <email> <subject> <body> : send to <email> a mail with the subject <subject> and with <body> as the text
                          /version : tells you the current vesion of the bot (debug purposes)  
                       ''')
    
    
# if __name__ == '__main__':
#     app.run()
    

def __ca