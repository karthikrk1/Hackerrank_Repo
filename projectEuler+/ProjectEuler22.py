#!/bin/python
N=int(input().strip())
names=[]
for _ in range(N):
    names.append(input().lower())
dic={}
names=sorted(names)
for x in names:
    tot=0
    for i in x:
        tot+= (ord(i)-96)
        out= tot*(names.index(x)+1)
        dic.update({x:out})

for _ in range(int(input())):
    print(dic[input().lower()])