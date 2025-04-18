n, d = map(int, input().split())
s = input()

min_jumps = float('inf')
visited = [False] * n

def dfs(pos, jumps):
    
    global min_jumps
    if pos == n - 1:
        min_jumps = min(min_jumps, jumps)
        return

    visited[pos] = True

    for i in range(1, d + 1):
        next_pos = pos + i
        if next_pos < n and s[next_pos] == '1' and not visited[next_pos]:
            dfs(next_pos, jumps + 1)

    visited[pos] = False  # backtrack

dfs(0, 0)

print(min_jumps if min_jumps != float('inf') else -1)
