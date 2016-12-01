T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    sum = 0
    exp = 2**n
    while exp > 0:
        sum+=(exp%10)
        exp=exp//10
    print(sum)
        