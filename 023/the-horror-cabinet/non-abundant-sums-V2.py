#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import sqrt

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

def factorise(n,primes):
    factors=[1]
    for x in primes:
        if x>n:
            break
        if n%x==0: 
            while n%x==0:
                factors.append(x)
                n=n/x
    return factors


############THIS IS THE PROBLEM!!!!##########################
def properDivisors(n,primes):
    propdivs=[]
    divs=factorise(n,primes)   
    for x in divs:
        for y in divs:
            prod=x*y
            if n % prod==0 and prod not in propdivs: 
                if prod<n: propdivs.append(prod)
                x=prod
    propdivs.sort()
    return propdivs

def isAbundant(n,primes):
    if sum(properDivisors(n,primes))>n: 
        return True
    else:
        return False
    
# unfortunately List Comprehension appears to be quite a bit slower (cos double counting?)


lmin=12
lmax=28123
#lmax=50

primeslist=primesUpTo(lmax)

'''
for x in range(1,lmax):
    print("##################")
    print("Number is",x)
    print("Divs:",factorise(x,primeslist))
    print("Prop div:",properDivisors(x,primeslist))
    print(isAbundant(x,primeslist))
'''

abundants=[]

for i in range(lmin,lmax+1):
    if isAbundant(i,primeslist): 
        abundants.append(i)

print("Abundant numbers:",abundants)


sumAbundants=[]
i=0
while i<len(abundants):
    y=abundants[i]
    for x in abundants:
        if (y+x)<=lmax and (y+x) not in sumAbundants: 
            sumAbundants.append(y+x)
    abundants.pop(0)

sumAbundants.sort()

print("###########################################################")
print("Numbers that can be written as abundant sums:", sumAbundants)

'''
nonSumAbundants=[]

for i in range(1,lmax+1):
    if i not in sumAbundants: nonSumAbundants.append(i)
    
print("Numbers not written as sum of abundants:", nonSumAbundants)
'''