#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is 
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
"""
#import sys
from math import sqrt,floor

limit=28123
lowlimit=12

def primesUpTo(n):
    primes=[2]
    for x in range(3,n+1):
        for y in primes:
            # unfortunately with list comprehension cant figure out how to do sqrt break
            divs=[]
            if y>sqrt(x): 
                break
            if x % y==0:
                divs.append(y)
                break
        if divs==[]: primes.append(x)
    return primes

# this is divisors, I need proper divisors??
def divisors(n):
    # find factors of number n
    primes=primesUpTo(floor(sqrt(n)))
    factors=[1]
    # All factors must be smaller than sqrt
    for i in range(len(primes)):
        while n % primes[i]==0:
            factors.append(primes[i])
            n=n/primes[i]
    return factors

def properdivisors(n):
    ls=divisors(n)
    #properdiv=[a*b for a in ls for b in ls] # this double-counts
    tempdiv=[]
    i=0
    while i<len(ls):
        for j in range(len(ls)):
            if n%(ls[i]*ls[j])==0:
                tempdiv.append(ls[i]*ls[j])
        ls.pop(0)
    properdiv=[]
    [properdiv.append(x) for x in tempdiv if x not in properdiv]
    return properdiv

def abundant(n):
    # return true if sum is greater than n false else
    if sum(properdivisors(n)) > n: 
        return True
    return False

# can now check for abundance, and write factors

# was pretty sure upper limit entirely fine for table but got curious abt max
# print(sys.maxsize)

#lowlimit=12 #temp
#limit=100 #temp
abundants=[]

#print(limit)
#print(divisors(limit))
#print(properdivisors(limit))
#print("Is this abundant",abundant(limit))

for i in range(lowlimit,limit+1):
    if abundant(i): abundants.append(i)

# we now have a list of all the abundant numbers up to the limit
# we want to find all the numbers up to the limit which CAN be written as the
# pairwise sum of two abundants

# abundants is an ordered list
print("abundants are",abundants)

sumabt=[]

# I want to remove duplicate operations, i.e.
# I can pop out the first entry once I've multiplied it by everything
# I use a while loop to stop when I've run out of list
i=0
while i<len(abundants):
    # then I can multiply by all remaining abundants
    for j in range(len(abundants)):
        #print(abundants,abundants[i],abundants[j])
        sumij=abundants[i]+abundants[j]
        # if I exceed limit the next one over also will so get out
        if sumij>limit:
            break
        else:
            sumabt.append(sumij)
    abundants.pop(0)
        
# now got a list of all abundants
sumabt.sort()
print("Pairs within limit that are sums of abt",sumabt)


'''
"Python has a language feature called List Comprehensions that is perfectly 
suited to making this sort of thing extremely easy" -- the internet'''


#nonabtsum = [x for x in range(1,limit+1) if x not in sumabt]
#print(sum(nonabtsum))
