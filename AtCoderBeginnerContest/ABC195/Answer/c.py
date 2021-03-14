n = int(input())

x = 1000
ans = 0

while(n>=x):
    ans += n-x+1
    x *= 1000

print(ans)