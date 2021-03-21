# WA
N, M = map(int, input().split())
S = []
for _ in range(N):
    s = list(map(int, input()))
    S.append(s)

score = [0] * N

k = 1 << (M)

cnt = 0

for x in range(k):
    for n in range(N):
        for i in range(M):
            if (x>>i) & 1:
                if S[n][i] == 1:
                    score[n] += 1
            else:
                if S[n][i] == 0:
                    score[n] += 1
    match = False
    AllScore = [0]*(M+1)
    for s in range(N):
        if score[s] == 0:
            continue
        AllScore[score[s]] += 1
    
    dic = {}

    for i in range(len(AllScore)):
        if AllScore[i] == 0:
            continue
        if AllScore[i] in dic.keys():
            if dic[AllScore[i]] == 1:
                match = True
                break
        else:
            dic[AllScore[i]] = 1
    if not match:
        cnt += 1
    score = [0] * N

print(cnt)