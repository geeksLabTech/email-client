## Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

# Email Client 
============================================================

python email client for the MATCOM UH mail
this allows to send and recieve emails withe the students account

## Installation and Deployment
============================================================


### Docker Container
============================================================

The easyest method to deploy this software is using Docker,
Make sure you have <a href='https://docs.docker.com'>installed</a> Docker on your machine.</br>
Then run the following command to build the container

`sudo docker build .`

if this process ends with no errors you should be able to run the container
`sudo docker run [container name]`

### Manual Install and Deploy
============================================================
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
<!-- TODO Daniel write the steps to deploy on heroku -->

## Usage 
============================================================

To check your inbox:</br>

`python3 main.py recieve your.email@estudiantes.matcom.uh.cu yourpassword`

</br>to send an email:</br>

`python3 main.py send your.email@estudiantes.matcom.uh.cu yourpassword reciever@example.com subject body`

</br>to get the help type:</br>

`python3 main.py`

</br>and for a specific command help type:</br>

`python3 main.py {command} --help`

# Telegram Bot
============================================================

You can access our telegram bot at @experimental_email_bot (temporary name) on telegram

