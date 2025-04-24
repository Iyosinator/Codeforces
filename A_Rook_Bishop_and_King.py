a,b,c,d=map(int,input().split())
k=0

if a==c or b==d:
    k=1
else:
    k=2
if (a+b) % 2 != (c+d) % 2:
    s=0
elif abs(a-c) == abs(b-d):
    s=1
else:
    s=2

print(k,s, max(abs(a-c), abs(b-d)))