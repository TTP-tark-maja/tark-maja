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
    with open('todaydata.txt', 'r') as pricesList:
        for line in pricesList:
            a, b, c = line.split('"')
            priceA = float(a)
            timeB = b
            timeB = timeB.replace("T", " ")
            timeB = datetime.datetime.strptime(timeB , "%Y-%m-%d %H:%M:%S")
            d, e = str(timeB).split(" ")                 
            price.append(priceA)                                               
            time.append(e)
            plt.plot(time, price)
    plt.xlabel("time(h, m, s)")
    plt.ylabel("Electricity price(€/MWh)")
    plt.title("Today's electricity prices(24h)")
    plt.show()
    
visulize_timedata()
