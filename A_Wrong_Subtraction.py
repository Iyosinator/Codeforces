n,k = map(int,input().split())

i = 0
ans = n

while i < k:
    ans = str(ans)
    if ans[-1] == "0":
        ans = int(ans) // 10
    else:
        ans = int(ans) - 1
    i+= 1

print(ans)
