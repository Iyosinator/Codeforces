player = input()

left = 0
count = 1  

for right in range(1, len(player)):
    if player[left] == player[right]:
        count += 1
        left += 1
        if count >= 7:
            break
    else:
        count = 1
        left = right 

if count >= 7:
    print('YES')
else:
    print('NO')
