a, b = map(int, input().split())

tmp = a+b

if tmp >= 15 and b >= 8:
    print('1')
elif tmp >= 10 and b >= 3:
    print('2')
elif tmp >= 3:
    print('3')
else:
    print('4')