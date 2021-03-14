import copy

n, m, q = map(int, input().split())
wv = [list(map(int, input().split())) for i in range(n)]
x = list(map(int, input().split()))

wv.sort()

for _ in range(q):
    l, r = map(lambda x: int(x) - 1, input().split())

    tmp_wv = copy.copy(wv)
    ans = 0

    useX = x[:l]+x[r+1:]
    useX.sort()

    for box in useX:
        value = 0
        index = -1
        for i in range(len(tmp_wv)):
            if tmp_wv[i][0] <= box:
                if value < tmp_wv[i][1]:
                    value = tmp_wv[i][1]
                    index = i
        if index != -1:
            ans += value
            tmp_wv.pop(index)
    
    print(ans)