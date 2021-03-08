n = int(input())
a, b = [], []
for i in range(n):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)

ans = 1001001001

for i in range(len(a)):
    for j in range(len(b)):
        now = 0
        if i == j:
            now = a[i] + b[j]
        else:
            now = max(a[i], b[j])
        if ans > now:
            ans = now

print(ans)