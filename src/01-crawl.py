import sys
import getopt
from util.crawler import *

isUrl = False
opts, args = getopt.getopt(sys.argv[1:], 'u')

infile = args[0]
outfile = args[1]

for o, a in opts:
    if o in ("-u","--url"):
        isUrl = True
    else :
        assert False, "unhandled option"
        
if(isUrl):
    text=Crawler().loadFromWeb(infile)
else:
    text=Crawler().loadFromFile(infile)
    
Crawler().save(outfile,text)