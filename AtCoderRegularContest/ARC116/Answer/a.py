T = int(input())

for _ in range(T):

    n = int(input())

    if n%4 == 0:
        print('Even')
    elif n%2 == 1:
        print('Odd')
    else:
        print('Same')