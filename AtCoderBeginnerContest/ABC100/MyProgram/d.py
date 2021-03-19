# TLE and WA
N, M = map(int, input().split())
x, y, z = [], [], []
for _ in range(N):
    n1, n2, n3 = map(int, input().split())
    x.append(n1)
    y.append(n2)
    z.append(n3)

app = tas = pop = 0

# 最初のM個のケーキの最大値を算出
for i in range(M):
    app += x[i]
    tas += y[i]
    pop += z[i]

ans = abs(app) + abs(tas) + abs(pop)

notUse = []

# M+1~N個までのケーキで最大値を求める
for i in range(N-M):
    # M+i+1個までの中で選ばないケーキをjとする
    nowMaxValue = -1
    notUseIndex = -1
    for j in range(M+i+1):
        if j in notUse:
            continue
        app = tas = pop = 0
        for k in range(M+i+1):
            if k in notUse:
                continue
            if k == j:
                continue
            app += x[k]
            tas += y[k]
            pop += z[k]
        tmpValue = abs(app) + abs(tas) + abs(pop)
        if tmpValue > nowMaxValue:
            nowMaxValue = tmpValue
            notUseIndex = j
    if nowMaxValue > ans:
        ans = nowMaxValue
        notUse.append(notUseIndex)
    else:
        notUse.append(M+i)

print(ans)