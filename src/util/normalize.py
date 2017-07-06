# -*- coding: utf-8 -*-
import jieba
import unicodedata
import re
import HTMLParser
from langconv import *

class Normalize:

    delimiters = "!|\?|\.\.\.|！|，|。|？|,|\.".decode('utf-8')
    stopword={k:k for k in ['a','at','there','out','who','his','by','after','were','it','be','had','says','said','been','that','is','to','on','so','where',
    'up','down','and','are','her','not','for','was','he','she','also','into','more','about','with','within','only','around','each','these','course','then','between','you','your','than',
    'will','from','though','name','using','before','this','that','with','an','we','I','they','their','have','has','as','of','in','am' 'and','the']}
    def load(self,filePath):
        documents=[]
        with open(filePath) as f:
            for line in f:
                documents.append(line.decode('utf-8'))
        return documents

    def save(self,filePath,documents):
        with open(filePath,'w') as f:
            docs=""
            for token in documents:
                line=""
                for word in token:
                    line+=word.encode('utf-8')+" "
                docs+=line.rstrip()+"\n"
            f.write(docs)
            return

    def seperateLines(self,cleantext):
        output=""
        # Split sentences into seperated new line
        for line in cleantext:
            delimiter = re.findall(self.delimiters,line)
            sentence=""
            for word in line:
                if(word in delimiter):
                    word+="\n"
                sentence+=word
            output+=sentence
        return output.strip().split("\n")

    def clean(self,documents):
        clean_doc = [HTMLParser.HTMLParser().unescape(line) for line in documents]
        clean_doc = [(re.sub(r'[<|>|+|=|_|@|#|$|%|^|&|*]',r'',line)) for line in documents]

        return clean_doc


    def translate(self, documents):
        c=Converter('zh-hant')
        documents_zh = [c.convert(line) for line in documents]
        return documents_zh

    def segment(self,documents):
        # loop through document list
        texts=[]
        for line in documents:
            # clean and tokenize document string
            tokens=[w.strip().rstrip() for w in jieba.cut(line)]
            texts.append(tokens)
        return texts

    def removeStopWords(self,documents):
        texts=[]
        for tokens in documents:
            # clean and tokenize document string
            a=[]
            for token in tokens:
                # Remove special character, Chinese
                # and English stop words (determined by length)
                # TODO: replace hard coded length to stop words
                w = token.strip().rstrip()

                if w.isalnum():
                    if not self.stopword.has_key(w.lower()) and len(w)>1:
                        a.append(w)
                elif len(w)>1 :
                    a.append(w)
            # Remove empty line
            if a:
                texts.append(a)
        return texts
