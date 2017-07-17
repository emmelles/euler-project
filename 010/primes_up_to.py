#!/usr/bin/env python
            
from timeit import default_timer as timer

def primes_up_to(upto):
    primes=[2]
    for n in range(3,upto+1):
        for m in range(0,len(primes)):
            if primes[m]<=n**0.5 and n % primes[m] == 0: break
            elif primes[m]>n**0.5:
                primes+=[n]
                break
    return primes

start=timer()
print primes_up_to(200)
end=timer()
print "Time elapsed (s)", end-start
