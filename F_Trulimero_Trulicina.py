t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    grid = []
    
    if k % 2 == 0 and m % 2 == 0:
        pairs = [(i + 1, k - i) for i in range(k // 2)]
        cycle_length = len(pairs)
        for i in range(n):
            pair = pairs[i % cycle_length]
            cycle_group = i // cycle_length
            start = 0 if cycle_group % 2 == 0 else 1
            row = []
            for j in range(m):
                if j % 2 == 0:
                    row.append(pair[start % 2])
                else:
                    row.append(pair[(start + 1) % 2])
            grid.append(row)
    else:
        for i in range(n):
            row = []
            for j in range(m):
                val = (i + j) % k + 1
                row.append(val)
            grid.append(row)
    
    for row in grid:
        print(' '.join(map(str, row)))