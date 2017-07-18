#!/usr/bin/env python

import itertools, math

def perms(str):
    return len(set(itertools.permutations(str)))

''' Brute force, we'd do something like:
str="0"*grid+"1"*grid
print len(set(itertools.permutations(str)))
But this takes up a lot of cpu time.
Consider instead:

full=perms("0123")
binary=perms("0011")
print full, binary, full/binary
Returns 24, 6, 4

full=perms("012345")
binary=perms("000111")
print full, binary, full/binary
Returns 720, 20, 36

full=perms("01234567")
binary=perms("00001111")
print full, binary, full/binary
Returns 40320, 70, 576'''

# We can conclude that the correct formula for permutations is:
def paths(gridsize):
    return math.factorial(gridsize*2)/math.factorial(gridsize)**2

print "For a %s by %s grid there are %s paths." % (2, 2, paths(2))
print "For a %s by %s grid there are %s paths." % (20, 20, paths(20))


