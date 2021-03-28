N = int(input())
A = list(map(int ,input().split()))

mod = 998244353

A.sort()

ans = 0
s = 0

for i in range(N):
    ans = (ans + A[i]*s + A[i]**2) % mod
    s = (2*s + A[i]) % mod

print(ans)