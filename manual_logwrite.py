import subprocess, sys
import datetime
line = subprocess.check_output(['tail' "-1", "logfile.txt"])
line2 = line.decode("utf-8")
with open("logfile.txt", "a") as file:
    if("sisse") not in line2:
        aeg = datetime.datetime.now().strftime("%H:%M:%S")
        file.write("Tarbija lylitati sisse kell:")
        file.write(aeg)
        file.write("\n")
        file.close()
    else:
        aeg = datetime.datetime.now().strftime("%H:%M:%S")
        file.write("Tarbija lylitati v2lja kell:")
        file.write(aeg)
        file.write("\n")
        file.close()
        
