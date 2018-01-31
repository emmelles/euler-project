#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:53:59 2018

@author: mls
"""

#f = open('names_test.txt', 'r')
f=open('names.txt','r')
ls = f.read().strip().replace('"','').split(",")
ls.sort()

values=[]

for i,name in enumerate(ls):
    val=(i+1)
    score=0
    for x in name:
       score+=ord(x.lower())-96
    values.append(score*val)

print sum(values)