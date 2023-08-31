import re

a= "11250098176 bytes total (6942457856 bytes free)"
with open("dir","r") as f:
    file=f.readlines()
    c=",".join(file)
    result=re.search("(\d+)\s+bytes\s+total\s+.(\d+)\s+bytes\s+free.",c).groups()
    total_mem=result[0]
    free_mem=result[1]
    print("总的内存为{},剩余内存为{}".format(total_mem,free_mem))




b="0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored"



c=" 0 output errors, 2 interface resets"

d="Processor  7F553B585048   2973590156   323362360   2650227796   2615137492   2649855728"

e="CPU utilization for five seconds: 0%/0%; one minute: 0%; five minutes: 0%"

f="Cisco IOS XE Software, Version 17.03.06"

g="uptime is 23 hours, 36 minutes"




