from datetime import datetime, timedelta, date
import urllib.request, json
import os
import datetime
#import datetime.strptime

today = str(date.today())
yesterday = str(date.today() - datetime.timedelta(1))

today = str(date.today())
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow1 = tomorrow.strftime('%Y-%m-%d')
yesterday = date.today() - datetime.timedelta(1)
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
    cheap_times = []
    expensive_times = []
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
            time = b
            time = time.replace("T", " ")
            number = float(a)
            if (number < avg):
                cheap_times.append(time)
            else:            
                expensive_times.append(time)
        print(cheap_times)
        return cheap_times, expensive_times

#lugeda failist elektriandmes
f = open("elektriandmed.txt","r")
fixed = (str((f.readline().rstrip())))
print(fixed)
print(fixed)
if(fixed == "fikseeritud"):
    cheap_times = []
    expensive_times = []
    day_price = (f.read())
    night_price = (f.read())
    delivery_price = (f.read())
    marginal_price = (f.read())
    f.close()
else:
    delivery_price = (f.read())
    marginal_price = (f.read())
    f.close()
    cheap_times, expensive_times = splitPrices()

#kasutaja sisestatud tingimused
how_many_minutes_in = 1000
how_many_minutes_out = 1600

how_many_minutes_in_at_once = 20
how_many_minutes_out_at_once = 30

which_timeperiod_in_starts1 = datetime.datetime(2015, 9, 12, 10, 9, 45)
which_timeperiod_in_ends1 = datetime.datetime(2015, 9, 12, 12, 12, 10)

which_timeperiod_in_starts2 = datetime.datetime(2015, 9, 12, 13, 9, 45)
which_timeperiod_in_ends2 = datetime.datetime(2015, 9, 12, 14, 12, 10)

which_timeperiod_in_starts3 = datetime.datetime(2015, 9, 12, 14, 20, 0)
which_timeperiod_in_ends3 = datetime.datetime(2015, 9, 12, 14, 50, 0)

which_timeperiod_in_starts4 = datetime.datetime(2015, 9, 12, 15, 9, 0)
which_timeperiod_in_ends4 = datetime.datetime(2015, 9, 12, 16, 12, 0)

which_timeperiod_out_starts1 = datetime.datetime(2015, 9, 12, 17, 0, 0)
which_timeperiod_out_ends1 = datetime.datetime(2015, 9, 12, 17, 30, 0)

which_timeperiod_out_starts2 = datetime.datetime(2015, 9, 12, 18, 9, 45)
which_timeperiod_out_ends2 = datetime.datetime(2015, 9, 12, 20, 9, 45)

which_timeperiod_out_starts3 = datetime.datetime(2015, 9, 12, 21, 9, 45)
which_timeperiod_out_ends3 = datetime.datetime(2015, 9, 12, 22, 9, 45)

which_timeperiod_out_starts4 = datetime.datetime(2015, 9, 12, 0, 0, 0)
which_timeperiod_out_ends4 = datetime.datetime(2015, 9, 12, 0, 0, 0)


max_electicity_consumption = 20
min_electicity_consumption = 10

appliance = 850

def get_input_from_file():
    #take the input form file
    with open ('conditions.txt', 'r') as userConditions:
        conditionsList = [how_many_minutes_in, how_many_minutes_out, how_many_minutes_in_at_once, how_many_minutes_out_at_once, max_electicity_consumption, min_electicity_consumption, appliance]
        conditionsList[0] = userConditions.readline()
        conditionsList[1] = userConditions.readline()
        conditionsList[2] = userConditions.readline()
        conditionsList[3] = userConditions.readline()
        conditionsList[4] = userConditions.readline()
        conditionsList[5] = userConditions.readline()
        conditionsList[6] = userConditions.readline()
        
        
    with open ('input.txt', 'r') as userInput:
        inputList = [which_timeperiod_in_starts1, which_timeperiod_in_ends1, which_timeperiod_in_starts2, which_timeperiod_in_ends2, which_timeperiod_in_starts3, which_timeperiod_in_ends3, which_timeperiod_in_starts4, which_timeperiod_in_ends4, which_timeperiod_out_starts1, which_timeperiod_out_ends1, which_timeperiod_out_starts2, which_timeperiod_out_ends2, which_timeperiod_out_starts3, which_timeperiod_out_ends3, which_timeperiod_out_starts4, which_timeperiod_out_ends4]
        inputList[0] = userInput.readline()
        inputList[1] = userInput.readline()
        inputList[2] = userInput.readline()
        inputList[3] = userInput.readline()
        inputList[4] = userInput.readline()
        inputList[5] = userInput.readline()
        inputList[6] = userInput.readline()
        inputList[7] = userInput.readline()
        inputList[8] = userInput.readline()
        inputList[9] = userInput.readline()
        inputList[10] = userInput.readline()
        inputList[11] = userInput.readline()
        inputList[12] = userInput.readline()
        inputList[13] = userInput.readline()
        inputList[14] = userInput.readline()
        inputList[15] = userInput.readline()
            
 
get_input_from_file()

def convert_min_to_hour(minutes):
    return minutes/60
    
def calculate_capacity(applience, workinghours):
    capacity = workinghours*(applience/1000)
    return capacity

def calculate_hours_from_capacity(appliance, capacity):
    hours = capacity/(appliance/1000)
    return hours

def calculate_timedifference_in_hours(starttime, endtime):
    timedifference =(endtime-starttime)
    duration_in_s = timedifference.total_seconds()
    hours = divmod(duration_in_s, 3600)[0]
    totalminutes = divmod(duration_in_s, 60)[0]
    minutes = round((totalminutes-hours*60)/6, 2)
    timedifference = hours+minutes
    return timedifference

def return_existing_workingtimes(which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3, which_timeperiod_in_starts4, which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3, which_timeperiod_in_ends4):
    if(which_timeperiod_in_starts1 is 0 and which_timeperiod_in_ends1 is 0):
        return '0'
    if(which_timeperiod_in_starts2 is 0 and which_timeperiod_in_ends2 is 0):
        return '1'
    if(which_timeperiod_in_starts3 is 0 and which_timeperiod_in_ends3 is 0):
        return '2'
    if(which_timeperiod_in_starts4 is 0 and which_timeperiod_in_ends4 is 0):
        return '3'
    if(which_timeperiod_in_starts1 is not 0 and which_timeperiod_in_ends1 is not 0):
        return '4'
    
def place_missing_times_to_plan(available_times, cheap_times, hours_needed, turn_on_at, turn_off_at):
    for x in range(1, available_times):
        cheap_times[x]=datetime.datetime.strptime(cheap_times[x] , "%Y-%m-%d %H:%M:%S")
        turn_on_at.append(cheap_times[x])
        turn_off_at.append(cheap_times[x] + timedelta(hours=hours_needed * 1.66666666667))
    return turn_on_at, turn_off_at

#kõikide aegade vahe tundides
timeIn1 = calculate_timedifference_in_hours(which_timeperiod_in_starts1, which_timeperiod_in_ends1)
timeIn2 = calculate_timedifference_in_hours(which_timeperiod_in_starts2, which_timeperiod_in_ends2)
timeIn3 = calculate_timedifference_in_hours(which_timeperiod_in_starts3, which_timeperiod_in_ends3)
timeIn4 = calculate_timedifference_in_hours(which_timeperiod_in_starts4, which_timeperiod_in_ends4)
timeOut1 = calculate_timedifference_in_hours(which_timeperiod_out_starts1, which_timeperiod_out_ends1)
timeOut2 = calculate_timedifference_in_hours(which_timeperiod_out_starts2, which_timeperiod_out_ends2)
timeOut3 = calculate_timedifference_in_hours(which_timeperiod_out_starts3, which_timeperiod_out_ends3)
timeOut4 = calculate_timedifference_in_hours(which_timeperiod_out_starts4, which_timeperiod_out_ends4)

hours_working = timeIn1 + timeIn2 + timeIn3 + timeIn4
hours_not_working = timeOut1 + timeOut2 + timeOut3 + timeOut4

#algab kontroll
def check_timedifference(starttime, endtime):
    timedifference = calculate_timedifference_in_hours(starttime, endtime)
    if(timedifference < 0):
        print("Time can not be negative")
        return False;
    elif (timedifference > 24):
        print("Time difference can not be over 24 hours")
        return False
    else:
        return True;

def check_workinghours(minutes_working, minutes_not_working, timeIn1, timeIn2, timeIn3, timeIn4, timeOut1, timeOut2, timeOut3, timeOut4):
    hours_must_be_working = convert_min_to_hour(minutes_working)
    hours_must_not_be_working = convert_min_to_hour(minutes_not_working)
    working_time_total = hours_working + hours_not_working
    
    if(hours_must_be_working !=0 and hours_working>hours_must_be_working):
        print("The working times entered are bigger than the working time allowance entered")
        return False
    if(hours_must_not_be_working !=0 and hours_not_working>hours_must_not_be_working):
        print("The shutdown times entered are bigger than the shutdown time allowance entered")
        return False
    if(working_time_total > 24):
        print("Device can not work more than 24 hours")
        return False
    else:
        print("Total working time: ")
        print(working_time_total)
        return(working_time_total)
    
def check_capacity(appliance, max_capacity, min_capacity, hours_working):
    capacity = calculate_capacity(appliance, hours_working)
    maxcapacity = calculate_capacity(appliance, 24)
    if(capacity>max_capacity):
        print('Entered working timees are crossing the capacity limit entered')
        return False
    if(maxcapacity<min_capacity):
        print('The minimum capacity can not be reached by your device')
        return False
    else:
        missing_capacity = min_capacity - capacity
        print('missing')
        print(missing_capacity)
        return(missing_capacity)
    
def check_if_hours_fit_to_limit(hours, limit_in_hours):
    if(hours <= limit_in_hours):
        return True
    else:
        return False
    
#kas kõik ajavahemikud klapivad
check1 = check_timedifference(which_timeperiod_in_starts1, which_timeperiod_in_ends1)
check2 = check_timedifference(which_timeperiod_in_starts2, which_timeperiod_in_ends2)
check3 = check_timedifference(which_timeperiod_in_starts3, which_timeperiod_in_ends3)
check4 = check_timedifference(which_timeperiod_in_starts4, which_timeperiod_in_ends4)
check5 = check_timedifference(which_timeperiod_out_starts1, which_timeperiod_out_ends1)
check6 = check_timedifference(which_timeperiod_out_starts2, which_timeperiod_out_ends2)
check7 = check_timedifference(which_timeperiod_out_starts3, which_timeperiod_out_ends3)
check8 = check_timedifference(which_timeperiod_out_starts4, which_timeperiod_out_ends4)
check9 = check_workinghours(how_many_minutes_in, how_many_minutes_out, timeIn1, timeIn2, timeIn3, timeIn4, timeOut1, timeOut2, timeOut3, timeOut4)
check10 = check_capacity(appliance, max_electicity_consumption, min_electicity_consumption, hours_working)

def check_final(check1, check2, check3, check4, check5, check6, check7, check8, check9, check10):
    if(check1 is not False and check2 is not False and check3 is not False and check4 is not False and check5 is not False and check6 is not False and check7 is not False and check8 is not False and check9 is not False and check10 is not False):
        print('Everything is correct')
        return True;
    else:
        print('Please fix your mistakes')
        return False;
#hakkame moodustama graafikut

if(check_final(check1, check2, check3, check4, check5, check6, check7, check8, check9, check10)==True):
    turn_device_on=[]
    turn_device_off=[]
    #kui pole vaja lisaaegu kuna kasutaja sisestatud aegadest piisab
    if(check10<max_electicity_consumption):
        how_many_times = return_existing_workingtimes(which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3, which_timeperiod_in_starts4, which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3, which_timeperiod_in_ends4)
        if(how_many_times == '0'):
            turn_device_on=[]
            turn_device_off=[]
        elif(how_many_times == '1'):
            turn_device_on=[which_timeperiod_in_starts1]
            turn_device_off=[which_timeperiod_in_ends1]
        elif(how_many_times == '2'):
            turn_device_on=[which_timeperiod_in_starts1, which_timeperiod_in_starts2]
            turn_device_off=[which_timeperiod_in_ends1, which_timeperiod_in_ends2]
        elif(how_many_times == '3'):
            turn_device_on=[which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3]
            turn_device_off=[which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3]
        elif(how_many_times == '4'):
            turn_device_on=[which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3, which_timeperiod_in_starts4]
            turn_device_off=[which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3, which_timeperiod_in_ends4]
    else:
        print('error')
    if(check10<=0):
        text_file1 = open("WorkingTimes.txt", "w")
        text_file2 = open("TurnOffTimes.txt", "w")
        for item in turn_device_on:
          text_file1.write("%s\n" % item)
        for item in turn_device_off:
          text_file2.write("%s\n" % item)
        text_file1.close()
        text_file2.close()
    else:
        missing_power = round(check10, 1)
        print(missing_power)
        missing_hours = round(calculate_hours_from_capacity(appliance, missing_power), 1)
        print(missing_hours)
        maxlimit = convert_min_to_hour(how_many_minutes_in_at_once)
        i=1
        while(check_if_hours_fit_to_limit(missing_hours, maxlimit) is False):
          i=i*2
          missing_hours = missing_hours/2
        place_missing_times_to_plan(i, cheap_times, missing_hours, turn_device_on, turn_device_off)
        print('Korras, jagasime aja', i, 'Ajajupid on', missing_hours, 'pikkused')
        text_file1 = open("WorkingTimes.txt", "w")
        text_file2 = open("TurnOffTimes.txt", "w")
        for item in turn_device_on:
          text_file1.write("%s\n" % item)
        for item in turn_device_off:
          text_file2.write("%s\n" % item)
        text_file1.close()
        text_file2.close()

print(turn_device_off)
