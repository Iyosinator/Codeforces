n,k,x = map(int,input().split())
balls = list(map(int,input().split()))

max_destroyed = 0


for i in range(n+1):
    b = balls[:i] + [x] + balls[i:]

    total_destroyed = 0
    changed = True


    while changed:
        changed = False
        new_b = []
        j = 0
        while j < len(b):
            L = j
            while j + 1 < len(b) and b[j + 1] == b[L]:
                j += 1
            count = j - L + 1
            if count >= 3:
                total_destroyed += count
                changed = True
            else:
                new_b.extend(b[L:j + 1])
            j += 1
        b = new_b

    if total_destroyed > 0:
        max_destroyed = max(max_destroyed, total_destroyed)

print(max_destroyed)

