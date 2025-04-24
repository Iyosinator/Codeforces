usernames = input()

unique = set()


for username in usernames:
    if username not in unique:
        unique.add(username)
n = len(unique)

if n%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')