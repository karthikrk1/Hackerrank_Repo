#!/bin/python3

import sys

def buildSieve(N=1000000):
    N+=1 # This is to make sure we have the N inclusive in the array and not getting it lost due to 0-based indexing of Python lists 
    isPrime = [True] * N # Initializing the isPrime list with all True values.
    isPrime[0] = isPrime[1] = False # Since 0 and 1 are considered Neither Prime nor composite. So we make them False.
    for (ind, num) in enumerate(isPrime):
        if num:
            for no in range(ind*ind, N, ind): # This is used to mark the factors as not Prime. 
                isPrime[no] = False
    return isPrime

def calSum(limit):
    #limit=1000000
    arr = buildSieve(limit)
    total=0
    sum=[0]*(limit+1)
    for i in range(0,limit+1):
        if arr[i]:
            total+=i
        sum[i]=total
    return total
                
        
t = int(input().strip())


sum=calSum(1000000)

for a0 in range(t):
    n = int(input().strip())
    print(sum[n])
    
    