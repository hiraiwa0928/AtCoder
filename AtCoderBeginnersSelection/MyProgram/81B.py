n = int(input())
a = list(map(int, input().split()))

cnt = 0
finish = False

while(finish == False):
    for i in range(n):
        if a[i]%2 == 0:
            a[i] /= 2
        else:
            finish = True
            break
    cnt += 1

print(cnt - 1)