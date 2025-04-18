import sys
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
 
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    colors = input()
    
    adj = [[] for _ in range(n+1)]
    for i in range(len(nums)):
        adj[nums[i]].append(i+2)
    ans = 0
 
    @bootstrap
    def dfs(i):
        global ans
        if colors[i-1] == 'W':
            color = 1
        else:
            color = -1
        child = 0
 
        for children in adj[i]:
            temp =  yield dfs(children)
            child += temp
        if color + child == 0:
            ans += 1
       
        yield color + child
 
    dfs(1)
    print(ans)