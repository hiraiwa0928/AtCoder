N = str(input())

n = ''
index = -1
for i in range(len(N)-1, -1, -1):
    if N[i] == '0':
        index = i
    else:
        break

if index == -1:
    index = len(N)

for i in range(index):
    n += N[i]

flag = True

for i in range(len(n)//2):
    if n[i] != n[len(n)-i-1]:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')