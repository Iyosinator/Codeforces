t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    ones_g1 = ones_g2 = cnt_b_g1 = cnt_b_g2 = 0
    for i in range(n):
        if (i + 1) % 2 == 1:
            if a[i] == '1': ones_g1 += 1
            if b[i] == '1': ones_g2 += 1
            cnt_b_g2 += 1
        else:
            if a[i] == '1': ones_g2 += 1
            if b[i] == '1': ones_g1 += 1
            cnt_b_g1 += 1
    print("YES" if ones_g1 <= cnt_b_g1 and ones_g2 <= cnt_b_g2 else "NO")
