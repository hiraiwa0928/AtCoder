N = int(input())
A = list(map(int, input().split()))

mod = 998244353

A.sort()

ans = 0

for i in range(N-1):
    ans += (A[i] ** 2) % mod
    num = 1
    for j in range(i+1, N):
        ans += ((A[i] * A[j] * num)) % mod
        num *= 2

ans += (A[N-1] ** 2) % mod

print(int(ans%mod))