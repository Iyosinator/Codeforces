question = input()


ans = []
for q in question:
    if q.isalnum() == True:
        ans.append(int(q))

ans.sort()

ans = '+'.join(str(num) for num in ans)
print(ans)
