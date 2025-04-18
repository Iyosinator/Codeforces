n = int(input())
nums = list(map(int,input().split()))

left = 0
right = n -1

sereja = 0
dima = 0

sereja_turn = True
dima_turn = False

turn = 0

while left <= right:
    if nums[left] > nums[right]:
        choosen = nums[left]
        left += 1
    else:
        choosen = nums[right]
        right -=1


    if turn % 2 == 0:
        sereja += choosen
    else:
        dima += choosen
    
    turn += 1

print(sereja,dima)

    