D, N = map(int, input().split())

num = 0
cnt = 0

if D == 0:
    while N > cnt:
        num += 1
        if num%100 != 0:
            cnt += 1
    print(num)
else:
    judgeNum = 100**D
    while N > cnt:
        num += 1
        if num%judgeNum == 0:
            tmp = num/judgeNum
            if tmp%100 != 0:
                cnt += 1
    print(num)