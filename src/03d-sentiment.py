import sys
from util.model_sentiment import *

infile = sys.argv[1]
outfile = sys.argv[2]
# [doc2vec_model, glm_model]
modelfile = [sys.argv[3],sys.argv[4]] 

m=Sentiment(modelfile[0],modelfile[1])

document=m.load(infile)

sentiment=m.getSentenceSentiment(document,True)

m.save(outfile,sentiment) 