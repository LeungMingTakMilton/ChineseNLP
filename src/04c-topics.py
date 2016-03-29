import sys
import unicodedata
import gensim
from gensim import corpora, models


infile = str(sys.argv[1])
outfile = str(sys.argv[2])

documents=[]
dict_records=[]
for line in open(infile):
    documents.append(line.rstrip().split(" "))      

dictionary = corpora.Dictionary(documents)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(document) for document in documents]    
# tfidf = models.TfidfModel(corpus)

# Maximum 3 topics in an essay
numTopics=3
if(len(documents) < 3):
    numTopics = len(documents)

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=numTopics)
    
with open(outfile,'w') as f:
    for i in range(numTopics):
        f.write("Topic "+str(i+1)+":\n")
        for word,score in lsi.show_topic(i):
            f.write( word.encode('utf-8')+", " +str(score)+"\n")  