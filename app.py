import imaplib
import email
import os

USEREMAIL = 'anything@mail.com'
USERPASS = 'anythingpass'

def downloadAttachment():

    mail = imaplib.IMAP4_SSL("imap.gmail.com", port=993)
    mail.login(USEREMAIL, USERPASS)

    mail.select()

    result, data = mail.uid('search', None, 'ALL')
    mails = len(data[0].split())

    for i in range(mails):
        latestEmailUID = data[0].split()[x]
        result, emailData = mail.uid('fetch', latestEmailUID, '(RFC822)')

        rawEmail = emailData[0][1]
        rawEmailString = rawEmail.decode('utf-8')
        emailMessage = email.message_from_string(rawEmailString)

        for attach in emailMessage.walk():
            if content.get_content_maintype() == 'multipart':
                continue
            if content.get('Content-Disposition') is None:
                continue
            fileName = content.get_filename()

            if bool(fileName):
                if (fileName.endswith(".pdf")):
                    if (fileName.startwith('SOMETHING')):
                        filePath = os.path.join('PATH', fileName)
                        if not os.path.isFile(filePath):
                            fileWrite = open(filePath, 'wb')
                            fileWrite.write(content.get_payload(decode=True))
                            fileWrite.close()
                        cwd = os.getcwd()
                        uid = latestEmailUID.decode('utf-8')
                        print(f'Downloaded "{fileName}" in "{cwd}" with UID "{uid}"')

downloadAttachment()
