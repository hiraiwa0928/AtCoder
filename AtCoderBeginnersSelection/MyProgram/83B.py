n, a, b = map(int, input().split())

ans = 0

for i in range(1, n+1):
    num = list(map(int, str(i)))
    n = sum(num)
    if n >= a and n <= b:
        ans += i

print(ans)