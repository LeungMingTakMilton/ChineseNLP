arg=$1
if [ "$arg" == "-u" ]
then
    IN_FILE=$2
    URLflag=true
else
    URLflag=false
    IN_FILE=$1
fi

SRC="./src/"
MODEL="./model/"
TEMP="./data/tmp/"
OUT="./data/output/"
IN="./data/input/"

# INPUT_FILE
RAW=$IN/article.txt

# TEMP FILE
CLEAN=$TEMP/clean.txt
SEGMENT=$TEMP/segment.txt
TOKEN=$TEMP/tokens.txt

# OUTPUT FILE
FREQ_WORDS=$OUT/freq.txt
BIGRAM=$OUT/bigram.txt
TRIGRAM=$OUT/trigram.txt
TFIDF=$OUT/score.txt
TOPICS=$OUT/topics.txt
SENTIMENT=$OUT/sentiment.txt

# MODEL FILE
MODEL_TFIDF=$MODEL/tfidf_dict.txt
MODEL_DOC2VEC=$MODEL/model_news.d2v
MODEL_LR=$MODEL/sentiment.lm

if [ $URLflag == "true" ]
then
    echo "python $SRC/01a-crawl.py $IN_FILE $RAW"
    python $SRC/01a-crawl.py $IN_FILE $RAW
    IN_FILE=$RAW
fi
echo "python $SRC/01-clean.py $IN_FILE $CLEAN"
python $SRC/01-clean.py $IN_FILE $CLEAN
echo "python $SRC/02-segment.py $CLEAN $SEGMENT"
python $SRC/02-segment.py $CLEAN $SEGMENT
echo "python $SRC/03-filter.py $SEGMENT $TOKEN"
python $SRC/03-filter.py $SEGMENT $TOKEN
echo "python $SRC/04d-sentiment.py $CLEAN $TOKEN $SENTIMENT $MODEL_DOC2VEC $MODEL_LR &"
python $SRC/04d-sentiment.py $CLEAN $TOKEN $SENTIMENT $MODEL_DOC2VEC $MODEL_LR &
echo "python $SRC/04a-ngram.py $TOKEN $FREQ_WORDS $BIGRAM $TRIGRAM &" 
python $SRC/04a-ngram.py $TOKEN $FREQ_WORDS $BIGRAM $TRIGRAM &
echo "python $SRC/04b-tfidf.py $TOKEN $TFIDF $MODEL_TFIDF &"
python $SRC/04b-tfidf.py $TOKEN $TFIDF $MODEL_TFIDF &
echo "python $SRC/04c-topics.py $TOKEN $TOPICS &"
python $SRC/04c-topics.py $TOKEN $TOPICS &
wait
