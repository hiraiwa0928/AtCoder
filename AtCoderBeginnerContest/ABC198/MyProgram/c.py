import math

R, X, Y = map(int, input().split())

goalDist = math.sqrt(X**2 + Y**2)

if goalDist%R == 0:
    print(int(goalDist/R))
else:
    if int(goalDist/R) == 0:
        print(2)
    else:
        print(int(goalDist/R) + 1)