n, m = map(int, input().split())
con = []
for i in range(m):
    con.append(list(map(int, input().split())))

k = int(input())
peo = []
for i in range(k):
    peo.append(list(map(int, input().split())))

# 全探索

k2 = 1 << k

ans = 0

for s in range(k2):
    dish = [0] * n
    for i in range(k):
        if (s>>i) & 1:
            dish[peo[i][0] - 1] += 1
        else:
            dish[peo[i][1] - 1] += 1
    
    now = 0
    for i in range(m):
        if dish[con[i][0] - 1] == 0 or dish[con[i][1] - 1] == 0:
            continue
        now += 1
    
    ans = max(ans, now)

print(ans)
