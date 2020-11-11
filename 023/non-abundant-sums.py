#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:36:46 2020

@author: mls
"""

# I got so confused on this problem for ages... not great

from math import sqrt

def properDivisors(n):
    pd=[1]
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: 
            pd+=[i]
            if int(n/i) not in pd: pd+=[int(n/i)]
    pd.sort() 
    
    return pd

def isAbundant(n):
    return sum(properDivisors(n))>n

############################################################

lmin=1
lmax=28123
#lmax=500


# for x in range(lmin,lmax+1):
#     print("Proper divisors of",x, "are", properDivisors(x))

abundants=[x for x in range(lmin,lmax+1) if isAbundant(x)]

abdsums=[]

while len(abundants): # i.e. >0
    x=abundants[0]
    for y in abundants:
        if (x+y)<lmax: abdsums.append(x+y)   
        else: break
    del abundants[0]

abdsums.sort()

# I was gonna get all non abundants but can just subtract from total given that
# I don't need to do anything else with non-abundant-sums
print(sum(range(lmax)) - sum(set(abdsums)))