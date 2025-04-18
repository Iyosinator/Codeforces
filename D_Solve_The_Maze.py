from collections import deque

def inbound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]

    possible = True


    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if inbound(ni, nj, n, m):
                        if grid[ni][nj] == 'G':
                            possible = False  
                        elif grid[ni][nj] == '.':
                            grid[ni][nj] = '#' 

    if not possible:
        print("No")
        continue

    visited = set()
    q = deque()

    if grid[n-1][m-1] != '#':
        q.append((n-1, m-1))
        visited.add((n-1, m-1))

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if inbound(nx, ny, n, m) and (nx, ny) not in visited and grid[nx][ny] != '#':
                visited.add((nx, ny))
                q.append((nx, ny))

 
    valid = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G' and (i, j) not in visited:
                valid = False
            if grid[i][j] == 'B' and (i, j) in visited:
                valid = False

    print("Yes" if valid else "No")
