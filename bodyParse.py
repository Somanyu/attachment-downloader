import imaplib
import base64
import os
import pdfplumber
import email
import mailbox

def parsing():
    mail = imaplib.IMAP4_SSL("imap.gmail.com", port=993)
    mail.login('Solutionssoftel@gmail.com', 'Temp12345')
    mail.select()

    result, data = mail.uid('search', None, 'ALL')
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        body = ""

        if email_message.is_multipart():
            for part in email_message.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)
                    if "IndiGo" in str(body):
                        print(body)
        else:
            body = email_message.get_payload(decode=True)
            if "IndiGo" in str(body):
                print(body)

parsing()