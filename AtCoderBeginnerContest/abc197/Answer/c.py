N = int(input())
A = list(map(int, input().split()))

ALL = 1 << (N-1)

ans = float('INF')

for x in range(ALL):
    now = 0
    o = 0
    for i in range(N):
        o |= A[i]
        if x>>i&1:
            now ^= o
            o = 0
    now ^= o
    ans = min(ans, now)

print(ans)