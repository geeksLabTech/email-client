import os
import email
import imaplib
import base64

def recieve_mail(email_user, email_pwd):
    mail = imaplib.IMAP4_SSL(host='correo.estudiantes.matcom.uh.cu', port=993)      #create conection with the imap server
    mail.login(email_user, email_pwd)                                               #login with the username and password

    #TODO allow to select other folders 
    mail.select('Inbox')                                                            #select all the inbox folder 


    type, data = mail.search(None, 'ALL')                                           #select all mails in the inbox
    
    mail_ids = data[0]                                                              #get the list with the email ids
    id_list = mail_ids.split()                                                  
    msg_list = []

    for num in id_list:                                                             #loop throw the emails
        typ, data = mail.fetch(num, '(RFC822)')                                     #get the mail and decode it
        
        #TODO get the unread mails separately
        for response_part in data:                                                  #loop throw the parts of the message          
            if isinstance(response_part, tuple):                                    
                msg = email.message_from_string(response_part[1].decode('utf-8'))   #get the message data and decode it
                email_subject = msg['subject']                                      #extract email subject
                email_from = msg['from']                                            #extract email sender

                print('From: ' + email_from + '\n')                                 #output extracted Data to the console
                print('Subject: ' + email_subject + '\n')
                print(msg.get_payload(decode=True))
                
                msg_list.append((email_subject, email_from, msg.get_payload(decode=True))) #append the mail to a list with all the emails
                
    return msg_list
        #to download attachments

        # raw_email = data[0][1]
        # raw_email_string = raw_email.decode('utf-8')
        #
        # email_message = ''                                                      #
        # email_message = email.message_from_string(raw_email_string) 
        # 
        # for part in email_message.walk():
        #     if part.get_content_maintype() = 'multipart':
        #         continue
        #     if part.get('Content-Disposition') is None:
        #         continue
        #     filename = part.get_filename()
        #     if bool(filename):
        #         filepath = os.join('./downloads', filename)
        #         if not os.path.isfile(filepath)
        #         fp = open(filepath, 'wb')
        #         fp.write(part.get_payload(decode=True))
        #         fp.close()
        #         subject = str(email_message).split('Subject', 1)[1].split('\nTo', 1)[0]
        #         print('Downloaded "{file}" from email titled "{subject}" with uid "{uid}".'.format(file=filename, subject=subject, uid=latest_email_uid.decode('utf-8')))
