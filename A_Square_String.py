t = int(input())


for i in range(t):
    word = input()
    n = len(word)
    mid = n//2
    left_half = word[0:mid]
    right_half = word[mid:]
    
    if n % 2 == 0 and right_half == left_half:
       print('YES')
    else:
         print('NO')
        
