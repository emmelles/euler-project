#!/usr/bin/env python
            
from timeit import default_timer as timer

# brute force
def brute_primes(upto):
    primes=[2]
    # over numbers want to check:
    for i in range(3,upto+1):
        # over current primes:            
        for j in range(len(primes)):
            if i % primes[j] == 0:
                break
            elif j==len(primes)-1:
                primes.append(i)     
    return primes

def primes_up_to(upto):
    primes=[2]
    # starts prime counting from 3
    for n in range(3,upto+1):
        # over current prime table
        for m in range(0,len(primes)):
            # because checking factors from beginning, need only get to sqrt(number)
            # as the next factor would be some number greater than sqrt(n),
            # sqrt(n)+q, and (sqrt(n)+q)*sqrt(n)>n
            if primes[m]<=n**(1/2) and n % primes[m] == 0: 
                break
            elif primes[m]>n**(1/2):
                primes+=[n]
                break
    return primes
  

start=timer()
print(brute_primes(20000))
end=timer()
print("Time elapsed (s)", end-start)


start=timer()
print(primes_up_to(20000))
end=timer()
print("Time elapsed (s)", end-start)
