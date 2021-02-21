def g1(numList):
    numSort = sorted(numList)
    num = [numSort[i] for i in range(len(numSort)) if numSort[i] != 0]
    numMin = 0
    for i in range(len(num)):
        numMin += num[i] * 10 ** (len(num) - i - 1)
    
    return numMin

def g2(numList):
    numSort = sorted(numList, reverse = True)
    numMax = 0
    for i in range(len(numSort)):
        numMax += numSort[i] * 10 ** (len(numSort) - i - 1)
    
    return numMax

def numList(n):
    n = list(str(n))
    n = [int(n[i]) for i in range(len(n))]

    return n

if __name__ == '__main__':
    n, k = map(int, input().split())

    for i in range(k):
        num = numList(n)
        aMin = g1(num)
        aMax = g2(num)
        n = aMax - aMin
    
    print(n)