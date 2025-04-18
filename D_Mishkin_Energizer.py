t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    cntL, cntI, cntT = s.count('L'), s.count('I'), s.count('T')
    m_found = -1
    for m in range(2 * n + 1):
        if (n + m) % 3 == 0:
            k = (n + m) // 3
            if cntL <= k and cntI <= k and cntT <= k:
                m_found = m
                break
    if m_found == -1:
        print(-1)
        continue
    if m_found == 0:
        print(0)
        continue
    deficitL, deficitI, deficitT = k - cntL, k - cntI, k - cntT
    ops = []
    while deficitL or deficitI or deficitT:
        opPerformed = False
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if (s[i] == 'L' and s[i + 1] == 'I') or (s[i] == 'I' and s[i + 1] == 'L'):
                    cand = 'T'
                elif (s[i] == 'L' and s[i + 1] == 'T') or (s[i] == 'T' and s[i + 1] == 'L'):
                    cand = 'I'
                else:
                    cand = 'L'
                if (cand == 'L' and deficitL) or (cand == 'I' and deficitI) or (cand == 'T' and deficitT):
                    ops.append(i + 1)
                    if cand == 'L':
                        deficitL -= 1
                    elif cand == 'I':
                        deficitI -= 1
                    else:
                        deficitT -= 1
                    s.insert(i + 1, cand)
                    opPerformed = True
                    break
        if not opPerformed:
            break
    if deficitL or deficitI or deficitT:
        print(-1)
    else:
        print(len(ops))
        for op in ops:
            print(op)
