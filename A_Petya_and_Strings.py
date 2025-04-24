str1 = input()
str2 = input()

s1 =str1.lower()
s2 =str2.lower()

for i in range (len(s1)):
    if ord(s1[i]) < ord(s2[i]):
        print(-1)
        break
    elif ord(s1[i]) > ord(s2[i]):
        print(1)
        break
else:
    print(0)
    
            