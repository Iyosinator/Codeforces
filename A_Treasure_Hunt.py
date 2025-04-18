t = int(input())
for _ in range(t):
    x, y, a = map(int, input().split())
    target = 2 * a + 1
    if target % (2 * (x + y)) <= 2 * x:
        print("NO")
    else:
        print("YES")
    
    '''

        x, y, a = map(int, input().split())
        depth = a + 0.5
        buried = 0
        turn = 1

        while buried < depth:
            if turn % 2 == 1: 
                buried += x
            else: 
                buried += y

            if buried >= depth:
                break
            turn += 1

        if turn % 2 == 1:
            print("NO")  
        else:
            print("YES")  
    '''