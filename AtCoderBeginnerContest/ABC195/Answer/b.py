a, b, w = map(int, input().split())

w *= 1000

min = None

if w%b == 0:
    min = int(w/b)
else:
    min = int(w/b) + 1
max = int(w/a)

if max - min < 0:
    print('UNSATISFIABLE')
else:
    print(min, max)