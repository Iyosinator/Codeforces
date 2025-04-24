import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(n)]

    can_escape = [[False] * m for _ in range(n)]
    exit_cells = []

    for r in range(n):
        for c in range(m):
            cell = grid[c][c]
            if cell in DIRECTIONS:
                dr, dc = DIRECTIONS[cell]
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    can_escape[r][c] = True
                    exit_cells.append((r, c))

    queue = deque(exit_cells)
    while queue:
        r, c = queue.popleft()
        for dir_char, (dr, dc) in DIRECTIONS.items():
            pr, pc = r - dr, c - dc
            if 0 <= pr < n and 0 <= pc < m:
                if grid[pr][pc] == dir_char and not can_escape[pr][pc]:
                    can_escape[pr][pc] = True
                    queue.append((pr, pc))

    changed = True
    while changed:
        changed = False
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '?' and not can_escape[r][c]:
                    all_neighbors_good = True
                    for dr, dc in DIRECTIONS.values():
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            if not can_escape[nr][nc]:
                                all_neighbors_good = False
                                break
                    if all_neighbors_good:
                        can_escape[r][c] = True
                        changed = True

    trapped = 0
    for r in range(n):
        for c in range(m):
            if not can_escape[r][c]:
                trapped += 1
    print(trapped)
