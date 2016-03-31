import sys
import unicodedata


# Check if a word is all CJK characters
def isCJK(w):
    return all(u'\u4e00' <= c <= u'\u9fff' for c in w.decode('utf-8'))

inputfile = str(sys.argv[1])
outputfile = str(sys.argv[2])

content=[]

with open(inputfile) as f:
    for line in f:
        content.append(line)
        
# loop through document list
texts=[]
for line in content:
    # clean and tokenize document string
    tokens=[]
    for w in line.split(" "):
        # Assume all stop words are single Chinese characters
        # TODO: replace hard coded length to stop words 
        tmp = w.rstrip()
        # special condition for building news, to be remove after 
        # 1 April 2016
        if (tmp.startswith('-') or tmp.endswith('-') or tmp.endswith(':')):
              tokens.append(w.strip().rstrip())            
        elif w.isalnum() and len(w)>3:
              tokens.append(w.strip().rstrip())
        elif len(w)>5:
              tokens.append(w.strip().rstrip())            
    texts.append(tokens)

# remove empty sentence and write to resultant string
result=""
for line in texts:
    tokens=""
    # if line:
    for word in line:
        tokens+=word+" "
    result=result+tokens.rstrip()+"\n"
    
with open(outputfile,'w') as f:
    f.write(result)