#kontrollfunktsioon

## väljasoleku aeg ei saa olla pikem kui seesoleku aeg
## seesoleku aeg ei saa olla üle 24h ---
## korraga ei saa olle sees üle 24h
## korraga ei saa olla väljas kauem kui korraga sees
## algus aeg ja lõpuaeg peavad olema vastavalt enne ja pärast ---
## min ja max elektri kasutused ei saa miinuses olla
## puhkeajad peavad mahtuma 24h sisse

from datetime import datetime, timedelta

how_many_minutes_in = 180
how_many_minutes_out = 60

how_many_minutes_in_at_once = 20
how_many_minutes_out_at_once = 30

which_timeperiod_in_starts = datetime(2015, 9, 12, 10, 9, 45)
which_timeperiod_in_ends = datetime(2015, 9, 12, 12, 12, 10)

which_timeperiod_out_starts = '2018-06-08 18:00:00'
which_timeperiod_out_ends = '2018-06-08 20:00:00'

max_electicity_consumption = 10
min_electicity_consumption = 2

timeDifference1 = 0
timeDifference2 = 0
timeDifference3 = 0
timeDifference4 = 0

appliance = 850

conditions = (how_many_minutes_in, how_many_minutes_out, how_many_minutes_in_at_once, how_many_minutes_out_at_once, which_timeperiod_in_starts, which_timeperiod_in_ends, which_timeperiod_out_starts, which_timeperiod_out_ends, max_electicity_consumption, min_electicity_consumption, appliance)

def convert_Min_To_Hour(minutes):
    return minutes/60
    
def calculate_capacity(applience, workinghours):
    capacity = workinghours*(applience/1000)
    print(capacity);
    return capacity

def calculate_timedifference_in_hours(starttime, endtime):
    timedifference =(endtime-starttime)
    duration_in_s = timedifference.total_seconds()
    hours = divmod(duration_in_s, 3600)[0]
    totalminutes = divmod(duration_in_s, 60)[0]
    minutes = round((totalminutes-hours*60)/6, 2)
    timedifference = hours+minutes
    return timedifference


def check_Timedifference (starttime, endtime):
    timedifference = calculate_timedifference_in_hours(starttime, endtime)
    if(timedifference < 0.1):
        print("Time can not be negative")
    elif (timedifference > 24):
        print("Time difference can not be over 24 hours")
    else:    
        print(timedifference)

def check_Amount_Of_Hours_Working(minutesWorking, minutesNotWorking, timeDifference1, timeDifference2, timeDifference3, timeDifference4):
    minutesWorking = convert_Min_To_Hour(how_many_minutes_in)
    minutesNotWorking = convert_Min_To_Hour(how_many_minutes_out)
    totalWorkingTime = minutesWorking + minutesNotWorking + timeDifference1 + timeDifference2 + timeDifference3 + timeDifference4
    if(totalWorkingTime > 24):
        print("On or Off times are too long")
    else:
        print(totalWorkingTime)
    
        
    
    
check_Amount_Of_Hours_Working(how_many_minutes_in, how_many_minutes_out, timeDifference1, timeDifference2, timeDifference3, timeDifference4)        

check_Timedifference(which_timeperiod_in_starts, which_timeperiod_in_ends)

timedifference = calculate_timedifference_in_hours(which_timeperiod_in_starts, which_timeperiod_in_ends)
capacity = calculate_capacity(appliance, timedifference)
    
