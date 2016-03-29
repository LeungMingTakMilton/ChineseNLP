import sys
import operator

# from gensim import corpora, models
# from gensim.corpora import MmCorpus

def ngrams(input, n):
    output = {}
    for i in range(len(input)-n+1):
        g = ' '.join(input[i:i+n])
        output.setdefault(g, 0)
        output[g] += 1
    return output

infile = str(sys.argv[1])
outfileFreq = str(sys.argv[2])
outfileBigram = str(sys.argv[3])
outfileTrigram = str(sys.argv[4])

document=[]

for line in open(infile):
    for word in line.split(" "):
        document.append(word.rstrip())      


frequency = ngrams(document,1)
bigram = ngrams(document,2)
trigram = ngrams(document,3)

frequency = sorted(frequency.items(), key=operator.itemgetter(1),reverse=True)
bigram = sorted(bigram.items(), key=operator.itemgetter(1),reverse=True)
trigram = sorted(trigram.items(), key=operator.itemgetter(1),reverse=True)

with open(outfileFreq,'w') as f:
    for word,count in frequency:
        f.write( word+", " +str(count)+"\n")   
with open(outfileBigram,'w') as f:
    for word,count in bigram:
        f.write( word+", " +str(count)+"\n")   
with open(outfileTrigram,'w') as f:
    for word,count in trigram:
        f.write( word+", " +str(count)+"\n")   

        
        
# lsi = models.LsiModel.load("wiki_lsi.mm")
# dictionary = corpora.Dictionary.load_from_text("wikiDict.txt")
# dictionary.add_documents(document) 
# 
# for word, index in dictionary.token2id.iteritems():
#     print word + ": " +str(index)
# 
# corpus = corpora.MmCorpus('test.mm')

# corpus = [dictionary.doc2bow(text) for text in document]

# convert tokenized documents into a document-term matrix
# tfidf = models.TfidfModel(corpus) 
# corpus_tfidf = tfidf[corpus]

# for id, cnt in corpus[0]:
#     print "(%s, %d) " % (dictionary[id], cnt),
# for id, score in tfidf[corpus[0]]:
#     print "(%s, %.2f) " % (dictionary[id], score),    
