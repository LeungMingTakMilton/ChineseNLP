import sys
import unicodedata


# Check if a word is all CJK characters
def isCJK(w):
    if not w.isalpha():
        return False
    for c in w:
        n = unicodedata.name(unicode(c))
        if not n.startswith("CJK"):
            return False
    return True

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
    line = line.split(" ")
    for w in line:
        # if condition is to remove a single Chinese character
        # TODO: Add a dynamic filter function to handle unicode
        if len(w)>5:
                tokens.append(w.strip().rstrip())
    texts.append(tokens)

# remove empty sentence and write to resultant string
result=""
for line in texts:
    tokens=""
    if line:
        for word in line:
            tokens+=word+" "
        result=result+tokens.rstrip()+"\n"
    
with open(outputfile,'w') as f:
    f.write(result)