t = int(input())

counter = 0
for i in range(t):
    p,v,t = map(int,input().split())

    if (p+v == 2 or p+t == 2 or t+v == 2):
        counter += 1


print(counter)

   
