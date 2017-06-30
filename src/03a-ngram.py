import sys
from util.model_key import *

infile = sys.argv[1]
ngramFiles =[sys.argv[2],sys.argv[3],sys.argv[4]]

m=KeyModel()

document=m.load(infile)

ngrams=[m.ngrams(document,i+1) for i in range(3)]

for i in range(3):
    m.save(ngramFiles[i],ngrams[i]) 
