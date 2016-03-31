# -*- coding: utf-8 -*-
import sys
import re
import unicodedata
from util.langconv import *

inputfile = str(sys.argv[1])
outputfile = str(sys.argv[2])

output=[]

out=open(outputfile,'w')

# Translate character from simplified Chinese to traditional Chinese
with open(inputfile) as f:
    for line in f:
        line = Converter('zh-hant').convert(line.decode('utf-8'))
        out.write(line.encode('utf-8'))

# with open(outputfile,'w') as f:
#     for sentence in content:
#         f.write(sentence.encode('utf-8'))