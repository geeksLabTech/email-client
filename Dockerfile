FROM Ubuntu
FROM Python:3.7

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /opt/Telegram_Bot
ENTRYPOINT FLASK_APP=/opt/Telegram_Bot/app.py flask run

# TODO steps to deploy on heroku
# TODO setup mongodb
