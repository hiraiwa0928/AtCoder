# WA
import copy
n, m, q = map(int, input().split())
nimotu = [list(map(int, input().split())) for i in range(n)]
x = list(map(int, input().split()))

nimotu.sort()

for i in range(q):

    useX = copy.copy(x)
    nimo = copy.copy(nimotu)

    query = list(map(int, input().split()))
    query[0] -= 1
    query[1] -= 1

    useX = useX[0:query[0]] + useX[query[1]+1:]
    
    useX.sort()
    ans = 0

    for i in range(len(useX)):
        index = -1
        for j in range(len(nimo)):
            if useX[i] >= nimo[j][0]:
                index = j
        if index == -1:
            break
        value = 0
        valueIndex = -1
        for k in range(0, index + 1):
            if value < nimo[k][1]:
                value = nimo[k][1]
                valueIndex = k
        ans += value
        if valueIndex != -1:
            nimo.pop(valueIndex)
    print(ans)
