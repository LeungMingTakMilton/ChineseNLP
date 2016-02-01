#!/usr/bin/python
# -*- coding: utf-8 -*-
import jieba
import codecs
import unicodedata
import sys
jieba.load_userdict("dict.txt.big.txt")
jieba.load_userdict("dict.txt")
jieba.load_userdict("PA2016-jieba.txt")
# Check if a word is all CJK characters
def isCJK(w):
    if not w.isalpha():
        return False
    for c in w:
        n = unicodedata.name(unicode(c))
        if not n.startswith("CJK"):
            return False
    return True

# Input file
infname = sys.argv[1]
infile = codecs.open(infname, "r", "utf-8")

# Output file
outfname = sys.argv[2]
outfile = codecs.open(outfname, "w", "utf-8")

i = 0
for l in infile:
    l = l.strip()
    words = []
    for w in jieba.cut(l):
        if len(w) > 1:
            if isCJK(w):
                words.append(w.strip())
    outfile.write("%s\n" % " ".join(words))
    i = i + 1
    if i % 1000 == 0:
        print "%d lines processed..." % i


outfile.close()
