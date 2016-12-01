#!/bin/python3

import sys

def findTriplet(n):
    out=[]
    for i in range(1,n//2):
        j = (((n-i)*(n-i))-(i**2))//2*(n-i)
        k = n-j-i
        if (i**2)+(j**2)==(k**2) and j>0 and k>0 and j+k>i and i+j>k and i+k>j:
            out.append(i*j*k)
    if out:
        return max(out)
    else:
        return -1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(findTriplet(n))