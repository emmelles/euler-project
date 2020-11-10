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

def properDivisors(n,primes):
    #propdivstemp=[x*y for x in factorise(n) for y in factorise(n) if n%(x*y)==0]
    propdivs=[]
    divs=factorise(n,primes)
    #[propdivs.append(x) for x in propdivstemp if x not in propdivs]
    x=0
    while x < len(divs):
        for y in divs:
            if n % (divs[x]*y)==0 and (divs[x]*y) not in propdivs: propdivs.append(divs[x]*y)
        divs.pop(0)
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
x=13
print(factorise(x,primeslist))
print(properDivisors(x,primeslist))
print(isAbundant(x,primeslist))
'''

abundants=[]

for i in range(lmin,lmax+1):
    if isAbundant(i,primeslist): abundants.append(i)

#print("Abundant numbers:",abundants)

sumAbundants=[]

i=0
while i<len(abundants):
    for x in abundants:
        if (abundants[i]+x)<lmax: 
            sumAbundants.append(abundants[i]+x)
    abundants.pop(0)

print("Numbers that can be written as abundant sums:", sumAbundants)

'''
nonSumAbt=[]
for x in range(len(sumAbundants)):
    if x not in sumAbundants: nonSumAbt.append(x)
    if x>=lmax: break

print("Non abundant sum numbers:", nonSumAbt[-1])
'''