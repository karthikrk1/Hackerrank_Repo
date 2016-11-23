t = int(input().strip())

def findFactorial(n):
    a=[]
    a.append(1)
    for i in range(1,n+1):
        a.append(i*a[i-1])
    
    return a[n]
        

for _ in range(t):
    n=int(input().strip())
    fact=findFactorial(n)
    sum=0
    while fact > 0:
        sum+=(fact%10)
        fact=fact//10
    print(sum)
    
