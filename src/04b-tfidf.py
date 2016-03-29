import sys
import re
import math
import operator
from collections import Counter

def tfidf(dictionary, total_words, total_docs):
    output=[]
    for key,value in count.iteritems():
        if(record.has_key(key)):
            occur = float(record.get(key))
        else:
            occur = 0
        tf = value/float(total_words)
        idf =  math.log((total_docs+1)/(occur+1),2)
        output.append((key,tf*idf))
    return output

infile = str(sys.argv[1])
outfile = str(sys.argv[2])
dictfile = str(sys.argv[3])

document=[]
dict_records=[]
for line in open(infile):
    for word in line.split(" "):
        document.append(word.rstrip())      
# dictfile format: 
# <index>\t<token>\t<occurrence>\n
for line in open(dictfile):
    dict_records.append(re.split(r'\t|\n',line))

word = [record[1] for record in dict_records]
word_in_docs_count = [record[2] for record in dict_records]

record = dict(zip(word,word_in_docs_count))

# for key,value in record.iteritems():
#     print key,value


# tfidf_dict = corpora.Dictionary.load("tfidf_dict")
# Magic number; Total documents in wiki 
total_docs = 227364 # tfidf_dict.num_docs
total_words = len(document)
count = Counter(document)
result = tfidf(count,total_words, total_docs)
result = sorted(result, key=operator.itemgetter(1),reverse=True)
    
with open(outfile,'w') as f:
    for word,count in result:
        f.write( word+", " +str(count)+"\n")   