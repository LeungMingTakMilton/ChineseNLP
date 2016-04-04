import sys
from util.normalize import *

infile = sys.argv[1]
outfile = sys.argv[2]

s=Normalize()

documents=s.load(infile)
#["","",.....""]
documents=s.seperateLines(documents)
#["","",.....""]
documents=s.clean(documents)
#["","",.....""]
documents=s.translate(documents)
#["","",.....""]
documents=s.segment(documents)
#[["",...""],["",...""]...,["",...""]]
documents=s.removeStopWords(documents)
#[["",...""],["",...""]...,["",...""]]
s.save(outfile,documents)