#!/usr/bin/env python

# I figured I'd start this problem by playing with prime factors in python
# given that I haven't (and wanted to try filter n stuff)
# Self-contained so no roots and floors

num=int(raw_input("Enter to factorise:"))

def factors(n):
    fact=[]
    while n%2==0:
        n,fact=n/2,[2]
        if n==1: return fact
    # courtesy of the internet, really neat. Using a generator here, then
    # implicit list operation to add the increasing factors and decreasing extras n/i
    # (note that this does yield repetition for perfect squares)
    fact+=reduce(list.__add__,([i, n/i] for i in range(1, int(n**0.5)+1) if n%i==0))
    return fact

print factors(num)
