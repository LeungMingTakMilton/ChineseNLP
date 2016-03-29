import jieba
import sys
import unicodedata


# Check if a word is all characters, including Chinese and English
def isCharacter(w):
    if not w.isalpha():
        return False
    return True


inputfile = str(sys.argv[1])
outputfile = str(sys.argv[2])
userdict = str(sys.argv[3])

jieba.load_userdict(userdict)

content=[]

with open(inputfile) as f:
    for line in f:
        content.append(line)
        
# loop through document list
texts=[]
for i in content:
    # clean and tokenize document string
    tokens=[]
    for w in jieba.cut(i):
#         print w
#         if len(w)>1:
#             if isCharacter(w):
                tokens.append(w.strip())
    texts.append(tokens)

with open(outputfile,'w') as f:
    docs=""
    for token in texts:
        line=""
        for word in token:
            line+=word.encode('utf-8')+" "
        docs=docs+line.rstrip()+"\n"
    f.write(docs)