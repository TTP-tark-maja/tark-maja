fm = open("todaydata.txt")
for rida in fm:
    if(len(rida)==27):
        print (float(rida[:5]))
    elif(len(rida)==26):
         print(float(rida[:4]))
    elif(len(rida)==24):
        print(float(rida[:2]))
fm.close
vaartus = 48
