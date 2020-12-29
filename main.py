import pyttsx3
import PyPDF2
book = open('react.pdf', 'rb')
readerPdf = PyPDF2.PdfFileReader(book)
pages = readerPdf.numPages
print(pages)

speech = pyttsx3.init()

# rate
rate = speech.getProperty('rate')
print(rate)
speech.setProperty('rate',120)

# voice change
voices = speech.getProperty('voices')
speech.setProperty('voice', voices[1].id)
for num in range(59, pages):
    page = readerPdf.getPage(num)
    text = page.extractText()
    speech.say('My current speaking rate is ' + str(rate))
    speech.say(text)
    speech.runAndWait()