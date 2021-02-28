import math
n = int(input())

num = []

for i in range(2, int(math.sqrt(n)) + 1):
    for j in range(2, int(math.log(n, i)) + 1):
        num.append(i**j)

print(n - len(set(num)))