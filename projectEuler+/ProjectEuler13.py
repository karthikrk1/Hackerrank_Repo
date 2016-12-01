n = int(input().strip())

sum = 0

for _ in range(n):
    sum+=int(input().strip())
    
s = str(sum)
print(s[0:10])