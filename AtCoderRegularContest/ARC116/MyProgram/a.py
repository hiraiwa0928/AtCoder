import math
T = int(input())

for _ in range(T):

    evenNum = 0
    oddNum = 0

    n = int(input())
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n%i == 0:
            if i%2 == 0:
                evenNum += 1
            else:
                oddNum += 1
            if int(n/i)%2 == 0:
                evenNum += 1
            else:
                oddNum += 1
    
    if evenNum == oddNum:
        print('Same')
    elif evenNum > oddNum:
        print('Even')
    else:
        print('Odd')