n = int(input())
a, b = [], []
for i in range(n):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)

min = 100000000000

for i in range(len(a)):
    for j in range(len(b)):
        tmp = 0
        if i == j:
            tmp = a[i] + b[j]
        else:
            if a[i] >= b[j]:
                tmp = a[i]
            else:
                tmp = b[j]
        if min > tmp:
            min = tmp

print(min)