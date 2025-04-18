t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum_even = sum_odd = max_even = max_odd = 0
    has_even = has_odd = False
    for num in a:
        if num % 2 == 0:
            sum_even += num
            max_even = max(max_even, num)
            has_even = True
        else:
            sum_odd += num
            max_odd = max(max_odd, num)
            has_odd = True
    original_max = max(a)
    if not has_even or not has_odd:
        print(original_max)
    else:
        print(max(original_max, sum_odd + max_even if has_even else 0, sum_even + max_odd if has_odd else 0))
