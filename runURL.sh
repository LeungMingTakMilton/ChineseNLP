# SRC_PATH=$1
# MODEL_PATH=$2
# IN_FILE=$3
# TEMP_PATH=$4
# OUT_PATH=$5

SRC_PATH="./src/"
MODEL_PATH="./model/"
IN_URL=$1
TEMP_PATH="./data/tmp/"
OUT_PATH="./data/output/"
IN_PATH="./data/input/"

IN_FILE=$IN_PATH/article.txt

#TEMP FILE
CLEAN_PATH=$TEMP_PATH/clean.txt
SEGMENT_PATH=$TEMP_PATH/segment.txt
TOKEN_PATH=$TEMP_PATH/tokens.txt

# OUTPUT PATHECTORY
FREQ_PATH_WORDS=$OUT_PATH/freq.txt
BIGRAM_PATH=$OUT_PATH/bigram.txt
TRIGRAM_PATH=$OUT_PATH/trigram.txt
TFIDF_PATH=$OUT_PATH/score.txt
TOPICS_PATH=$OUT_PATH/topics.txt

echo "python $SRC_PATH/crawl.py $IN_URL $IN_FILE"
python $SRC_PATH/crawl.py $IN_URL $IN_FILE
echo "python $SRC_PATH/01-clean.py $IN_FILE $CLEAN_PATH"
python $SRC_PATH/01-clean.py $IN_FILE $CLEAN_PATH
echo "python $SRC_PATH/02-segment.py $CLEAN_PATH $SEGMENT_PATH $MODEL_PATH/user_dict.txt"
python $SRC_PATH/02-segment.py $CLEAN_PATH $SEGMENT_PATH $MODEL_PATH/user_dict.txt
echo "python $SRC_PATH/03-filter.py $SEGMENT_PATH $TOKEN_PATH"
python $SRC_PATH/03-filter.py $SEGMENT_PATH $TOKEN_PATH
echo "python $SRC_PATH/04a-ngram.py $TOKEN_PATH $FREQ_PATH_WORDS $BIGRAM_PATH $TRIGRAM_PATH"
python $SRC_PATH/04a-ngram.py $TOKEN_PATH $FREQ_PATH_WORDS $BIGRAM_PATH $TRIGRAM_PATH
echo "python $SRC_PATH/04b-tfidf.py $TOKEN_PATH $TFIDF_PATH $MODEL_PATH/tfidf_dict.txt"
python $SRC_PATH/04b-tfidf.py $TOKEN_PATH $TFIDF_PATH $MODEL_PATH/tfidf_dict.txt
echo "python $SRC_PATH/04c-topics.py $TOKEN_PATH $TOPICS_PATH"
python $SRC_PATH/04c-topics.py $TOKEN_PATH $TOPICS_PATH
