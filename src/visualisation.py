# -*- coding: utf-8 -*-
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
from collections import defaultdict
import numpy as np

class Visualization():
    
    def __init__(self):
        return

    def findKeywords(self,data, wordLimit):
        # datetime -> word record -> word,score list/datetime (-> word/score)
        d = defaultdict(list)
        for wordfile in data:
            for reocrd in wordfile[:2]: # Get top 2 words from scores in each date
                d[reocrd[0][0]].append(float(reocrd[0][1]))
        if(len(d)>wordLimit):
            percentile=(1-(wordLimit/float(len(d))))*100
            interestScore=np.percentile(np.array([max(d[k]) for k,v in d.items()]),percentile)
            return [k for k,v in d.items() if max(d[k])>interestScore]
        return [k for k,v in d.items()]

    def grepTrendPoints(self,word,trend):
        # word data structure:
        # datetime -> word record -> word,score list/datetime (-> word/score)
        # Target: return a dict of:
        # word1 [0.0, 0.03,......0.2]
        point=[]
        for table in trend:
            tmp=[]
            for record in table:
                if record[0][0]==word:
                    tmp.append(float(record[0][1]))
            if tmp:
                point.append(tmp[0])
            else:
                point.append(0.0)
        return (word, point)

    def getTrace(self,interest,time):
        trace=[]
        for a in range(len(interest)):
            trace.append(go.Scatter(
                mode='lines+markers',
                x=[i for i in time],
                y=interest[a][1],
                name = interest[a][0],
                connectgaps=True,
                line = dict(
                    shape = 'spline')
                )
            )
        layout = dict(
            title = 'News Trend from '+str(time[0])+" to "+str(time[len(time)-1]),
            yaxis = dict(title = 'Importance Index'),
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=7,
                             label='1w',
                             step='day',
                             stepmode='backward'),
                        dict(count=1,
                             label='1m',
                             step='month',
                             stepmode='backward'),
                        dict(count=6,
                             label='6m',
                             step='month',
                             stepmode='backward'),
                        dict(count=1,
                            label='YTD',
                            step='year',
                            stepmode='todate'),
                        dict(count=1,
                            label='1y',
                            step='year',
                            stepmode='backward'),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(),
                type='date'
            )
        )
        fig=dict(data=trace,layout=layout)
        return fig

    def heatmap(self,fileName, startdate, category):
        infile = open(fileName)
        data = [line.decode('utf-8').split(": ") for line in infile]
        socre = [[float(x) for x in (str(x[1]).replace("[","").replace("]","").replace("\n","").split(","))]
                 for x in data][::1]
        topics = ["Topic_"+str(i) for i in range(len(socre[0]))][::1]
        keys = [x[0] for x in data][::1]
        data = [
            go.Heatmap(
                z= zip(*socre),
                x=keys,
                y=topics,
                colorscale='Viridis',
            )
        ]

        layout = go.Layout(
            title=category+' News Topics since '+startdate,
            xaxis = dict(ticks=''),
            yaxis = dict(ticks='')
        )
        fig = go.Figure(data=data, layout=layout)
        return fig
    
    def sentimentTrend(self,data,chartTitle):
        trace=[]
        labels=['實用', '感人', '開心','有趣', '無聊', '害怕','難過', '憤怒']
        x_data=map(lambda k: [float(elem) for elem in k],[s[-1][0][2].replace("[","").replace("]","").split(",") for s in data])
        # Normalize elements in list such that the sum of all sentiments equals to 1
        x_data=map(lambda k: [elem/sum(k) for elem in k],x_data)
        y_data=[date[-1][1] for date in data]
        for i in range(len(labels)):
            trace.append(go.Bar(
                x=[e[i] for e in x_data],
                y=y_data[::1],
                name=labels[i],
                orientation='h',
                opacity=0.8,
             ))

        layout = go.Layout(
            barmode='stack',
            title= chartTitle
            )
        fig = go.Figure(data=trace, layout=layout)
        return fig
    
    def stackWordCount(self,data,xaxisName,yaxisName,titleName): 
        d = defaultdict(list)
        for i in range(len(data)):
            date=data[i][0][1]
            for record in data[i]:
                d[record[0][0]].append((float(record[0][1]),record[1]))
            for k,v in d.items():
                if len(d[k])<=i:
                    for j in range(i-len(d[k])+1):
                        d[k].append((0.0,date))
        summed = {k: sum([x[0]for x in v]) for (k, v) in d.items()}
        sort_summed = sorted(summed.iteritems(),key=lambda (k,v): v,reverse=True)[:20]
        trace=[]
        # key is for get daytime
        key=sort_summed[0][0]
        for i in range(len(data)):
            trace.append(go.Bar(
                x=[k for k,v in sort_summed],
                y=[d[k][i][0] if(len(d[k])>=i+1) else 0.0 for k,v in sort_summed],
                name=d[key][i][1],
                opacity=0.7
            )
        ) 
        layout = go.Layout(
        barmode='stack',
        yaxis = dict(title = yaxisName),
        xaxis = dict(title = xaxisName),
        title= titleName
        )
        fig = go.Figure(data=trace, layout=layout)
        return fig
    
    def searchNews(self,headlines,keyWords):
        filter_keyWords=[]
        for record in headlines:
            tmp=[]
            for word in keyWords:
                if word in record[0]:
                    tmp.append(word)
            if(tmp):
                filter_keyWords.append(tmp)
        filter_headlines = [record for record in headlines if (any(word in record[0] for word in keyWords)) ]
        data_matrix = [['News Headline','Key words']]
        for key,record in sorted(zip(filter_keyWords,filter_headlines)):
            data_matrix.append(['<a href="'+record[1]+'">'+record[0]+'</a>'," ".join(key)])
        table = FF.create_table(data_matrix)
        return table
    
    def freqCount(self,data,wordLimit,xaxisName,yaxisName,title):
        trace1 = go.Bar(
            y=[row[0] for row in data[:wordLimit]][::-1],
            x=[row[1][0] for row in data[:wordLimit]][::-1],
            name=data[0][1][1],
            orientation = 'h',
            marker = dict(
                color = 'rgba(55, 128, 191, 0.6)',
                line = dict(
                    color = 'rgba(55, 128, 191, 1.0)',
                    width = 1,
                )
            )
        )
        data = [trace1]
        layout = go.Layout(
            barmode='stack',
            yaxis = dict(title = yaxisName),
            xaxis = dict(title = xaxisName),
            title = title
        )
        fig = go.Figure(data=data, layout=layout)
        return fig