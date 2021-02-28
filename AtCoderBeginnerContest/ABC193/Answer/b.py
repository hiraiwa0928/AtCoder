n = int(input())

ans = -1

for i in range(n):
    a, p, x = map(int, input().split())
    if(x-a >= 1):
        if ans == -1:
            ans = p
        else:
            ans = min(ans, p)

print(ans)