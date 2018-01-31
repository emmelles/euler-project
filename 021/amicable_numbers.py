#!/usr/bin/env python

upto=10000
nos=list(range(0,upto))

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

amicables=[]

while nos:
    x=nos.pop(0)
    friend=sum(divisors(x))
    if sum(divisors(friend))==x and friend!=x:
        if friend in nos: nos.remove(friend)
        amicables+=[x,friend]

print sum(amicables)
