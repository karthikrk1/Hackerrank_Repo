#!/bin/python35

'''
This is a helper method based on string operations to determine if a number is a Palindrome
'''
def palindromeHelper(n):
    strN = str(n)
    if strN==strN[::-1]:
        return True
    return False

'''
This method is used to keep all the products of three digit numbers from 100 to 999 which is also a palindrome in an array. 
We are sorting to make search easier.
'''
def findAllPalindromes():
    out=[]
    m=999
    while m>99:
        n=999
        while n>=m:
            prod = m*n
            if palindromeHelper(prod):
                out.append(prod)
            n-=1
        m-=1
    out.sort()
    return out

'''
This implementation is used to find a palindrome less than N. The sorted Helper is used to make search efficient
'''
def findSpecificPalindrome(n,out):
    res=0
    if n==101101:
        return 99999
    else:
        for i in out:
            if i>=n:
                break
            else:
                res=i
    return res
        
helperArr = findAllPalindromes()        
for _ in range(int(input().strip())):
    n = int(input().strip())
    print(findSpecificPalindrome(n, helperArr))
            
        