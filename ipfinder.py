import subprocess
import os
import platform
from datetime import datetime
with open(os.devnull, "wb") as limbo:
        net = raw_input("Enter the Network address : ").split('.')      
        a = '.'
        net2  = net[0]+a+net[1]+a +net[2]+a
        start = int(input("Enter the start address : "))
        end = int(input ("Enter the end address : "))
        oper = platform.system()
        if (oper == 'Windows'):
                ping = "ping -n 1 -w 200 "
        else:
                ping = "ping -c 1 -W 200 "

        t1 = datetime.now()
        summ=0
        for n in range(start, end):
                
                ip=net2+str(n)
                ping1= ping+ip
                result=subprocess.Popen(ping1,
                        stdout=limbo, stderr=limbo).wait()
                if result == 0:
                        summ+=1
                        print ip, "---> " "active"
                else:
                      continue
        t2 = datetime.now()
        total = t2 - t1
        
        print ("number of active hosts = {} ").format(summ)
        print ("Scanning complete in {}").format(total)
