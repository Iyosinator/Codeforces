t = int(input())
ans = 0

for i in range(t):
    operations = input()
    
    if operations[0:2] == "++":
        ans += 1
    elif operations[-2:] == "++":
        ans += 1
    elif operations[0:2] == "--":
        ans -= 1 
    elif operations[-2:] == "--":
        ans -= 1
   
print(ans)
