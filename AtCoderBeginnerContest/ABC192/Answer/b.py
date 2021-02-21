s = input()

odd = True
even = True

for i in range(len(s)):
    if (i+1)%2 == 1:
        if s[i].isupper():
            odd = False
    else:
        if s[i].islower():
            even = False

if odd == True and even == True:
    print('Yes')
else:
    print('No')