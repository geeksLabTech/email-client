import typer
from email_get import recieve_mail
from email_send import send_mail


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


# launch cli app
if __name__ == '__main__':
    app()
