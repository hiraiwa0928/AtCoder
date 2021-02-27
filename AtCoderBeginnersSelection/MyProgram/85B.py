n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
d = sorted(d, reverse = True)

now = d[0]
cnt = 1

for i in range(1, n):
    if now > d[i]:
        now = d[i]
        cnt += 1

print(cnt)