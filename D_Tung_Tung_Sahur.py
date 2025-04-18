t = int(input())

for i in range(t):
    p = input()
    s = input()

    n, m = len(p), len(s)
    i, j = 0, 0
    ok = True

    while i < n and ok:
        c = p[i]
        cntP = 0
        while i < n and p[i] == c:
            cntP += 1
            i += 1

        if j >= m or s[j] != c:
            ok = False
            break

        cntS = 0
        while j < m and s[j] == c:
            cntS += 1
            j += 1

        if cntS < cntP or cntS > 2 * cntP:
            ok = False
            break

    if i < n or j < m:
        ok = False

    print("YES" if ok else "NO")
