import typer
from email_client.email_get import recieve_mail
from email_client.email_send import send_mail
import json
# from os import urandom
from cryptography.fernet import Fernet

# creating cli app
app = typer.Typer()


# send command 
@app.command(name='send', help='send mail, recieve the following args:\n sender: the email account\
    you want to use to send the email (this will not be stored anywhere)\n pwd: your password (this\
    will not be stored anywhere)\n to: the email account you want to \
    send your email to\n subject: the subject of the mail\n text: the body of the email')
def send(sender, pwd, to, subject, text):
    send_mail(sender, pwd, to, subject, text)


# recieve command
@app.command(name='recieve', help='check inbox and return all recieved emails, recieve the following arg:\n\
    email_user: your email account\n email_pwd: the password for your email')
def recieve(email_user, email_pwd):
    recieve_mail(email_user, email_pwd)

@app.command(name='setup_mail', help='set up all the config files for the app')
def setup_mail():
    
    # Get the config for the email server
    config_file = {}
    config_file['imap_host'] = input("Imap host: ")
    config_file['imap_port'] = input("Imap port: ")
    config_file['smtp_host'] = input("Smtp host: ")
    config_file['smtp_port'] = input("Smtp port: ")
    
    # Export it to the config file
    with open('./config/config_email.json', 'w') as json_file:
        json.dump(config_file,json_file)
        
@app.command(name='setup_bot', help='set up all the config files for the telegram bot')
def setup_bot():
    
    config_file = {}
    
    config_file['bot_token'] = input("Bot Token: ")
    config_file['bot_user_name'] = input("Bot User Name: ")
    config_file['URL'] = input("URL: ")
    
    with open('./config/config_bot.json', 'w') as json_file:
        json.dump(config_file,json_file)

@app.command(name='setup_key', help='create a random key for the db encryption')
def setup_key():    
    with open('./config/encrypt.key', 'wb') as f:
        f.write(Fernet.generate_key())


# launch cli app
if __name__ == '__main__':
    app()

