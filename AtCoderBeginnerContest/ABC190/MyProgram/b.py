n, s, d = map(int, input().split())
magic = [list(map(int, input().split())) for i in range(n)]

flag = 0

for i in range(n):
    if s > magic[i][0] and d < magic[i][1]:
        flag = 1
        break

if flag == 1:
    print('Yes')
else:
    print('No')