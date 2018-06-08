import time
import urllib.request, json 
#Päringu saime https://dashboard.elering.ee/documentation.html lehelt.
with urllib.request.urlopen("https://dashboard.elering.ee/api/nps/price/ee/latest") as url:
    #võtab eleringist stringina viimase hinna ja kuupäeva
    jsonstring = json.loads(url.read().decode())
    data =(jsonstring['data'])
    string = data[0]
    time = time.ctime(string['timestamp'])
    price = string['price']
    print(time)
    print(price)

#kirjutab andmed faili    
with open('data.txt', 'w') as outfile:  
    json.dump(time, outfile)
    json.dump(', '+price, outfile)
