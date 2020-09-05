import smtplib
from tools.read_config import read_config


def send_mail(sender, pwd, to, subject, text):
    # Read the email config file
    config = read_config('./config/config_email.json')
    # create connection with the smtp server
    smtpserver = smtplib.SMTP_SSL(host=config['smtp_host'], port=config['smtp_port'])   
    # send enhaced HELO to the server to identify with the server
    smtpserver.ehlo()                                                               
    # login in the server with the credentials given
    smtpserver.login(sender, pwd)                                                    
    # create the email 
    msg = 'Subject:'+subject+'\n\n'+text                                            
    # send the email
    smtpserver.sendmail(sender, to, msg)                                               

    # close connection
    smtpserver.close()                                                             
