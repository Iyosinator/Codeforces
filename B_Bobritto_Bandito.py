t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    k = m if m <= -l else -l
    print(-k, m - k)
