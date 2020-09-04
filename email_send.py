import email
import smtplib


def send_mail(sender, pwd, to, subject, text):
    
    smtpserver = smtplib.SMTP_SSL(host='smtp.estudiantes.matcom.uh.cu', port=465)
    smtpserver.ehlo()
    smtpserver.login(sender,pwd)
    msg = 'Subject:'+subject+'\n\n'+text
    smtpserver.sendmail(sender,to,msg)
    
    smtpserver.close()
    