import requests
import sys
import unicodedata
from readability.readability import Document
from BeautifulSoup import BeautifulSoup
# html = requests.get('http://initiumlab.com/').content

url=str(sys.argv[1])
outfile=str(sys.argv[2])

html = requests.get(url).content
readable_article = Document(html).summary()
readable_title = Document(html).short_title()
cleantext = BeautifulSoup(readable_article).text

# print cleantext

with open(outfile,'w') as f:
        f.write(cleantext.encode('utf-8'))   