n = int(input())
info = [list(map(int, input().split())) for i in range(n)]

info = sorted(info)
value = -1

for i in range(n):
    if info[i][2] - info[i][0] > 0:
        if value == -1:
            value = info[i][1]
        elif value >= info[i][1]:
            value = info[i][1]

print(value)