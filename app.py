import os
from pyrogram import Client, filters
from tools.read_config import read_config

from email_client.email_send import send_mail
from email_client.email_get import recieve_mail

config_data = read_config('./config/config_bot.json')
app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'])


# @app.on_message(filters.text)
# def responder(client,message):
#     message.reply_text("hello "+message.from_user.mention)
    
@app.on_message(filters.command('recieve'))
def recieve_emails(client, message):
    
    # print(message)
    message.reply_text('getting emails') 
    
    texts = message.text.split(" ")
    user = texts[1]
    pwd = texts[2]
    emails = recieve_mail(user,pwd)
    # # for i in 
    # print(emails)
    message.reply_text(emails[0])

if __name__ == '__main__':
    app.run()
    # main()

