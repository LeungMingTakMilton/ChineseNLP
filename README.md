# ChineseNLP

## In a nutshell
1. Extract key topics and most common words from a document:
```bash
python run.py -lnst data/input/essay data/output/essay/
```
2. Extract key topics and most common words from url:
```bash
python run.py -lnstu https://theinitium.com/article/20160309-dailynews-alphago/ data/output/essay/
```
## run.py usage
```bash
python run.py [-l|-n|-s|-t|-u] [input file] [outputPath]
```

## Dependencies
gensim
jieba
sklearn
numpy
readability
BeautifulSoup

###  ngrams and frequency count
option: -n
output files: [freq bigram trigram]
file format:
[word]: [count]
...
[word]: [count]

sorted by count in descending order

###  tfidf
option: -t
output file: score
file format:
[key word]: [score]
...
[key word]: [score]

sorted by score in descending order

### latent semantic indexing (LSI)
option: -l
output file: topics
file format:
[key word]: [score1, score2, score3]
...
[key word]: [score1, score2, score3]

sorted by score1, followed by score2 and score3 in desending order
score range: [0,1]

###  sentiment analysis using doc2vec and mlr
option: -s
output file: sentiment
file format:
[sentence1]: [s1,s2,s3,s4,s5,s6,s7,s8]
[sentence2]: [s1,s2,s3,s4,s5,s6,s7,s8]
[sentence3]: [s1,s2,s3,s4,s5,s6,s7,s8]
...
Overall: [s1,s2,s3,s4,s5,s6,s7,s8]

sentiment meaning:
s1:實用	s5:無聊
s2:感人	s6:害怕
s3:開心	s7:難過 
s4:有趣	s8:憤怒

score range: [0,1]

