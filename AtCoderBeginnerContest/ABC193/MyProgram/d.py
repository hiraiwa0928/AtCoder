# WA
k = int(input())
s = input()
t = input()
s = s[:4]
t = t[:4]
s = list(map(int, s))
t = list(map(int, t))

cards = [1*k] * 9
takaCards = [0] * 9
aokiCards = [0] * 9

for i in range(len(s)):
    cards[s[i] - 1] -= 1
    takaCards[s[i] - 1] += 1

for i in range(len(t)):
    cards[t[i] - 1] -= 1
    aokiCards[t[i] - 1] += 1

takaScore, aokiScore = 0, 0

for i in range(9):
    takaScore += (i+1) * 10**takaCards[i]
    aokiScore += (i+1) * 10**aokiCards[i]

ans = 0
maisu = sum(cards)
kakuritu = 1

for i in range(2):
    kakuritu *= (i+1) / (maisu - i)

for i in range(len(cards)):
    if cards[i] == 0:
        continue
    cards[i] -= 1
    takaCards[i] += 1
    for j in range(len(cards)):
        if cards[j] == 0:
            continue
        if cards[j] != 0:
            takaScore = 0
            aokiScore = 0
            aokiCards[j] += 1
            for i in range(9):
                takaScore += (i+1) * 10**takaCards[i]
                aokiScore += (i+1) * 10**aokiCards[i]
            if takaScore > aokiScore:
                ans += kakuritu
        aokiCards[j] -= 1
    takaCards[i] -= 1

print(ans)