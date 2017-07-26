#!/usr/bin/env python

f=open("triangle.txt","r")

currentline=f.readline().split()
nextline=f.readline().split()

while nextline:
    for i in range(0, len(nextline)):
        if i==0: nextline[0]=int(nextline[0])+int(currentline[0])
        elif 0<i<len(nextline)-1: nextline[i]=int(nextline[i])+max(int(currentline[i]),int(currentline[i-1]))
        else: nextline[i]=int(nextline[i])+int(currentline[i-1])
        
    currentline=nextline
    nextline=f.readline().split()
print "The maximum sum path is ", max(currentline)
    
f.close()
