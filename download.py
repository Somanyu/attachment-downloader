import imaplib
import email
import attachments
# import sqlify
# import jsonify
# import kafkaProducer
# import pdftotxt


def download():
    # gmail login(IMAP)
    mail = imaplib.IMAP4_SSL("imap.gmail.com", port=993)
    mail.login('<EXAMPLE@MAIL.COM>', '<PASSWORD>') # Enter your mail and password
    mail.select()

    #type,data = mail.search(None, 'ALL')
    result, data = mail.uid('search', None, '(UNSEEN)')
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        #typ, data = mail.fetch(i, '(RFC822)' )
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        # downloading attachments
        email_message = email.message_from_string(raw_email_string)
        for content in email_message.walk():
            if content.get_content_maintype() == 'multipart':
                continue
            if content.get('Content-Disposition') is None:
                continue
            fromEmail = email_message['from']
            fileName = content.get_filename()
            # print(fromEmail)

            # Download condition based on Sender's mail
            if fromEmail == "Somanyu Samal <somanyu.samal@gmail.com>":
                attachments.airblue_download_attachments(
                    fileName, content, latest_email_uid)
            if fromEmail == "Somanyu Samal <somanyu.03samal@gmail.com>":
                attachments.aiExpress_download_attachments(
                    fileName, content, latest_email_uid)
            if fromEmail == '"destination order" <order@destination.com>':
                attachments.destination_download_attachments(
                    fileName, content, latest_email_uid)

# while 1==1:
    # download()
