# -*- coding: utf-8 -*-
import sys
import re
import unicodedata
from util.langconv import *

inputfile = str(sys.argv[1])
outputfile = str(sys.argv[2])

content=[]
output=[]
delimiters = "!|\?|\.\.\.|！|。|？".decode('utf-8')

# Translate character from simplified Chinese to traditional Chinese
with open(inputfile) as f:
    for line in f:
        line = Converter('zh-hant').convert(line.decode('utf-8'))
        content.append(line)

# Split sentences into seperated new line
for line in content:
    delimiter = re.findall(delimiters,line)
    sentence=""
    for word in line:
        if(word in delimiter):
            word+="\n"
        sentence=sentence+word
    output.append(sentence.strip())

with open(outputfile,'w') as f:
    for sentence in output:
        f.write(sentence.encode('utf-8'))