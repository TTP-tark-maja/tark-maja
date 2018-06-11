#kontrollfunktsioon

## väljasoleku aeg ei saa olla pikem kui seesoleku aeg ---
## seesoleku aeg ei saa olla üle 24h ---
## korraga ei saa olle sees üle 24h ---
## korraga ei saa olla väljas kauem kui korraga sees --- 
## algus aeg ja lõpuaeg peavad olema vastavalt enne ja pärast ---
## min ja max elektri kasutused ei saa miinuses olla
## puhkeajad peavad mahtuma 24h sisse ---

from datetime import datetime, timedelta

how_many_minutes_in = 180
how_many_minutes_out = 60

how_many_minutes_in_at_once = 20
how_many_minutes_out_at_once = 30

which_timeperiod_in_starts1 = datetime(2015, 9, 12, 10, 9, 45)
which_timeperiod_in_ends1 = datetime(2015, 9, 12, 12, 12, 10)

which_timeperiod_in_starts2 = datetime(2015, 9, 12, 13, 9, 45)
which_timeperiod_in_ends2 = datetime(2015, 9, 12, 14, 12, 10)

which_timeperiod_in_starts3 = datetime(2015, 9, 12, 13, 9, 45)
which_timeperiod_in_ends3 = datetime(2015, 9, 12, 13, 9, 45)

which_timeperiod_in_starts4 = datetime(2015, 9, 12, 15, 9, 45)
which_timeperiod_in_ends4 = datetime(2015, 9, 12, 16, 12, 10)

which_timeperiod_out_starts1 = datetime(2015, 9, 12, 17, 9, 45)
which_timeperiod_out_ends1 = datetime(2015, 9, 12, 19, 9, 45)

which_timeperiod_out_starts2 = datetime(2015, 9, 12, 18, 9, 45)
which_timeperiod_out_ends2 = datetime(2015, 9, 12, 20, 9, 45)

which_timeperiod_out_starts3 = datetime(2015, 9, 12, 18, 9, 45)
which_timeperiod_out_ends3 = datetime(2015, 9, 12, 20, 9, 45)

which_timeperiod_out_starts4 = datetime(2015, 9, 12, 18, 9, 45)
which_timeperiod_out_ends4 = datetime(2015, 9, 12, 20, 9, 45)


max_electicity_consumption = 10
min_electicity_consumption = 2

appliance = 850

  
conditions = (how_many_minutes_in, how_many_minutes_out, how_many_minutes_in_at_once, how_many_minutes_out_at_once, which_timeperiod_in_starts1, which_timeperiod_in_ends1, which_timeperiod_out_starts1, which_timeperiod_out_ends1, max_electicity_consumption, min_electicity_consumption, appliance)

def convert_Min_To_Hour(minutes):
    return minutes/60
    
def calculate_capacity(applience, workinghours):
    capacity = workinghours*(applience/1000)
    return capacity

def calculate_timedifference_in_hours(starttime, endtime):
    timedifference =(endtime-starttime)
    duration_in_s = timedifference.total_seconds()
    hours = divmod(duration_in_s, 3600)[0]
    totalminutes = divmod(duration_in_s, 60)[0]
    minutes = round((totalminutes-hours*60)/6, 2)
    timedifference = hours+minutes
    return timedifference

time1 = calculate_timedifference_in_hours(which_timeperiod_in_starts1, which_timeperiod_in_ends1)
time2 = calculate_timedifference_in_hours(which_timeperiod_in_starts2, which_timeperiod_in_ends2)
time3 = calculate_timedifference_in_hours(which_timeperiod_in_starts3, which_timeperiod_in_ends3)
time4 = calculate_timedifference_in_hours(which_timeperiod_in_starts4, which_timeperiod_in_ends4)
timeOut1 = calculate_timedifference_in_hours(which_timeperiod_out_starts1, which_timeperiod_out_ends1)
timeOut2 = calculate_timedifference_in_hours(which_timeperiod_out_starts2, which_timeperiod_out_ends2)
timeOut3 = calculate_timedifference_in_hours(which_timeperiod_out_starts3, which_timeperiod_out_ends3)
timeOut4 = calculate_timedifference_in_hours(which_timeperiod_out_starts4, which_timeperiod_out_ends4)

def check_Timedifference (starttime, endtime):
    timedifference = calculate_timedifference_in_hours(starttime, endtime)
    if(timedifference < 0.1):
        print("Time can not be negative")
    elif (timedifference > 24):
        print("Time difference can not be over 24 hours")
    else:
        print("time differnece: ")
        print(timedifference)

def check_Amount_Of_Hours_Working(minutesWorking, minutesNotWorking, timeDifference1, timeDifference2, timeDifference3, timeDifference4, minutesOut1, minutesOut2, minutesOut3, minutesOut4):
    minutesWorking = convert_Min_To_Hour(how_many_minutes_in)
    minutesNotWorking = convert_Min_To_Hour(how_many_minutes_out)
    totalWorkingTime = minutesWorking + minutesNotWorking + timeDifference1 + timeDifference2 + timeDifference3 + timeDifference4 + minutesOut1 + minutesOut2 + minutesOut3 + minutesOut4
    if(totalWorkingTime > 24):
        print("On or Off times are too long")
    else:
        print("Total working time: ")
        print(totalWorkingTime)
        

    
    
def check_capacity(appliance, max_capacity, min_capacity, time1start, time1end, time2start, time2end, time3start, time3end, time4start, time4end):

    timetogether = time1 + time2 + time3 + time4
    print('togther')
    print(timetogether)
    print('capa')
    capacity = calculate_capacity(appliance, timetogether)
    print(capacity)
    maxcapacity = calculate_capacity(appliance, 24)
    if(capacity>max_capacity):
        print('Sisestatud ajad ületavad sisestatud maksimaalse elektrimahu')
    if(maxcapacity<min_capacity):
        print('Sisestatud minimaalset elektrimahtu ei ole sellel seadel võimalik täita') 
    else:
        missing_capacity = min_capacity - capacity
        print('missing')
        print(missing_capacity)
        print('Korras')


check_capacity(appliance, max_electicity_consumption, min_electicity_consumption, which_timeperiod_in_starts1, which_timeperiod_in_ends1,  which_timeperiod_in_starts2, which_timeperiod_in_ends2, which_timeperiod_in_starts3, which_timeperiod_in_ends3, which_timeperiod_in_starts4, which_timeperiod_in_ends4)
timedifference = calculate_timedifference_in_hours(which_timeperiod_in_starts1, which_timeperiod_in_ends1)
capacity = calculate_capacity(appliance, timedifference)

     
    
    
check_Amount_Of_Hours_Working(how_many_minutes_in, how_many_minutes_out, time1, time2, time3, time4, timeOut1, timeOut2, timeOut3, timeOut4)        

check_Timedifference(which_timeperiod_in_starts1, which_timeperiod_in_ends1)

timedifference = calculate_timedifference_in_hours(which_timeperiod_in_starts1, which_timeperiod_in_ends1)
capacity = calculate_capacity(appliance, timedifference)
    
