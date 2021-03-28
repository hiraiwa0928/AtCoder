H, W, X, Y = map(int, input().split())
S = [list(map(str, input())) for _ in range(H)]

X -= 1
Y -= 1

ans = 1

for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    tmpX = X
    tmpY = Y
    while True:
        tmpX += i
        tmpY += j
        if not (0 <= tmpX < H and 0 <= tmpY < W):
            break
        if S[tmpX][tmpY] == '#':
            break
        ans += 1

print(ans)