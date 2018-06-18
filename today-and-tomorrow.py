import time
import datetime
import urllib.request, json
import os
from datetime import date, timedelta

#modules for graphs
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pylab as plt
import matplotlib.patches as mpatches

today = str(date.today())
yesterday = str(date.today() - timedelta(1))
#print(yesterday)
#print(today)

today = str(date.today())
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow1 = tomorrow.strftime('%Y-%m-%d')
yesterday = date.today() - timedelta(1)
yesterday1 = yesterday.strftime('%Y-%m-%d')
text = 'https://dashboard.elering.ee/api/nps/price?start='
text2 = '&end='
#Päringu saime https://dashboard.elering.ee/documentation.html lehelt.
with urllib.request.urlopen(text+yesterday1+text2+tomorrow1) as url:
    #print(text+yesterday1+text2+tomorrow1)
    #võtab eleringist stringina tänased hinnad
    jsonstring = json.loads(url.read().decode())
    data =(jsonstring['data'])
    eesti = data['ee']
    #kirjutab andmed faili    
    with open('todaydata.txt', 'w') as outfile:

        now = datetime.datetime.now()

        for i in range (21, 45) :
            eestiajad =(eesti[i])
            kellaaeg = (eestiajad['timestamp'])
            price = (eestiajad['price'])
            time = datetime.datetime.fromtimestamp(kellaaeg).isoformat()
            json.dump(price, outfile)
            json.dump(time, outfile)
            outfile.write('\n')


def splitPrices():
    #function that splits prices into cheap and expensive lists according to average
    cheapPricesList = []
    expensivePricesList = []
    total_sum = 0
    with open('todaydata.txt', 'r') as pricesList:
        for line in pricesList:
            count = len(open('todaydata.txt').readlines(  ))
            a, b, c = line.split('"')
            number = float(a)
            total_sum += number
            avg = total_sum/count
    pricesList.close()
    with open('todaydata.txt', 'r') as pricesList: 
        for line in pricesList:
            a, b, c = line.split('"')
            number = float(a)
            time = b
            time = time.replace("T", " ")
            time = datetime.datetime.strptime(time , "%Y-%m-%d %H:%M:%S")
            if (number < avg):
                cheapPricesList.append(time)
            else:            
                expensivePricesList.append(time)
                
            
        print("Cheap: ")
        print(cheapPricesList)

        print("Expensive: ")
        print(expensivePricesList)


def visulize_timedata():
    #function that visulizes todays data as a linegraph
    #must install Matplotlib
    price = []
    time = []
    workingtimes = []
    notworkingtimes = []
    annotation = []
    with open('todaydata.txt', 'r') as pricesList, open('WorkingTimes.txt','r') as workingTimes, open('WorkingOfftimes.txt','r') as notWorkingTimes, open('clientData.txt','r') as fixedPriceslist:
        if(fixedPricesList.readlines() == "Fikseeritud"):
            for line in fixedPricesList:
                fprices = fixedPricesList.readlines()
                print(fprices)
                
        else:
            for line in pricesList:
                #taking the times and prices from todaydata.txt and making a linegraph
                a, b, c = line.split('"')
                priceA = float(a) #a - taking the prices from todays data
                timeB = b #b - taking the dates from todays data
                timeB = timeB.replace("T", " ")
                timeB = datetime.datetime.strptime(timeB , "%Y-%m-%d %H:%M:%S")
                d, e = str(timeB).split(" ")
                        
                price.append(priceA)                                               
                time.append(timeB)            		
			
        for line in workingTimes:                
            #taking the times from workingtimes.txt and adding them to the table as dots
            timeB2 = datetime.datetime.strptime(line.strip() , "%Y-%m-%d %H:%M:%S")
            f, g = line.split(' ')
            timeG = g #g - taking the times from working times
            #workingtimes.append(timeG)
            workingtimes.append(timeB2)
            
        for line in notWorkingTimes:
            #taking the times from notworkingtimes.txt and adding them to the table as dots
            timeB3 = datetime.datetime.strptime(line.strip() , "%Y-%m-%d %H:%M:%S")
            h, i = line.split(' ')
            timeI = i #i - taking the times from not working times
            notworkingtimes.append(timeB3)

    workline = [45 for aeg in workingtimes]										#ajagraafiku osa
    endline = [45 for aeg in workingtimes]										#ajakraafiku osa
    red_patch = mpatches.Patch(color='red', label='Device ended working')		#legend
    green_patch = mpatches.Patch(color='green', label='Device started working')	#legend
    
    plt.plot(time, price)
    plt.scatter(workingtimes, workline, color='green') 							#ajakraafiku osa
    plt.scatter(notworkingtimes, endline, color='red') 							#ajakraafiku osa	
    plt.xlabel("time(date, hour)")
    plt.ylabel("Electricity price(€/MWh)")
    plt.title("Today's electricity prices(24h), includes device's Working timetable")
    plt.gcf().autofmt_xdate()
    plt.legend(handles=[green_patch, red_patch])								#legend
    savefig('24h.png')															#pilt
    #plt.show()
    
visulize_timedata()


def visulize_timedata_fixed():
    fixedPrices = []
    time = []
    with open('clientData.txt','r') as fixedPriceslist, open('todaydata.txt', 'r') as pricesList:	         
        for line in pricesList:                    #taking the times from todaydata.txt
            a, b, c = line.split('"')
            timeB = b #b - taking the dates from todays data
            timeB = timeB.replace("T", " ")
            timeB = datetime.datetime.strptime(timeB , "%Y-%m-%d %H:%M:%S")
            d, e = str(timeB).split(" ")			
            time.append(timeB)            

        for line in fixedPriceslist:
            lines = fixedPricesList.readlines()
            fPrice = float(lines) #a - taking the prices from clientData.txt					
            price.append(fPrice)                                                         	

