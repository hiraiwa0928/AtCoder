N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

A = [None] * N
B = [None] * N

for i in range(N):
    min = float('INF')
    for j in range(N):
        if min > C[j][i]:
            min = C[j][i]
    B[i] = min

judge = True

for i in range(N):
    A[i] = C[i][0] - B[0]
    if A[i] < 0:
        judge = False
        break
    for j in range(1, N):
        if C[i][j] != A[i] + B[j]:
            judge = False

if judge:
    print('Yes')
    print(*A)
    print(*B)
else:
    print('No')