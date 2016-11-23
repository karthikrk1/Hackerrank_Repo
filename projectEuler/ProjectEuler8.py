#!/bin/python3

import sys

def findProd(n):
    out=1
    for i in n:
        out*=int(i)
    return out 

def findMaxProd(num,n,k):
    maxi=-(sys.maxsize)
    i=0
    for i in range(len(num)-k+1):
        numPart = num[i:i+k]
        prod = findProd(numPart)
        if prod > maxi:
            maxi = prod
        
    return maxi

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(findMaxProd(num,n,k))


    