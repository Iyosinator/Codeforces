word = input()
vowel = ['a','e','i','o','u','y']
ans = []

word = word.lower()

for w in word:
    if w not in vowel:
        ans.append(w)

print('.'+'.'.join(ans))