#!/usr/bin/env python

num=str(2**1000)
#num=str(2**15)
print num

tot=0
for i in range(0,len(num)):
    tot+=int(num[i])
    
print tot

