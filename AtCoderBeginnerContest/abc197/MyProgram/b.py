H, W, X, Y = map(int, input().split())
S = [list(map(str, input())) for _ in range(H)]

X -= 1
Y -= 1

cnt = 0

if S[X][Y] == '.':
    cnt += 1

for i in range(X-1, -1, -1):
    if S[i][Y] == '.':
        cnt += 1
    else:
        break

for i in range(X+1, H):
    if S[i][Y] == '.':
        cnt += 1
    else:
        break

for i in range(Y-1, -1, -1):
    if S[X][i] == '.':
        cnt += 1
    else:
        break

for i in range(Y+1, W):
    if S[X][i] == '.':
        cnt += 1
    else:
        break

print(cnt)