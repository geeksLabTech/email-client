import email
import smtplib


def send_mail(sender, pwd, to, subject, text):
    
    smtpserver = smtplib.SMTP_SSL(host='smtp.estudiantes.matcom.uh.cu', port=465)   #create connection with the smtp server
    smtpserver.ehlo()                                                               #send enhaced HELO to the server to identify with the server
    smtpserver.login(sender,pwd)                                                    #login in the server with the credentials given
    msg = 'Subject:'+subject+'\n\n'+text                                            #create the email 
    smtpserver.sendmail(sender,to,msg)                                              #send the email

    smtpserver.close()                                                              #close connection
    