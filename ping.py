import os
import re
#cmd1 here, we can give command
cmd1 = "ping -n 1 192.168.1."
#ip were not completely mentioned in cmd1 
# last set of ip will be our range limits
for i in range(50,200):
    op = os.popen(cmd1+str(i)).readlines()
    #here,cmd1 is concatenated with i 
    #op's result comes as list as readlines() is used
    #print(str1)
    for j in op:
        mo = re.search(".*time=(\d+)ms.*",j)
        #Reply from 192.168.1.62: bytes=32 time=30ms TTL=64
        #search for time=xxms

        if mo:
            print("Its pingable!")
            print(f"{cmd1[9:]+str(i)} has a response time of {mo[1]}ms")
            break
    else:
        print("Not pingable!!")
#Reply from 192.168.1.62: bytes=32 time=30ms TTL=64
