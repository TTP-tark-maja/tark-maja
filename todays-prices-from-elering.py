import time
import datetime
import urllib.request, json

#Päringu saime https://dashboard.elering.ee/documentation.html lehelt.
with urllib.request.urlopen("https://dashboard.elering.ee/api/nps/price?start=&end=") as url:
    #võtab eleringist stringina tänased hinnad
    jsonstring = json.loads(url.read().decode())
    data =(jsonstring['data'])
    eesti = data['ee']
    #kirjutab andmed faili    
    with open('todaydata.txt', 'w') as outfile:
        
        for i in range (0, 12) :
            eestiajad =(eesti[i])
            kellaaeg = (eestiajad['timestamp'])
            price = (eestiajad['price'])
            time = datetime.datetime.fromtimestamp(kellaaeg).isoformat()
            json.dump(price, outfile)
            json.dump(time, outfile)
            outfile.write('\n')

