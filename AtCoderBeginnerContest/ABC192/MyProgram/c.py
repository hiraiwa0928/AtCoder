n, k = map(int, input().split())
num = list(str(n))

for i in range(k):
    minList = []
    maxList = []
    n = [int(num[i]) for i in range(len(num))]
    minList.extend(sorted(num))
    n = [int(num[i]) for i in range(len(num)) if num[i] != '0']
    maxList.extend(sorted(n, reverse = True))
    minNum = 0
    maxNum = 0
    for j in range(len(minList)):
        minNum += int(minList[j]) * 10 ** (len(minList) - j - 1)
    for j in range(len(maxList)):
        maxNum += int(maxList[j]) * 10 ** (len(minList) - j - 1)
    num = list(str(maxNum - minNum))

[print(num[i], end = '') for i in range(len(num))]
print()