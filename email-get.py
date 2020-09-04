import os
import email
import imaplib
import base64



## Credentials ################################################################
email_user = input('Email: ') 
email_pwd = input('Password: ') 


mail = imaplib.IMAP4_SSL(host='correo.estudiantes.matcom.uh.cu', port=993)
mail.login(email_user, email_pwd)

mail.select('Inbox')

type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    
    email_message = ''
    email_message = email.message_from_string(raw_email_string)
    # email_message = 
    
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']

            print('From: ' + email_from + '\n')
            print('Subject: ' + email_subject + '\n')
            print(msg.get_payload(decode=True))
            
    #to download attachments
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
            