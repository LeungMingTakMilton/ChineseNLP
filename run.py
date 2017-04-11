import sys
import getopt
from src.util.crawler import * 
from src.util.normalize import *
from src.util.model_key import *
from src.util.model_sentiment import *

def usage():
    print ("""
          usage:
          python run.py [-s|-t|-n|-l] [input file] [output path]
          python run.py -u [-s|-t|-n|-l] [url] [output path]
          """)
    return 

def main():
    useUrl=False
    useNgrams=False
    useTfIdf=False
    useLsi=False
    useSentiment=False

    try:
        lontOpts=["url","sentiment","tfidf","ngram","lsi"]
        opts, args = getopt.getopt(sys.argv[1:],'ustnl',lontOpts)
    except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err))
        usage()
        sys.exit(2)

    infile = args[0]
    outpath = args[1]

    # Default model path
    sentimentModelPath="model/train_news.d2v"
    linearModelPath="model/sentiment.mlr"
    tfidfModelPath="model/tfidf_dict.txt"

    # Default output files
    ngramsFile = [outpath+"/freq",outpath+"/bigram",outpath+"/trigram"]
    keyFile = outpath+"/score"
    topicFile = outpath+"/topics"
    sentimentFile = outpath+"/sentiment"

    for o, a in opts:
        if o in ("-u","--url"):
            useUrl = True
        elif o in ("-s", "--sentiment"):
            useSentiment = True
        elif o in ("-t", "--tfidf"):
            useTfIdf = True
        elif o in ("-n", "--ngram"):
            useNgrams = True
        elif o in ("-l", "--lsi"):
            useLsi = True
        else :
            assert False, "unhandled option"

    if(useUrl):
        raw=Crawler().loadFromWeb(infile)
    else:
        raw=Crawler().loadFromFile(infile)

    n=Normalize()
    token_zh=n.translate(n.clean(n.seperateLines([raw])))
    documents=n.removeStopWords(n.segment(token_zh))

    if(useTfIdf):
        # total_docs: magic number; total documents in wiki 
        # TODO: remove magic number
        m=KeyModel(tfidfModelPath)
        m.doc_num=227364
    else:
         m=KeyModel()
    
    if(useNgrams):
        ngrams=[m.ngrams(documents,i+1) for i in range(3)]
        for i in range(len(ngrams)):
            m.save(ngramsFile[i],ngrams[i])

    if(useTfIdf):
        score=m.tfidf(documents)
        m.save(keyFile,score)

    if(useLsi):
        topics=m.topics(documents)
        m.save(topicFile,topics)

    if(useSentiment):
        se=Sentiment(sentimentModelPath,linearModelPath)
        emotion=se.getSentenceSentiment(documents,True)
        # [["zh_word_1", "zh_word_2"...],[0.3,0.2,0,0,0.5,0,0,0]] ->
        # [["zh_word_1 zh_word_2..."],[0.3,0.2,0,0,0.5,0,0,0]]
        emotion=[([" ".join(x[0])],x[1]) for x in emotion]
        se.save(sentimentFile,emotion,True)

if __name__ == "__main__":
    main()


