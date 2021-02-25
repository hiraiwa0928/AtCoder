a, b, c = map(int, input().split())

if c == 0:
    if a >= b+1:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if b >= a+1:
        print('Aoki')
    else:
        print('Takahashi')