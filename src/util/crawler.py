import requests
import unicodedata
import HTMLParser
from readability.readability import Document
from BeautifulSoup import BeautifulSoup

class Crawler():
    
    def loadFromWeb(cls,url):   
        html = requests.get(url).content
        readable_article = Document(html).summary()
        readable_title = Document(html).short_title()
        cleantext = BeautifulSoup(readable_article).text
        cleantext = HTMLParser.HTMLParser().unescape(cleantext)
        return cleantext
    
    def loadFromFile(cls,filePath):
        text=""
        with open(filePath) as f:
            for line in f:
                text=text+line
        return text.decode('utf-8')
    
    def save(cls,filePath,document):
        with open(filePath,'w') as f:
            for line in document:
                f.write(line.encode('utf-8'))
        return     