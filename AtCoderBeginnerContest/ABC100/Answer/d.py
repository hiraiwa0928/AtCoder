N, M = map(int, input().split())
x, y, z = [], [], []
for i in range(N):
    n1, n2, n3 = map(int, input().split())
    x.append(n1)
    y.append(n2)
    z.append(n3)

ans = -1

for a in [1, -1]:
    for b in [1, -1]:
        for c in [1, -1]:
            l = []
            for i in range(N):
                l.append(a*x[i]+b*y[i]+c*z[i])
            l.sort(reverse = True)
            ans = max(ans, sum(l[:M]))

print(ans)