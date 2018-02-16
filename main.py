# -*- coding: utf-8 -*-
import sys
from flask import Flask, request
from src.util.crawler import *
from src.util.normalize import *
from src.util.model_key import *
from src.util.model_sentiment import *
', '.join([w for w in jieba.cut('Hello world')])
tfidfModelPath="./model/tfidf_dict.txt"
n=Normalize()
m=KeyModel(tfidfModelPath)
m.setTopic(6)
m.doc_num=227364
app = Flask(__name__)

def analyse(url):
	toString=lambda x:x[0]+' '+str(x[1])
	# url=request.json['url']
	raw=Crawler().loadFromWeb(url)
	token_zh=n.translate(n.clean(n.seperateLines([raw])))
	documents=n.removeStopWords(n.segment(token_zh))
	ngrams=[m.ngrams(documents,i+1) for i in range(3)]
	score=m.tfidf(documents)
	topics=m.topics(documents)
	# topic1'\n'.join(map(toString,topics))
	# tfidf: '\n'.join(map(toString,score))
	# trigram: '\n'.join(map(toString,ngrams[2]))
	# topic2: '\n\n'.join(['\n'.join(map(lambda x:x[0]+' '+str(x[1][idx]),tags[idx])) for idx in range(6)])
	tags=[filter(lambda x:x[1][idx]!=0,topics) for idx in range(len(topics[0][1]))]
	highlight_text=reduce(lambda x,y:x.replace(y[0][0],'<b style=\'background-color:'+y[1]+'\'>'+y[0][0]+'</b>'),
		zip(reduce(lambda a,b:a+b,tags[:min(len(topics[0][1]),3)]),['#F1948A']*len(tags[0])+['#82E0AA']*len(tags[1])+['#85C1E9']*len(tags[2])),raw)

	return highlight_text +'<p>'+'<p>'.join(['<br>'.join(map(lambda x:x[0]+' '+str(x[1][idx]),tags[idx])) for idx in range(len(topics[0][1]))])

@app.route('/api/nlp', methods=['GET'])
def get():
	url=request.args.get('url')
	return analyse(url)

@app.route('/api/nlp', methods=['POST'])
def post():
	url=request.json['url']
	return analyse(url)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
