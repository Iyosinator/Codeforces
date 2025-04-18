from collections import deque

n, m, k = map(int, input().split())
grid = [input().strip() for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


visited = [[False] * m for _ in range(n)]
picture_map = [[-1] * m for _ in range(n)]

queries = [tuple(map(int, input().split())) for _ in range(k)]

for x, y in queries:
    x -= 1  
    y -= 1

    if picture_map[x][y] == -1:
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        component = [(x, y)]
        pictures = 0

        while queue:
            cx, cy = queue.popleft()
            
            for dx, dy in directions:
                nx = cx + dx
                ny = cy + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        component.append((nx, ny))
                    elif grid[nx][ny] == '*':
                        pictures += 1

        for cx, cy in component:
            picture_map[cx][cy] = pictures


    print(picture_map[x][y])
