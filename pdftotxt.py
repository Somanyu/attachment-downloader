import os
import pdfplumber
from PyPDF2 import PdfFileReader

AIRBLUE_TXT_PATH = "C:/Users/somanyu/Desktop/destination/Text/airblue/"
AIRBLUE_PDF_PATH = "C:/Users/somanyu/Desktop/destination/PDFs/airblue/"

AIRINDIAEXP_TXT_PATH = "C:/Users/somanyu/Desktop/destination/Text/airindiaexpress/"
AIRINDIAEXP_PDF_PATH = "C:/Users/somanyu/Desktop/destination/PDFs/airindiaexpress/"

destination_TXT_PATH = "C:/Users/somanyu/Desktop/destination/Text/destination/"
destination_PDF_PATH = "C:/Users/somanyu/Desktop/destination/PDFs/destination/"


def pdfToText(airline, path, fileName, newName, noOfPages):
    with pdfplumber.open(fileName) as pdf:
        extractText = str()
        if airline == "airindia":
            for i in range(0, noOfPages):
                pdfPages = pdf.pages[i]
                extractText += pdfPages.extract_text()

        elif airline == "airblue":
            # extractText = str()
            for j in range(0, noOfPages):
                pdfPages = pdf.pages[j]
                extractText += pdfPages.extract_text()

        elif airline == "destination":
            for k in range(0, noOfPages):
                pdfPages = pdf.pages[k]
                extractText += pdfPages.extract_text()

        destination_filePath = path + str(newName) + ".txt"
        destinationFile = open(destination_filePath, "a", encoding="utf-8")
        destinationFile.write(extractText)


def fileWriting():

    for airindiaexpFilename in os.listdir(AIRINDIAEXP_PDF_PATH):
        airindiaexp = os.path.join(AIRINDIAEXP_PDF_PATH, airindiaexpFilename)
        if os.path.isfile(airindiaexp):
            # print(airindiaexp)
            with open(airindiaexp, "rb") as f:
                airindiaPdf = PdfFileReader(f)
                numberPages = airindiaPdf.getNumPages()
                # print(numberPages)
            pdfToText(
                "airindia",
                AIRINDIAEXP_TXT_PATH,
                airindiaexp,
                airindiaexpFilename,
                numberPages,
            )
            cwd = os.getcwd()
            print(
                "Created {txtFile}.txt in {directory}\\Text\\airindiaexpress".format(
                    txtFile=airindiaexpFilename[:-4], directory=cwd
                )
            )

    for airblueFilename in os.listdir(AIRBLUE_PDF_PATH):
        airblue = os.path.join(AIRBLUE_PDF_PATH, airblueFilename)
        if os.path.isfile(airblue):
            # print(airblueFilename)
            with open(airblue, "rb") as f:
                airbluePdf = PdfFileReader(f)
                numberPages = airbluePdf.getNumPages()
                # print(numberPages)
            pdfToText(
                "airblue", AIRBLUE_TXT_PATH, airblue, airblueFilename, numberPages
            )
            cwd = os.getcwd()
            print(
                "Created {txtFile}.txt in {directory}\\Text\\airblue".format(
                    txtFile=airblueFilename[:-4], directory=cwd
                )
            )

    for destinationFilename in os.listdir(destination_PDF_PATH):
        destination = os.path.join(destination_PDF_PATH, destinationFilename)
        if os.path.isfile(destination):
            # print(destinationFilename)
            with open(destination, "rb") as f:
                destinationPdf = PdfFileReader(f)
                numberPages = destinationPdf.getNumPages()
            pdfToText(
                "destination",
                destination_TXT_PATH,
                destination,
                destinationFilename,
                numberPages,
            )
            cwd = os.getcwd()
            print(
                "Created {txtFile}.txt in {directory}\\Text\\destination".format(
                    txtFile=destinationFilename[:-4], directory=cwd
                )
            )
