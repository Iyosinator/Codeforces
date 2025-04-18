t = int(input())

for i in range(t):
    word = input()
    ans = []
    ans.append(word[0])

    for i in range(len(word)):
        if word[i] == " ":
            ans.append(word[i+1])


    print(''.join(ans))