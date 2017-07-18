#!/usr/bin/env python

from math import log

bound=1000000

def next_collatz(n):
    if log(n,2).is_integer(): return 1
    elif n%2==0: n/=2
    else: n=3*n+1
    return n

max_val,max_count=0,0
for x in range(1,bound+1):
    n=x
    counter=0
    while n!=1:
        n=next_collatz(n)
        counter+=1
    if counter>max_count:
        max_val,max_count=x,counter
        
print max_val, max_count
