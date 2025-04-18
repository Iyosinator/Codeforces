from bisect import bisect_left
from collections import defaultdict

MAX_VAL = 100005
divisors = [[] for _ in range(MAX_VAL)]

for i in range(2, MAX_VAL):
    for j in range(i, MAX_VAL, i):
        divisors[j].append(i)

t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    positions = defaultdict(list)

    for idx in range(n):
        positions[array[idx]].append(idx)

    for i in range(q):
        k, left, right = map(int, input().split())
        left -= 1
        right -= 1

        current_idx = left
        result = 0
        while current_idx <= right:
            if k == 1:
                result += right - current_idx + 1
                break

            next_idx = right + 1
            div_list = divisors[k] if k < MAX_VAL else []

            if not div_list:
                temp = k
                for divisor in range(2, int(k ** 0.5) + 1):
                    if temp % divisor == 0:
                        div_list.append(divisor)
                        while temp % divisor == 0:
                            temp //= divisor
                if temp > 1:
                    div_list.append(temp)

            for divisor in div_list:
                if divisor in positions:
                    pos = positions[divisor]
                    idx = bisect_left(pos, current_idx)
                    if idx < len(pos) and pos[idx] < next_idx:
                        next_idx = pos[idx]

            result += (next_idx - current_idx) * k
            if next_idx > right:
                break

            while k % array[next_idx] == 0:
                k //= array[next_idx]

            result += k
            current_idx = next_idx + 1

        print(result)
