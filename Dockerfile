FROM ubuntu

RUN apt-get update && apt-get -y python3
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /opt/Telegram_Bot
ENTRYPOINT FLASK_APP=/opt/Telegram_Bot/app.py flask run