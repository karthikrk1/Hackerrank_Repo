#!/bin/python35
import math


def nDigitFibo(n):
    phi = ((1+math.sqrt(5))/2)
    ans = math.ceil((math.log(10)*(n-1)+math.log(5)/2)/math.log(phi))
    return ans

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    print(nDigitFibo(N))
    

    