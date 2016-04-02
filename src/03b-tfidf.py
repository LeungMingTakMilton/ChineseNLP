import sys
from util.model_key import *

infile = sys.argv[1]
outfile =sys.argv[2]

m=KeyModel()

document=m.load(infile)

tfidf=m.tfidf(document)

m.save(outfile,tfidf) 