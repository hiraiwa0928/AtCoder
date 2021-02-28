import math
n = int(input())

cnt = 0
num = []

for i in range(2, int(math.sqrt(n)) + 2):
    for j in range(2, int(math.sqrt(n)) + 2):
        if i**j > n:
            break
        num.append(i**j)

num = set(num)

print(n - len(num))