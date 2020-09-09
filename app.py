import os
import pymongo

from pyrogram import Client, filters
from tools.read_config import read_config
from tools.db_tools import  search_user

from email_client.email_send import send_mail
from email_client.email_get import recieve_mail

from model.db import create_connection

from cryptography.fernet import Fernet
# import base64


config_data = read_config('./config/config_bot.json')
app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'])
db = create_connection()
table = db.users.users

# app = appl.run()

def get_fernet():
    key = ''
    with open('./config/encrypt.key', 'r') as f:
        key = f.readline()
    f = Fernet(key)
    return f
 
@app.on_message(filters.command('recieve'))
def recieve_emails(client, message):
    
    #extract identifier form client or message
    db_user = search_user(message.chat.id, db.users.users)[0]
    
    message.reply_text('getting emails') 
    
    f = get_fernet()
    print(db_user)
    user = f.decrypt(db_user['email']).decode()
    pwd = f.decrypt(db_user['password']).decode()
    
    
    emails = recieve_mail(user,pwd)
    for i in emails:
        message.reply_text(i)

# TODO make this (send) to work with diferent messages, 
# /send triggers the action and 
# then it asks for the email of the reciever
# then the subject and finally the body of the email 

@app.on_message(filters.command('send'))
def send_email(client,message):
    
    # extract identifier form message (chat_id)
    db_user = search_user(message.chat.id, table)[0]

    # get encryption/decryption tool load the key
    f = get_fernet()
    
    # get the email and password and decrypt it
    user = f.decrypt(db_user['email']).decode()
    pwd = f.decrypt(db_user['password']).decode()

    # get reciever email, subject and text for the email
    texts = message.text.split(" ")

    to = texts[1]
    subject = texts[2]
    body = texts[3]
    
    # send message and tell the user that the email is sent
    send_mail(user,pwd,to,subject, body)    
    message.reply_text('Sent!')
    
@app.on_message(filters.command('version'))
def get_version(client, message):
    message.reply_text('V-0.2') 

@app.on_message(filters.command('register'))
def register_user(client, message):
    
    texts = message.text.split(" ")
    email = texts[1]
    password = texts[2]
    
    userinfo = {}
    
    f = get_fernet()
    
    userinfo['identifier'] = message.chat.id
    userinfo['email'] = f.encrypt(email.encode())
    userinfo['password'] = f.encrypt(password.encode())
    
    result = table.insert_one(userinfo)
    message.reply_text('Registered!') 
    
    
if __name__ == '__main__':
    app.run()
    # main()

