# WA
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for i in range(k)]

con = [0] * n

for i in range(m):
    for j in range(2):
        con[ab[i][j] - 1] += 1

whereball = [0] * n

for i in range(k):
    for j in range(2):
        whereball[cd[i][j] - 1] += 1

ball = [0] * n

for i in range(k):

    if ball[cd[i][0] - 1] == 0 and ball[cd[i][1] -1] == 0:
        if whereball[cd[i][0] - 1] >= whereball[cd[i][1] -1]:
            ball[cd[i][1] -1] += 1
            whereball[cd[i][0] - 1] -= 1
            whereball[cd[i][1] -1] -= 1
        else:
            ball[cd[i][0] - 1] += 1
            whereball[cd[i][0] - 1] -= 1
            whereball[cd[i][1] -1] -= 1
    elif ball[cd[i][0] - 1] == 0 or ball[cd[i][1] -1] == 0:
        if ball[cd[i][0] - 1] == 0:
            ball[cd[i][0] - 1] += 1
            whereball[cd[i][0] - 1] -= 1
            whereball[cd[i][1] -1] -= 1
        elif ball[cd[i][1] -1] == 0:
            ball[cd[i][1] - 1] += 1
            whereball[cd[i][0] - 1] -= 1
            whereball[cd[i][1] -1] -= 1
    else:
        if whereball[cd[i][0] - 1] > whereball[cd[i][1] -1]:
            ball[cd[i][1] - 1] += 1
            whereball[cd[i][0] - 1] -= 1
            whereball[cd[i][1] -1] -= 1
        elif whereball[cd[i][0] - 1] < whereball[cd[i][1] -1]:
            ball[cd[i][0] - 1] += 1
            whereball[cd[i][0] - 1] -= 1
            whereball[cd[i][1] -1] -= 1
        else :
            if con[cd[i][0] - 1] >= con[[i][1] - 1]:
                ball[cd[i][1] - 1] += 1
                whereball[cd[i][0] - 1] -= 1
                whereball[cd[i][1] -1] -= 1
            else:
                ball[cd[i][0] - 1] += 1
                whereball[cd[i][0] - 1] -= 1
                whereball[cd[i][1] -1] -= 1

cnt = 0

for i in range(m):
    if ball[ab[i][0] - 1] >= 1 and ball[ab[i][1] - 1] >= 1:
        cnt += 1

print(cnt)