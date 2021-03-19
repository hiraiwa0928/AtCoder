N = int(input())
a = list(map(int, input().split()))

cnt = 0

for ele in a:
    while True:
        if ele%2 == 0:
            cnt += 1
            ele /= 2
        else:
            break

print(cnt)