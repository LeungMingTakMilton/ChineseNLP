import os
import re
import math
import operator
import unicodedata
from collections import defaultdict,Counter
from gensim import corpora, models

class KeyModel:
    
    dict_records = []
    doc_num = 0
    topic_num = 3 # Default 3 topics in lsi
    
    def setTopic(self,i):
        self.topic_num=i
    
    def __init__(self, *args, **kwargs):
        dict_records=[]

        # dictfile format: 
        # <index>\t<token>\t<occurrence>\n
        if(len(args)>0):
            dictfile = args[0]
            for line in open(dictfile):
                    dict_records.append(re.split(r'\t|\n| ',line))
    
    def ngrams(self, documents, n):
        bag_of_words=[documents[i][j] for i in range(len(documents)) for j in range(len(documents[i]))]
        output = {}
        for i in range(len(bag_of_words)-n+1):
            g = ' '.join(bag_of_words[i:i+n])
            output.setdefault(g, 0)
            output[g] += 1
        return sorted(output.items(), key=operator.itemgetter(1), reverse=True)
    
    def tfidf(self, documents):
        
        bag_of_words=[documents[i][j] for i in range(len(documents)) for j in range(len(documents[i]))]

        d = self.dict_records
        word = [x[1] for x in d]
        word_in_docs_count = [x[2] for x in d]
        record = dict(zip(word,word_in_docs_count))

        total_docs = self.doc_num # tfidf_dict.num_docs
        total_words = len(bag_of_words)
        count = Counter(bag_of_words)

        output=[]
        for key,value in count.iteritems():
            if(record.has_key(key)):
                occur = float(record.get(key))
            else:
                occur = 0
            tf = value/float(total_words)
            idf =  math.log((total_docs+1)/(occur+1),2)
            output.append((key,float("{0:.4f}".format(tf*idf))))
        return sorted(output, key=operator.itemgetter(1),reverse=True)    
    def topics(self,documents):
        
        dictionary = corpora.Dictionary(documents)

        # convert tokenized documents into a document-term matrix
        corpus = [dictionary.doc2bow(document) for document in documents]    
        tfidf = models.TfidfModel(corpus)        
        numTopics=min(self.topic_num,len(documents))
        lsi = models.LsiModel(tfidf[corpus], id2word=dictionary, num_topics=numTopics)
        
        # Convert separated (word,score) vectors to
        # word-score matrix; 0 represents empty entries
        topics=[lsi.show_topic(i) for i in range(numTopics)]
        d = defaultdict(list)
        for i in range(len(topics)):
            fuck = []
            for k,v in topics[i]:
                if k not in d:
                    fuck.append((k,v))
                else:
                    d[k].append(float("{0:.2f}".format(abs(v))))
            for k,v in fuck:
                for asdf in range(i):
                    d[k].append(0)
                d[k].append(float("{0:.2f}".format(abs(v))))
            for k,v in d.items():
                if len(v)<=i:
                    d[k].append(0)
        sort_d=sorted(d.iteritems(),key=operator.itemgetter(1),reverse=True)
        return sort_d
    
    def load(self,infile):
        document=[]
        for line in open(infile):
            line = line.decode('utf-8').rstrip().strip().split(" ")
            document.append(line)
        return document
    
    def save(self,outfile,model):
	dir = os.path.dirname(outfile)
	if not os.path.exists(dir):
    		os.makedirs(dir)
        with open(outfile,'w') as f:
            for word,count in model:
                f.write(word.encode('utf-8')+": " +str(count)+"\n")  
    
