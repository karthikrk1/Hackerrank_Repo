#!/bin/python35
import functools
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(functools.reduce(lambda x,y: x*y//gcd(x,y), range(1,n+1)))
    