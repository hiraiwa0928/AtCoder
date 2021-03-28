# WA
N = int(input())
A = list(map(int, input().split()))

ans = float('INF')

ALL = 1 << N

for x in range(ALL):
    if x == 0 or x == ALL - 1:
        continue
    bit1 = 0
    bit2 = 0
    for i in range(N):
        if x>>i&1:
            bit1 |= A[i]
        else:
            bit2 |= A[i]
    ans = min(ans, bit1^bit2)

print(ans)