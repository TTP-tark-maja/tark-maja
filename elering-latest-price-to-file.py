import urllib.request, json 
#Päringu saime https://dashboard.elering.ee/documentation.html lehelt.
with urllib.request.urlopen("https://dashboard.elering.ee/api/nps/price/ee/latest") as url:
    data = json.loads(url.read().decode())
    print(data)
    
with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
