from datetime import date
today = str(date.today())
print(today)
import time
import datetime
import urllib.request, json
import os
import pytz


today = str(date.today())
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow1 = tomorrow.strftime('%Y-%m-%d')
text = 'https://dashboard.elering.ee/api/nps/price?start='
text2 = '&end='
#Päringu saime https://dashboard.elering.ee/documentation.html lehelt.
with urllib.request.urlopen(text+today+text2+tomorrow1) as url:
    #võtab eleringist stringina tänased hinnad
    jsonstring = json.loads(url.read().decode())
    data =(jsonstring['data'])
    eesti = data['ee']
    #kirjutab andmed faili    
    with open('todaydata.txt', 'w') as outfile:

        now = datetime.datetime.now()

        for i in range (0, 22) :
            eestiajad =(eesti[i])
            kellaaeg = (eestiajad['timestamp'])
            price = (eestiajad['price'])
            time = datetime.datetime.fromtimestamp(kellaaeg).isoformat()
            json.dump(price, outfile)
            json.dump(time, outfile)
            outfile.write('\n')
