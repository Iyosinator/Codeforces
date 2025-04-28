n = int(input())
games = input()

anton =  0
danik = 0
for g in games:
    if g == 'A':
        anton += 1
    else:
        danik += 1


if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print('Friendship')
