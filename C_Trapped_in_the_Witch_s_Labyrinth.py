import sys

input = sys.stdin.readline

q = int(input().strip())
for i in range(q):
    n, m = map(int, input().strip().split())
    grid = [input().strip() for i in range(n)]


    vis = [[0] * m for _ in range(n)]
   
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    i = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0), "?": (0, 0)}

    def inbound(r, c):
        return 0 <= r < n and 0 <= c < m

    stack = []

    for i in range(n):
        if grid[i][0] == "L":   
            vis[i][0] = 1
            stack.append((i, 0))
        
     
        if grid[i][m - 1] == "R":
            vis[i][m - 1] = 1
            stack.append((i, m - 1))

            
    for j in range(m):
        if grid[0][j] == "U":
            vis[0][j] = 1
            stack.append(0, j)
        if grid[n - 1][j] == "D":
            vis[n - 1][j] = 1
            stack.append(n - 1, j)
    
    while stack:
        row, col = stack.pop()
        for dr, dc in directions:
            r = dr + row
            c = dc + col
            
            if inbound(r, c) and vis[r][c] == 0:
                dr2, dc2 = ind[grid[r][c]]
                if r + dr2 == row and c + dc2 == col:
                    vis[r][c] = 1
                    stack.append((r, c))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "?":
                f = 1
                for dr, dc in directions:
                    r = i + dr
                    c = j + dc
                    if inbound(r, c):
                        f &= vis[r][c]
                vis[i][j] = f

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += (vis[i][j] ^ 1)

    #print(ans)
