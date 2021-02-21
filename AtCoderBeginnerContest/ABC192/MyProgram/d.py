x = list(map(int, input()))
m = int(input())

d = max(x)
cnt = 0

while(True):
    d += 1
    num = 0
    for i in range(0, len(x)):
        num += x[i] * d ** (len(x) - i - 1)
    if num > m:
        break
    cnt += 1

print(cnt)
