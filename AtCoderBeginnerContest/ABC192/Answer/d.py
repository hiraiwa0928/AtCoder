x = list(map(int, input()))
m = int(input())

if len(x) == 1:
    if x[0] <= m:
        print('1')
        exit()
    else:
        print('0')
        exit()
d = max(x)
ac = d
wa = m + 1

while(wa-ac > 1):
    wj = int((ac+wa)/2)
    v = 0
    for i in range(0, len(x)):
        v += x[i] * wj ** (len(x) - i - 1)
    if v <= m:
        ac = wj
    else:
        wa = wj

print(ac - d)