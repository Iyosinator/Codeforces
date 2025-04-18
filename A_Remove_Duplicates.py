t = int(input())
nums = list(map(int,input().split()))

ans = []

for num in nums:
    if num in ans:
        ans.remove(num)
    ans.append(num)
print(len(ans))
print(*ans)