import random
t = int(input())
ans = []
for i in range(t):
    l1,r1,l2,r2 = map(int,input().split())

    if l1 == r2:
        r2 = l2
    print(l1,r2)

