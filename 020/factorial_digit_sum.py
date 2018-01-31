#!/usr/bin/env python

from math import factorial as factorial
from functools import reduce

sum = reduce( (lambda x, y: int(x)+int(y)) , list(str(factorial(100))) )
print sum
