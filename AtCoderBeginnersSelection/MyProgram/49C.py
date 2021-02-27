s = input()
words = ['dream', 'dreamer', 'erase', 'eraser']

while(len(s) > 0):
    tmp = s[0:5]
    if tmp == words[0]:
        if s[5:10] == words[2]:
            s = s[5:]
        elif s[0:7] == words[1]:
            s = s[7:]
        else:
            s = s[5:]
    elif tmp == words[2]:
        if s[5:10] == words[0]:
            s = s[5:]
        elif s[0:6] == words[3]:
            s = s[6:]
        else:
            s = s[5:]
        pass
    else:
        print('NO')
        exit()

print('YES')