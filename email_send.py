import smtplib


def send_mail(sender, pwd, to, subject, text):
    # create connection with the smtp server
    smtpserver = smtplib.SMTP_SSL(host='smtp.estudiantes.matcom.uh.cu', port=465)   
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
