from collections import deque
import sys
t = int(sys.stdin.readline())


for i in range(t):
    n = int(sys.stdin.readline())
    nodes = list(map(int, sys.stdin.readline().split()))
    adj_list = [[] for _ in range(n)]

    count = 0
    indegree = [0] * n


    for i in range(n):
        adj_list[i].append(nodes[i]-1)
        indegree[nodes[i]-1] += 1

    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
  
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            for neig in adj_list[node]:
                indegree[neig] -= 1

                if indegree[neig] == 0:
                    queue.append(neig)
        count += 1
    print(count + 2)
    
