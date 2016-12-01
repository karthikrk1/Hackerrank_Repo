#!/bin/python35

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

def getFactors(n):
    factorsList = []
    for i in range(1,n+1):
        if n%i==0:
            factorsList.append(i)
    return factorsList

outList = [x for x in getFactors(min(b)) if all(x%i==0 for i in a) and all(j%x==0 for j in b)]

print(len(outList))



    