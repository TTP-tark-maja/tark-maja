import subprocess, sys
import datetime
import json
fm = open("WorkingTimes.txt")
kell = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
for rida in fm:
    if kell not in rida:
        x=2
    else:
        process =subprocess.Popen(["/home/pi/Desktop/tark-maja/relee_sisselylitus.sh"])
        with open("logfile.txt", "a") as file:
            line = subprocess.check_output(['tail', '-1', "logfile.txt"])
            line2 = line.decode("utf-8")
            if("sisse") not in line2:
                aeg = datetime.datetime.now().strftime("%H:%M:%S")
                file.write("Tarbija lylitati sisse kell:")
                file.write(aeg)
                file.write("\n")
                file.close()
fs = open("TurnOffTimes.txt")
for row in fs:
    if kell not in row:
        x=2
    else:
        process =subprocess.Popen(["/home/pi/Desktop/tark-maja/relee_valjalylitus.sh"])
        with open("logfile.txt", "a") as file:
            line = subprocess.check_output(['tail', '-1', "logfile.txt"])
            line2 = line.decode("utf-8")
            if("v2lja") not in line2:
                aeg = datetime.datetime.now().strftime("%H:%M:%S")
                file.write("Tarbija lylitati v2lja kell:")
                file.write(aeg)
                file.write("\n")
                file.close()
		
