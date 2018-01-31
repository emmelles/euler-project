#!/usr/bin/env python

from timeit import default_timer as timer

num=1
lim=501

def triangle(n):
    return n*(n+1)*0.5

#~~ BRUTE FORCE ~~#

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

#~~ MORE COMPLICATED ISN'T ALWAYS BETTER ~~~#

def primes_up_to(upto):
    primes=[2]
    for n in range(3,upto+1):
        for m in range(0,len(primes)):
            if primes[m]<=n**0.5 and n % primes[m] == 0: break
            elif primes[m]>n**0.5:
                primes+=[n]
                break
    return primes

def divisors_using_gen_primes(n,primes):
    fact=1
    for i in range(0, len(primes)):
        exp=1
        while n%primes[i]==0:
            exp+=1
            n/=primes[i]
        fact*=exp
    return fact

#~~~~~~~~~~~~~~~~~~~~~#

primes=primes_up_to(1000)

start=timer()

current=triangle(num)
#while divisors(current)<lim:
while divisors_using_gen_primes(current,primes)<lim:
    num+=1
    current=triangle(num)

print int(current)

end=timer()
print "Time elapsed ", end-start

# Method 2
start=timer()

current=triangle(num)
while divisors(current)<lim:
    num+=1
    current=triangle(num)

print int(current)

end=timer()
print "Time elapsed ", end-start
