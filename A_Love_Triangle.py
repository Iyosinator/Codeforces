n = int(input())  # number of planes
f = list(map(int, input().split()))  # who each plane likes

f = [x - 1 for x in f]  # Convert to 0-based indexing

for i in range(n):
    a = f[i]       # plane i likes
    b = f[a]       # plane a likes
    c = f[b]       # plane b likes
    if c == i:     # if plane c likes back to i => triangle!
        print("YES")
        break
else:
    print("NO")
