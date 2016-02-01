#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import sys
from langconv import *
# Read wiki dump file name from argument
infname = sys.argv[1]
outfname = "texts.txt"

# Extract texts in abstracts and saved into a file (texts.txt)
infile = codecs.open(infname, "r", "utf-8")
outfile = codecs.open(outfname, "w", "utf-8")
i = 0
for l in infile:
    if l.startswith("<abstract>"):
        l = l.encode('utf-8')
        text = l.strip().replace("<abstract>","").replace("</abstract>","")
        text = Converter('zh-hant').convert(text.decode('utf-8'))
        if len(l) > 200:
            outfile.write("%s\n" % text)
            i = i + 1
            if i % 1000 == 0:
                print "%d abstracts extracted..." % i

outfile.close()
