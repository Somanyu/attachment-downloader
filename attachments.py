import os


def aiExpress_download_attachments(fileName, content, uid):
    if bool(fileName):
        if (fileName.endswith(".pdf")):
            filePath = os.path.join(
                'C:/Users/somanyu/Desktop/destination/PDFs/airindiaexpress', fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(content.get_payload(decode=True))
                fp.close()
            cwd = os.getcwd()
            print('Downloaded "{file}" in "{directory}\\PDFs\\airindiaexpress" with UID {uid}'.format(
                file=fileName, uid=uid.decode('utf-8'), directory=cwd))


def airblue_download_attachments(fileName, content, uid):
    if bool(fileName):
        if (fileName.endswith(".pdf")):
            filePath = os.path.join(
                'C:/Users/somanyu/Desktop/destination/PDFs/airblue', fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(content.get_payload(decode=True))
                fp.close()
            cwd = os.getcwd()
            print('Downloaded "{file}" in "{directory}\\PDFs\\airblue" with UID {uid}'.format(
                file=fileName, uid=uid.decode('utf-8'), directory=cwd))


def destination_download_attachments(fileName, content, uid):
    if bool(fileName):
        if (fileName.endswith(".pdf")):
            if(not fileName.startswith("destination")):
                # change the file path accordingly
                filePath = os.path.join(
                    'C:/Users/somanyu/Desktop/destination/PDFs/destination', fileName)
                if not os.path.isfile(filePath):
                    fp = open(filePath, 'wb')
                    fp.write(content.get_payload(decode=True))
                    fp.close()
                cwd = os.getcwd()
                print('Downloaded "{file}" in "{directory}\\PDFs\\destination" with UID {uid}'.format(
                    file=fileName, uid=uid.decode('utf-8'), directory=cwd))
