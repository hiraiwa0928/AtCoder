import math
n = int(input())
plans = [list(map(int, input().split())) for i in range(n)]

time = plans[0][0] - plans[0][1] - plans[0][2]
if time < 0 or time%2 == 1:
    print('No')
    exit()
x, y = plans[0][1], plans[0][2]

for i in range(1, n):
    disx = abs(plans[i][1] - x)
    disy = abs(plans[i][2] - y)
    time = plans[i][0] - plans[i-1][0] - disx - disy
    if time < 0 or time%2 == 1:
        print('No')
        exit()
    else :
        x = plans[i][1]
        y = plans[i][2]

print('Yes')