import time
import datetime
import urllib.request, json
import os
from datetime import date, timedelta
import matplotlib.pyplot as plt
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
    with open('todaydata.txt', 'r') as pricesList, open('workingtimes.txt','r') as workingTimes, open('notworkingtimes.txt','r') as notWorkingTimes:
        for line in pricesList:
            #taking the times and prices from todaydata.txt and making a linegraph
            a, b, c = line.split('"')
            priceA = float(a) #a - taking the prices from todays data
            timeB = b #b - taking the dates from todays data
            timeB = timeB.replace("T", " ")
            timeB = datetime.datetime.strptime(timeB , "%Y-%m-%d %H:%M:%S")
            d, e = str(timeB).split(" ")
            
            price.append(priceA)                                               
            #time.append(e)
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

    workline = [55 for aeg in workingtimes]
    endline = [55 for aeg in workingtimes]
    red_patch = mpatches.Patch(color='red', label='Device ended working')
    green_patch = mpatches.Patch(color='green', label='Device started working')
    
    plt.plot(time, price)
    plt.scatter(workingtimes, workline, color='green')
    plt.scatter(notworkingtimes, endline, color='red')
    plt.xlabel("time(date, hour)")
    plt.ylabel("Electricity price(€/MWh)")
    plt.title("Today's electricity prices(24h), includes device's Working timetable")
    plt.gcf().autofmt_xdate()
    plt.legend(handles=[green_patch, red_patch])
    plt.show()
    
visulize_timedata()

