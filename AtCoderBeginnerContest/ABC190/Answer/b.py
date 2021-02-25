n, s, d = map(int, input().split())

flag = False

for i in range(n):
    x, y = map(int, input().split())
    if s > x and d < y:
        flag = True

print('Yes') if flag else print('No')