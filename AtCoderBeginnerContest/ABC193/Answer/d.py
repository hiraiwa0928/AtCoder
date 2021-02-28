def score(num):
    score = 0
    for i in range(9):
        score += (i+1) * 10 ** num.count(i+1)
    return score

if __name__ == '__main__':
    k = int(input())
    s = list(map(int, input()[0:4]))
    t = list(map(int, input()[0:4]))

    c = [k] * 9

    for i in range(4):
        c[s[i] - 1] -= 1
        c[t[i] - 1] -= 1

    cnt = 0

    for i in range(9):
        for j in range(9):
            s.append(i+1)
            t.append(j+1)

            taka = score(s)
            aoki = score(t)
            if taka > aoki:
                if i == j:
                    cnt += c[i] * (c[i] - 1)
                else:
                    cnt += c[i] * c[j]
            s.pop()
            t.pop()

    total = sum(c) * (sum(c)-1)
    print(cnt/total)