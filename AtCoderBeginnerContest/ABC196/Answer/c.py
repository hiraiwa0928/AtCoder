N = int(input())

cnt = 0

while True:
    if N >= int(str(cnt+1)*2):
        cnt += 1
    else:
        break

print(cnt)