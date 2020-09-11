import os
import pymongo

from pyrogram import Client, filters
from pyrogram.methods import password
from pyrogram.types import Message, User, Chat
from pyrogram.types.user_and_chats import chat
from tools.read_config import read_config
from tools.db_tools import  search_user

from email_client.email_send import send_mail
from email_client.email_get import recieve_mail

from model.db import *

from cryptography.fernet import Fernet
# import base64

config_data = read_config('./config/config_bot.json')

app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'])
create_db_connection('users_db')

def get_fernet():
    key = ''
    with open('./config/encrypt.key', 'r') as f:
        key = f.readline()
    f = Fernet(key)
    return f
 
@app.on_message(filters.command('recieve'))
def recieve_emails(client, message: Message):
    
    #extract identifier form client or message
    # db_user = search_user(client, table)
    
    message.reply_text('getting emails') 
    
    f = get_fernet()
    
    user = UserDb.objects.get(chat_id=message.chat.id)

    username = f.decrypt(user.username).decode()
    password = f.decrypt(user.password).decode()
    
    
    emails = recieve_mail(username, password)
    for i in emails:
        message.reply_text(i)

# TODO make this (send) to work with diferent messages, 
# /send triggers the action and 
# then it asks for the email of the reciever
# then the subject and finally the body of the email 

@app.on_message(filters.command('send'))
def send_email(client,message: Message):
    
    # extract identifier fromm message (chat_id)
    user = UserDb.objects.get(chat_id=message.chat.id)

    # get encryption/decryption tool load the key
    f = get_fernet()
    
    # get the email and password and decrypt it
    username = f.decrypt(user.username).decode()
    password = f.decrypt(user.password).decode()

    # get reciever email, subject and text for the email
    texts = message.text.split(" ")

    to = texts[1]
    subject = texts[2]
    body = texts[3]
    
    # send message and tell the user that the email is sent
    send_mail(username, password, to, subject, body)    
    message.reply_text('Sent!')
    
@app.on_message(filters.command('version'))
def get_version(client, message: Message):
    message.reply_text('V-0.2') 

@app.on_message(filters.command('register'))
def register_user(client, message: Message):
    
    texts = message.text.split(" ")
    username = texts[1]
    password = texts[2]
    chat_id = message.chat.id

    f = get_fernet()

    encrypted_username = f.encrypt(username.encode())
    encrypted_password = f.encrypt(password.encode())   

    user = UserDb(
        chat_id=chat_id,
        username=encrypted_username, 
        password=encrypted_password
    )
    
    user.save()
@app.on_message(filters.command('logout'))
def register_user(client, message: Message):
    user = UserDb.objects.get(chat_id=message.chat.id)
    user.delete()
    message.reply_text('logued out') 
    
    #userinfo['identifier'] = message.chat.id
    #userinfo['email'] = f.encrypt(email.encode())
    #userinfo['password'] = f.encrypt(password.encode())
    
    #result = table.insert_one(userinfo)
    
if __name__ == '__main__':
    app.run()
    # main()

