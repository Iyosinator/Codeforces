from collections import deque
import sys

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque()
center = (2,2)

def inbound(r,c):
    return  0 <= r < 5 and 0 <= c < 5

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            start = (i,j)
            break

queue.append((start[0],start[1],0))
visited = set()

visited.add((start[0],start[1]))

while queue:
    r,c,dist = queue.popleft()

    if (r,c) == center:
        print(dist)
        break

    for dr,dc in directions:
        nr,nc = r + dr, c + dc

        if inbound(nr,nc) and (nr,nc) not in visited:
            visited.add((nr,nc))
            queue.append((nr,nc,dist+1))



