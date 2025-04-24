n = int(input())
steps = 0

if n%5 == 0:
    steps += n//5
if n%5 != 0:
    steps += n//5 + 1

print(steps)