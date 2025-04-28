t = int(input())
x_value,y_value,z_value = 0,0,0
tx = 0
ty = 0
tz = 0

for i in range(t):
    x,y,z = list(map(int,input().split()))

    tx += x
    ty += y
    tz += z


if tx == ty == tz == 0:
    print('YES')
else:
    print('NO')



