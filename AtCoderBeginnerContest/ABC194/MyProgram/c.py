import copy
import math
n = int(input())
a = list(map(int, input().split()))

num = []
ans = 0
before = None
for i in range(1, n):
    if i == 1:
        num.append(a[i] - a[i-1])
        before = a[i]
    else:
        num = list(map(lambda x: x-(before - a[i]), num))
        num = list(map(lambda x: math.fabs(x), num))
        num.append(a[i] - a[i-1])
        before = a[i]
    tmp = 0
    for i in range(len(num)):
        if num[i] < 0:
            tmp += -1 * num[i]
        else:
            tmp += num[i]
    ans += int(tmp ** 2)

print(ans)