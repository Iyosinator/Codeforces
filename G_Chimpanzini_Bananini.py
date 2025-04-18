from collections import deque

t = int(input())

for i in range(t):
    q = int(input())
    dq = deque()
    reversed_flag = False
    total_sum = 0
    r_value = 0

    for _ in range(q):
        query = list(map(int, input().split()))
        s = query[0]

        if s == 3:
            k = query[1]
            m = len(dq)
            r_value += k * (m + 1)
            total_sum += k
            if not reversed_flag:
                dq.append(k)
            else:
                dq.appendleft(k)
            print(r_value)
        elif s == 1:
            m = len(dq)
            if m == 0:
                print(0)
                continue
            if not reversed_flag:
                x = dq.pop()
                dq.appendleft(x)
            else:
                x = dq.popleft()
                dq.append(x+1)
            r_value += total_sum - m * x
            print(r_value)
        elif s == 2:
            m = len(dq)
            r_value = (m + 1) * total_sum - r_value
            reversed_flag = not reversed_flag
            print(r_value)
