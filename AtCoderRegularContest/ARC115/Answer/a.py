N, M = map(int, input().split())
S = [list(map(int, input())) for _ in range(N)]

even, odd = 0, 0

for i in range(N):
    cnt = 0
    for j in range(M):
        if S[i][j] == 1:
            cnt += 1
    if cnt%2 == 0:
        even += 1
    else:
        odd += 1

print(even * odd)