[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJavierOramas%2FTelegram-Mail&count_bg=%233D91C8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# Email Client 
==============

python email client for any email server that supports imap and smtp,   
using a telegram bot as interface

## Installation and Deployment
==============================


### Docker Container

The easiest method to deploy this software is using Docker,
Make sure you have <a href='https://docs.docker.com'>installed</a> Docker on your machine.</br>

Then run the following command to build the container

`sudo docker build .`

if this process ends with no errors you should be able to run the container 

`sudo docker run <container name>`

### Manual Install and Deploy

First of all make sure that your system is up to Date

(Ubuntu) `sudo apt-get update && sudo apt-get upgrade`

(Arch) `sudo pacman -Syu`

Then make sure that python3 is installed and in the latest version (3.8 at hte time of writting)
(Ubuntu) `sudo apt-get install python3`

(Arch) `sudo pacman -S python3`

Now install pip
(Ubuntu) `python3 -m pip install --upgrade pip`

(Arch) `python3 -m pip install --upgrade pip`

And then install the requirements

`pip install -r requirements.txt`

Now you are Ready to Deploy

#### Deploy to heroku manually

##### First approach:
You must to create an account on heroku and download heroku cli <a href='https://devcenter.heroku.com/articles/heroku-cli'>here</a>

##### Install heroku cli

Now, open a terminal and execute the following commands:

`$ heroku login`

`$ heroku create <name of your app>`

`$ git add .`

`$ git commit -m "first commit"`

`$ git push heroku master`

`$ heroku ps:scale web=1`

`$ heroku open`

##### Second approach:

If you have a Github account you can simply add a new app from heroku dashboard
and connect to your Github repo.
Now you can do automatically o manually deploys without the cli :)

If you need more information of how to deploy a python app on heroku refer to <a href='https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true'>this page</a>

### Email Servers Configuration

Finally to set up the bot and the server run: </br>

`pyhton3 main.py setup_bot` 

now you would be asked to input the bot token, name and url

`pyhton3 main.py setup_email` 

now you would be asked to input the email imap host and port as well as the smtp host and port
now you are ready to use the service

## Usage 
========

To check your inbox:</br>

`python3 main.py recieve your.email@estudiantes.matcom.uh.cu yourpassword`

</br>to send an email:</br>

`python3 main.py send your.email@estudiantes.matcom.uh.cu yourpassword reciever@example.com subject body`

</br>to get the help type:</br>

`python3 main.py`

</br>and for a specific command help type:</br>

`python3 main.py {command} --help`

# Telegram Bot
==============

You can access our telegram bot at @experimental_email_bot (temporary name) on telegram

