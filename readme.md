[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJavierOramas%2FTelegram-Mail&count_bg=%233D91C8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Build Status](https://img.shields.io/github/forks/Telegram-Mail/email-client.svg)](https://github.com/Telegram-Mail/email-client) [![Build Status](https://img.shields.io/github/stars/Telegram-Mail/email-client.svg)](https://github.com/Telegram-Mail/email-client) [![License](https://img.shields.io/github/license/Telegram-Mail/email-client.svg)](https://github.com/Telegram-Mail/email-client) [![Build Status](https://img.shields.io/travis/Telegram-Mail/email-client/master.svg)](https://travis-ci.org/Telegram-Mail/email-client)
![Build Status](https://img.shields.io/badge/Powered_by-pyrogram-orange?style=flat&logo=pyrogram)
[![deepcode](https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6IlRlbGVncmFtLU1haWwiLCJyZXBvMSI6ImVtYWlsLWNsaWVudCIsImluY2x1ZGVMaW50IjpmYWxzZSwiYXV0aG9ySWQiOjIyNTkyLCJpYXQiOjE1OTk5NjUwNjZ9.CrCIXty0ZOuGRyz2GjF4llbCD6XQu1Z7p5dKTI05als)](https://www.deepcode.ai/app/gh/Telegram-Mail/email-client/_/dashboard?utm_content=gh%2FTelegram-Mail%2Femail-client)

# Email Client 

python email client for any email server that supports imap and smtp,   
using a telegram bot as interface

## Installation and Deployment


### Manual Install and Deploy


First of all make sure that your system is up to Date

(Ubuntu) `sudo apt-get update && sudo apt-get upgrade`

(Arch) `sudo pacman -Syu`

Install Mongodb for users handle
(Ubuntu) `sudo apt-get install mongodb`

(Arch) `sudo pacman -S mongodb`

Set MongoDB daemon to run at startup:

`sudo systemctl enable mongod`
`sudo systemctl start mongod`

Then make sure that python3 is installed and in the latest version (3.8 at the time of writting)
(Ubuntu) `sudo apt-get install python3`

(Arch) `sudo pacman -S python3`

Now install pip
(Ubuntu) `python3 -m pip install --upgrade pip`

And then install the requirements

`pip install -r requirements.txt`

Now you are Ready to Deploy

### Email Servers Configuration

Finally to set up the bot and the server run: </br>

`pyhton3 main.py setup_bot` 

now you would be asked to input the bot token, name and url

`pyhton3 main.py setup_email` 

now you would be asked to input the email imap host and port as well as the smtp host and port
now you are ready to use the service

### Generate encryption key
Generate encryption key for the database, its very important that you keep this, if this key
gets lost you wont be able to decrypt the data</br>
`pyhton3 main.py setup_key` 


## Usage 

To check your inbox:</br>

`python3 main.py recieve your.email@estudiantes.matcom.uh.cu yourpassword`

</br>to send an email:</br>

`python3 main.py send your.email@estudiantes.matcom.uh.cu yourpassword reciever@example.com subject body`

</br>to get the help type:</br>

`python3 main.py`

</br>and for a specific command help type:</br>

`python3 main.py {command} --help`

# Telegram Bot

You can access our telegram bot at @experimental_email_bot (temporary name) on telegram

## Commands

### Register
in order to use the bot you need to register on the db, to do it, sent the bot the following info:</br>
`/register <email> <password>`
this will register email and password encripted on the db

### Recieve
to recieve unread emails just type:</br>
`/recieve`

### Send
to send an email type:</br>
`/send <reciever email> <subject> <body>`

### Logout
Loguot and remove your data from the server
`/logout`
