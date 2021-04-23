import itertools

S = []
useAlpha = []
for i in range(3):
    s = list(map(str, input()))
    S.append(s)
    useAlpha.extend(s)

useAlpha = list(set(useAlpha))

if len(useAlpha) > 10:
    print('UNSOLVABLE')
    exit()

dict = {}

judge = False

for c in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    for i in range(len(useAlpha)):
        dict[useAlpha[i]] = c[i]
    N = [0, 0, 0]
    NG = False
    for i in range(3):
        for j in range(len(S[i])):
            if j == 0 and dict[S[i][j]] == 0:
                NG = True
                break
            N[i] += dict[S[i][j]] * 10**(len(S[i])-j-1)
        if NG:
            break
    if N[0] + N[1] == N[2] and not NG:
        judge = True
        break

if judge:
    for i in range(3):
        print(N[i])
else:
    print('UNSOLVABLE')