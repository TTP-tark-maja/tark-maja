import time
import datetime
import urllib.request, json
import os
from datetime import date, timedelta
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

        for i in range (21, 46) :
            eestiajad =(eesti[i])
            kellaaeg = (eestiajad['timestamp'])
            price = (eestiajad['price'])
            time = datetime.datetime.fromtimestamp(kellaaeg).isoformat()
            json.dump(price, outfile)
            json.dump(time, outfile)
            outfile.write('\n')
