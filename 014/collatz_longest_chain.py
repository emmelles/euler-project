#!/usr/bin/env python

from math import log
import time

start=time.time()

bound=1000000

def next_collatz(n):
    if log(n,2).is_integer(): return 1
    elif n%2==0: n/=2
    else: n=3*n+1
    return n

max_val,max_count=0,0
cache={}
for x in range(1,bound+1):
    n=x
    counter=0
    while n!=1:
        if n in cache:
            counter+=cache[n]
            n=1
        else:
            n=next_collatz(n)
            counter+=1
    cache[x]=counter
    if counter>max_count:
        max_val,max_count=x,counter

end=time.time()
print "Longest chain is %s with length %s, time elapsed %s seconds" % (max_val, max_count+1, end-start)
