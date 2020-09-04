import email
import smtplib


def send_mail(sender, pwd, to):
    
    smtpserver = smtplib.SMTP_SSL(host='smtp.estudiantes.matcom.uh.cu', port=465)
    print('here')
    smtpserver.ehlo()
    # smtpserver.startssl()
    # smtpserver.ehlo()
    smtpserver.login(sender,pwd)
    msg = 'Subject:probando script\n esto esta mandado con el script'#+subject+'\n'+text
    smtpserver.sendmail(sender,to,msg)
    
    print('Sent')
    smtpserver.close()
    