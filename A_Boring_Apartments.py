t = int(input())

for i in range(t):
    x = input()
    n = len(x)
    
    print((int(x[0]) - 1) * 10 + (n * (n + 1)) // 2)
    '''
    ans = (int(x[0]) - 1) * 10

    if len(x) == 1:
        ans += 1
    elif len(x) == 2:
        ans += 3
    elif len(x) == 3:
        ans += 6
    elif len(x) == 4:
        ans += 10
    print(ans)
    '''


    
     