# ChineseNLP
NLP Engine that supports keyword extraction, topic modelling and sentiment analysis

## 1. Installation
```bash
pip install -r requirements.txt
```
## 2. run.py usage
```bash
python run.py [-l|-n|-s|-t|-u] [input file] [outputPath]
```
Find files in data/output/ after execution

## 3. Example
a. Extract key topics and most common words from a document:
```bash
python run.py -lnt data/input/essay data/output/essay/
```
b. Extract key topics and most common words from url:
```bash
python run.py -lnstu https://theinitium.com/article/20160309-dailynews-alphago/ data/output/essay/
```
c. Building key topics and sentiment model from rthk local and international news
```bash
python sql.py -c local,international rthk_data 2016/01/01 2016/04/01 data/output/news
```
d. Building key topics and sentiment model from fso blog
```bash
python sql.py fso_blog_data 2016/01/01 2016/04/01 data/output/fso_blog
```
e. Building key topics and sentiment model from ceo blog
```bash
python sql.py ceo_blog_data 2016/01/01 2016/04/01 data/output/ceo_blog
```

## 4. Option Description
### ngrams and frequency count
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

### latent semantic indexing (LSI)
option: -l
output file: topics
file format:
_[key word 1]: [score1, score2, score3, score4, score5, score6]
[key word 2]: [score1, score2, score3, score4, score5, score6]
...
[key word n]: [score1, score2, score3, score4, score5, score6]

sorted by score1, followed by score2, score3 ... and score6 in desending order

### sentiment format

file format
[article_1]: [url1]: [s1,s2,s3,s4,s5,s6,s7,s8]
[article_2]: [url2]: [s1,s2,s3,s4,s5,s6,s7,s8]
[article_3]: [url3]: [s1,s2,s3,s4,s5,s6,s7,s8]
...
Overall: [s1,s2,s3,s4,s5,s6,s7,s8]

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

## 5. sql.py usage
```bash
python sql.py [-c category] [table] [start yyyy/mm/dd] [end yyyy/mm/dd] [output path]
```
## 6. qurey.sh usage
./query.sh [start date] [end date] [grep interval] [shift inerval] [table] [category (only for rthk_data)]
Example: 
```bash
./query.sh 2016/02/08 2016/04/04 1days 1days rthk_data local
./query.sh 2016/02/08 2016/04/04 1days 1days fso_blog_data
./query.sh 2016/02/08 2016/04/04 1months 1days ceo_blog_data
```
