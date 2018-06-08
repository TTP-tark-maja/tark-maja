#fixed price function
import datetime
import time

fixedPriceNight = 2,5 
fixedPriceDay = 7,5 #measured in  kWH

NumberOfHooursUse = 0
NumberOfDaysUse = 0
WattsUsed = 0


def daylightSavingsTime():
    daylightTime = time.daylight and time.localtime().tm_isdst > 0
    if daylightTime == True:
        If #DayTime:
            #time is 
        
    else:
        nightTime = #kella 
           
    print(daylightTime)
    
    
def timeOfWeek():  #function to see if its weekday or weekend
    dayNr = datetime.datetime.today().weekday()
    if dayNr<5:
        print ('Weekday')
    else:
        print ('Weekend')
        
def fixedPrices():
    daylightSavingsTime()
    timeOfWeek()
    
    

    #[number of  hours’ use] x ([capacity of appliance expressed in watt] / 1,000) = number of kWh

fixedPrices()    

    
