t = int(input())


for i in range(t):
    grid = [input().strip() for _ in range(3)]

    for i in range(3):
        for j in range(3):
            if grid[i][j] == '?':
                j = grid[i].index('?')
                letters = [grid[i][(j+1)%3], grid[i][(j+2)%3]]
                
                if 'A' in letters and 'B' in letters:
                    print('C')
                elif 'A' in letters and 'C' in letters:
                    print('B')
                elif 'B' in letters and 'C' in letters:
                    print('A')