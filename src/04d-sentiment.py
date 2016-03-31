# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec

# classifier
# from sklearn import svm
# from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

import sys
import unicodedata

infile =  str(sys.argv[1])
tokenfile = str(sys.argv[2])
outfile = str(sys.argv[3])
doc2vecModel = str(sys.argv[4])
lrModel = str(sys.argv[5])

tokens=[]
documents=[]

for line in open(infile):
    documents.append(line.rstrip())

for line in open(tokenfile):
    tokens.append(line.rstrip())

# doc2vec and lr model are trained from 12000 threads including
# comments about electronic goods, books and hotels
model = Doc2Vec.load(doc2vecModel)
lr = joblib.load(lrModel)

vectors=[]

# Apply the infered vectors the logistic regression model
prediction = lr.predict([model.infer_vector(token.split(" ")) for token in tokens])

with open(outfile,'w') as f:
    for i in range(len(documents)):
        f.write(documents[i]+", "+str(prediction[i])+"\n")
    f.write(str(reduce(lambda x, y: (x + y) / 2, prediction)))
