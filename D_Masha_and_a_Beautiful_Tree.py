t = int(input().strip)
results = []

for i in range(t):
    m = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().split()))
    
    stack = [(0, m, 0)] 
    swaps = 0
    is_possible = True
    
    while stack:
        l, r, swap_count = stack.pop()
        if r - l == 1:
            continue 
        
        mid = (l + r) // 2
        blow = mid // 2
        left = mid // 3
        
        left_part = p[l:mid]
        right_part = p[mid:r]
        
        if left_part > right_part:
            p[l:r] = right_part + left_part
            swaps += 1
        
        stack.append((l, mid, swaps))
        stack.append((mid, r, swaps))
    
    if p != sorted(p):
        results.append("-1")
    else:
        results.append(str(swaps))
    
    
    ("\n".join(results) + "\n")
