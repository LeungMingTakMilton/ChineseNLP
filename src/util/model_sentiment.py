# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec

# classifier
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression

import os

class Sentiment:
    
    model=None
    lr=None
    
    def __init__(self, doc2vecModel, linearModel):
        self.model = Doc2Vec.load(doc2vecModel)
        self.lr = joblib.load(linearModel)
        
    def getTotalSentiment(self,document):
        
        model=self.model
        lr=self.lr
        total_score=[[]]

        if(document):
            no_of_sentence=len(document)        
            bag_of_words=[document[i][j] for i in range(no_of_sentence) for j in range(len(document[i]))]
            vectors_documents=[model.infer_vector(bag_of_words)]
            total_score = lr.predict_proba(vectors_documents)
        
        return [float("{0:.2f}".format(x)) for x in total_score[0]]
     
    def getSentenceSentiment(self,document,Total=False):
        
        model=self.model
        lr=self.lr
        output=[]
        
        if(document):
            vectors = [model.infer_vector(token) for token in document]
            prediction = lr.predict_proba(vectors)
            output=[((document[i],([float("{0:.2f}".format(x)) for x in prediction[i]])))for i in range(len(document))]
        
        if(Total):
            total=("",self.getTotalSentiment(document))
            output.append(total)
        return output
    
    def load(self,infile):
        document=[]
        for line in open(infile):
            line = line.decode('utf-8').rstrip().strip().split(" ")
            document.append(line)
        return document
    
    def save(self,outfile,model,Total=False):
        dir = os.path.dirname(outfile)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(outfile,'w') as f:
            for i in range(len(model)):
                word=model[i][0]
                count=model[i][1]
                line=": ".join(word).encode('utf-8')
                if Total and i==len(model)-1:
                    f.write(line+"Overall: " +str(count) +"\n")
                else:
                    f.write(line+": " +str(count) +"\n")
        return
