n,k = map(int,input().split())
nums = list(map(int,input().split()))

comparision_score = nums[k-1]
ans = 0
for num in nums:
    if num >= comparision_score and num > 0:
        ans+=1

print(ans)