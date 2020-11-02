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

limit=28124
lowlimit=12

def divisors(n):
    bound=n/2
    current=1
    l=[]
    while current<=bound:
        if n % current==0:
            l.append(current)
            current+=1
        else:
            current+=1
    return l

def abundant(n):
    if sum(divisors(n)) > n: 
        return True
    return False

print abundant(12)
print divisors(18)
print abundant(24)
print abundant(30)

absnums=[]

for i in range(1,40):
    if abundant(i): absnums.append(i)

print absnums
