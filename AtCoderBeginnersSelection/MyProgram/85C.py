# TLE
n, y = map(int, input().split())

flag = False

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if 10000*i + 5000*j + 1000*k == y:
                if i+j+k == n:
                    flag = True
                    print(i, j, k)
                    break
                if i+j+k > n:
                    break
        if flag or i+j > n:
            break
    if flag:
        break

if flag == False:
    print(-1, -1, -1)