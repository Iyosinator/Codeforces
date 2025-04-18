n = int(input())
s = input()

delete = 0

i = 0

while i <= n-3:
    if s[i:i+3] == 'xxx':
        delete += 1
        i+= 1
    else:
        i+= 1
print(delete)
