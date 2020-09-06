import os
from pyrogram import Client, filters
from tools.read_config import read_config

from email_client.email_send import send_mail
from email_client.email_get import recieve_mail

config_data = read_config('./config/config_bot.json')
app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'])

 
@app.on_message(filters.command('recieve'))
def recieve_emails(client, message):
    
    message.reply_text('getting emails') 
    
    texts = message.text.split(" ")
    user = texts[1]
    pwd = texts[2]
    emails = recieve_mail(user,pwd)
    for i in emails:
        message.reply_text(i)

# TODO make this to work with diferent messages, 
# /send triggers the action and then it asks for credentials (or get them from the stored date)
# then it asks for the email of the reciever
# then the subject and finally the body of the email 

@app.on_message(filters.command('send'))
def send_email(client,message):
    
    texts = message.text.split(" ")
    user = texts[1]
    pwd = texts[2]
    to = texts[3]
    subject = texts[4]
    body = texts[5]
    
    send_mail(user,pwd,to,subject, body)    
    message.reply_text('Sent!')
    
@app.on_message(filters.command('version'))
def recieve_emails(client, message):
    message.reply_text('V-0.1') 

if __name__ == '__main__':
    app.run()
    # main()

