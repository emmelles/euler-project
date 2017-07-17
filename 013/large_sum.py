#!/usr/bin/env python

f=open("test.txt","r")

entries=[]

for line in f:
    entries.append(int(line))

print sum(entries)
