#!/usr/bin/env python

num=1
# We could assume something more about starting point really,
# however we definitely know 7th doesn't have 500...

lim=501

def divisors(n):
    bound=n**0.5
    fact=0
    current=1
    while current<=bound:
        if n % current==0:
            fact+=2
            current+=1
        else:
            current+=1
    return fact

def triangle(n):
    return n*(n+1)*0.5

#~~~~~~~~~~~~~~~~~~~~~#

current=triangle(num)
while divisors(current)<lim:
    num+=1
    current=triangle(num)

print int(current)
