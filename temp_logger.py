# Raspberry Pi Temperature Logger
# Zagros Robotics, Inc.
# www.zagrosrobotics.com
# 6/25/2013

# Additional Modification by Asim Zeeshan
# Dated Sep 04, 2015
# Modified it to be run using a crontab instead of a "while True"

import smbus
import time
import datetime

#SMBus(0) - Raspberry Pi Model A
#SMBus(1) - Raspberry Pi Model B

bus = smbus.SMBus(1)

#I2C address of sensor
address = 0x48

def temperature():
    rvalue0 = bus.read_word_data(address,0)
    rvalue1 = (rvalue0 & 0xff00) >> 8
    rvalue2 = rvalue0 & 0x00ff
    rvalue = (((rvalue2 * 256) + rvalue1) >> 4 ) *.0625
    #print rvalue1, rvalue2
    return rvalue

#Open Log File
logfile=datetime.datetime.now().strftime("%Y-%m-%d")
f=open('logs/'+logfile+'_temperature_sensor.log','a')
now = datetime.datetime.now()
timestamp = now.strftime("%d-%b-%Y %H:%M:%S")
outvalue = temperature()
outstring = "["+str(timestamp)+"]  "+str(outvalue)+" C / "+str(outvalue*1.8+32)+" F"+"\n"
print outstring
f.write(outstring)
f.close()