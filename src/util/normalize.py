# -*- coding: utf-8 -*-
import jieba
import unicodedata
import re
from langconv import *

class Normalize:
    
    delimiters = "!|\?|\.\.\.|！|。|？".decode('utf-8')
    
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
        # loop through document list
        texts=[]
        for tokens in documents:
            # clean and tokenize document string
            a=[]
            for token in tokens:
                # Assume all stop words are single Chinese characters
                # TODO: replace hard coded length to stop words 
                w = token.strip().rstrip()
                w = re.sub(r'[@|#|$|%|^|&|*]',r'',w)
                if (w.isalnum() and len(w)>3):
                      a.append(w)                      
                elif len(w)>1:
                      a.append(w)       
            # Remove empty line
            if a:
                texts.append(a)
        return texts
    
    def translate(self, documents):
        c=Converter('zh-hant')  
        documents_zh = [c.convert(line) for line in documents]
        return documents_zh

    # Remove comment after 4 April 2016
    # Save 75% time if not using user dict
    # Default dictionary is substituted by userdict
    # jieba.load_userdict(userdict)
    def segment(self,documents):
        # loop through document list
        texts=[]
        for line in documents:
            # clean and tokenize document string
            tokens=[w.strip().rstrip() for w in jieba.cut(line)]
            texts.append(tokens)
        return texts
    
