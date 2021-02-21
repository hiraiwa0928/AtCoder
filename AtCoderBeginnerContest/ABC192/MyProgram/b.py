s = list(input())

kisu = 0
gusu = 0

for i in range(len(s)):
    if (i+1) % 2 == 1:
        if s[i].isupper():
            kisu = 1
    else:
        if s[i].islower():
            gusu = 1

if kisu == 0 and gusu == 0:
    print('Yes')
else:
    print('No')