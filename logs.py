import os

def demo():
    dir = "C:/Users/somanyu/Desktop/destination/PDFs/airblue"
    onlyfiles = next(os.walk(dir))[2]  
    airbluePDFsfiles = len(onlyfiles)

    dir = "C:/Users/somanyu/Desktop/destination/PDFs/airindiaexpress"
    onlyfiles = next(os.walk(dir))[2]  # dir is your directory path as string
    airindiaPDFsfiles = len(onlyfiles)

    dir = "C:/Users/somanyu/Desktop/destination/PDFs/destination"
    onlyfiles = next(os.walk(dir))[2]  
    destinationPDFsfiles = len(onlyfiles)

    return airbluePDFsfiles, airindiaPDFsfiles, destinationPDFsfiles


train = demo()

# print(train[2])