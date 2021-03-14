n = int(input())

cnt = 0
minNum = 1000
nowNum = 1000
konma = 1
if n >= 1000:
    while True:
        finish = False
        if minNum * 10**3 > n:
            nowNum = n
            finish = True
        else:
            nowNum *= 10**3
        
        cnt += konma * (nowNum - minNum) + 1

        if not finish:
            minNum *= 10**3
            konma += 1
        else:
            break

print(cnt)