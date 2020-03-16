import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
filename = '/Users/franceebbasta/PycharmProjects/cvData/cv/'
with os.scandir(filename) as entries:
    for entry in entries:
        print(entry.name)
        pdffFileObect = open(filename+entry.name, 'rb')
        print(pdffFileObect, 'non')
        pdfReader = PyPDF2.PdfFileReader(pdffFileObect)
        pageObj = pdfReader.getPage(0)
        text2 = textract.process(filename+entry.name,)
        text = text2.decode("utf-8")
        print(text)




