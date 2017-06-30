
# coding: utf-8

import plotly.tools as tls
import plotly.plotly as py
import datetime
import getopt
import sys
from src.visualisation import *
from plotly.offline import plot

def usage():
    print """
          usage:
          python plot.py [-l] date category
          """
    return 

def grepData(start,end,filePath):
    data=[]
    startDate=start
    endDate=end
    while(start<=end):
        year=start.year
        month=start.month
        day=start.day
        path=filePath.replace("YYYY",str(year))
        path=path.replace("MM",str(month) if month>9 else'0'+str(month))
        path=path.replace("DD",str(day) if day>9 else'0'+str(day))
        with open(path) as f:
            data.append([(line.split(": "),start) for line in f])
        start=start+datetime.timedelta(days=1)
    return data

isLocal=False
try:
    lontOpts=["local"]
    opts, args = getopt.getopt(sys.argv[1:],'l',lontOpts)
except getopt.GetoptError as err:
    print str(err) 
    usage()
    sys.exit(2)
    
for o, a in opts:
    if o in ("-l","--local"):
        isLocal = False
    else :
        assert False, "unhandled option"

v=Visualization()
tls.set_credentials_file(username='mingtak', api_key='y08kzntdko')

retrieval_datetime=args[0]
category=args[1]
year=retrieval_datetime.split("/")[0]
month=retrieval_datetime.split("/")[1]
day=retrieval_datetime.split("/")[2]
now=datetime.date(int(year), int(month), int(day))
oneMonthBefore=now-datetime.timedelta(days=30)
oneWeekBefore=now-datetime.timedelta(days=7)

weekly_trend_score_path="./data/output/YYYY/MM/DD/1weeks/rthk_data/"+category+"/score"
weekly_trend_sentiment_path="./data/output/YYYY/MM/DD/1weeks/rthk_data/"+category+"/sentiment"
weekly_topics_path="./data/output/"+year+"/"+month+"/"+day+"/1weeks/rthk_data/"+category+"/topics"
monthly_topics_path="./data/output/"+year+"/"+month+"/"+day+"/1months/rthk_data/"+category+"/topics"
daily_freq_path="./data/output/"+year+"/"+month+"/"+day+"/1days/rthk_data/"+category+"/freq"
daily_bigram_path="./data/output/"+year+"/"+month+"/"+day+"/1days/rthk_data/"+category+"/bigram"
daily_trigram_path="./data/output/"+year+"/"+month+"/"+day+"/1days/rthk_data/"+category+"/trigram"
daily_score_path="./data/output/"+year+"/"+month+"/"+day+"/1days/rthk_data/"+category+"/score"
daily_sentiment_path="./data/output/"+year+"/"+month+"/"+day+"/1days/rthk_data/"+category+"/sentiment"

output_news_trend=category.title()+" News Trend"
output_news_topics_monthly=category.title()+" News Topics Monthly"
output_news_topics_weekly=category.title()+" News Topics Weekly"
output_news_sentiment_monthly=category.title()+" News Sentiment"
output_news_freq_daily="Daily Freq "+category.title()
output_news_bigram_daily="Daily Bigram "+category.title()
output_news_trigram_daily="Daily Trigram "+category.title()
output_news_score_weekly=category.title()+" Weekly Key Words"
output_news_headline_daily=category.title()+" News Headline"

# data=grepData(datetime.date(2016, 2, 1),now,weekly_trend_score_path)
data=grepData(datetime.date(2017, 4, 30),now,weekly_trend_score_path)
wordSet=v.findKeywords(data,15)
points=[v.grepTrendPoints(word,data) for word in wordSet]
fig=v.getTrace(points,[d[0][1] for d in data])
if(isLocal):
    plot(fig,filename=output_news_trend,auto_open=False)
else:
    py.plot(fig,filename=output_news_trend,auto_open=False)

fig_heatmap = v.heatmap(monthly_topics_path,str(oneMonthBefore),category.title())
if(isLocal):
    plot(fig_heatmap,filename=output_news_topics_monthly,auto_open=False)
else:
    py.plot(fig_heatmap,filename=output_news_topics_monthly,auto_open=False)

fig_heatmap = v.heatmap(weekly_topics_path,str(oneWeekBefore),category.title())
if(isLocal):
    plot(fig_heatmap,filename=output_news_topics_weekly,auto_open=False)
else:
    py.plot(fig_heatmap,filename=output_news_topics_weekly,auto_open=False)

# sentiment_data=grepData(datetime.date(2016, 3, 12),now,weekly_trend_sentiment_path)
# sentiment_data=grepData(datetime.date(2017, 3, 23),now,weekly_trend_sentiment_path)
sentiment_data=grepData(datetime.date(2017, 4, 30),now,weekly_trend_sentiment_path)
if(isLocal):
    plot(v.sentimentTrend(sentiment_data,"Monthly news sentiment"),filename=output_news_sentiment_monthly,auto_open=False)
else:
    py.plot(v.sentimentTrend(sentiment_data,"Monthly news sentiment"),filename=output_news_sentiment_monthly,auto_open=False)

infile = open(daily_freq_path)
freq_data = ([(line.split(": ")[0],(int(line.split(": ")[1]),now)) for line in infile])
fig=v.freqCount(freq_data,15,"Word Count",'','')
if(isLocal):
    plot(fig,filename=output_news_freq_daily,auto_open=False)
else:
    py.plot(fig,filename=output_news_freq_daily,auto_open=False)

infile = open(daily_bigram_path)
freq_data = ([(line.split(": ")[0],(int(line.split(": ")[1]),now)) for line in infile])
fig=v.freqCount(freq_data,15,"Word Count",'','')
if(isLocal):
    plot(fig,filename=output_news_bigram_daily,auto_open=False)
else:
    py.plot(fig,filename=output_news_bigram_daily,auto_open=False)

infile = open(daily_trigram_path)
freq_data = ([(line.split(": ")[0],(int(line.split(": ")[1]),now)) for line in infile])
fig=v.freqCount(freq_data,15,"Word Count",'','')
if(isLocal):
    plot(fig,filename=output_news_trigram_daily,auto_open=False)
else:
    py.plot(fig,filename=output_news_trigram_daily,auto_open=False)

stack_keydata=grepData(oneWeekBefore,now,weekly_trend_score_path)
fig=v.stackWordCount(stack_keydata,"Words","Importance Index","Weekly key words")
if(isLocal):
    plot(fig,filename=output_news_score_weekly,auto_open=False)
else:
    py.plot(fig,filename=output_news_score_weekly,auto_open=False)

infile = open(daily_sentiment_path)
infile1 = open(daily_score_path)
headlines = [record.split(": ") for record in infile]
keyWords =[record.split(": ")[0] for record in infile1][:5]
table=v.searchNews(headlines,keyWords)
if(isLocal):
    plot(table,filename=output_news_headline_daily,auto_open=False)
else:
    py.plot(table,filename=output_news_headline_daily,auto_open=False)
