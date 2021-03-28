import math, cmath

N = int(input())
x0, y0 = map(int, input().split())
xN2, yN2 = map(float, input().split())

# p0の複素平面上の座標
p0 = complex(x0, y0)
# pN/2の複素平面上の座標
pN2 = complex(xN2, yN2)
# 正N角形の中心の座標
o = (p0+pN2)/2
# cmath.rect(絶対値、偏角)
r = cmath.rect(1, 2*math.pi/N)
# 原点を中心に回転させられるようにp0-oとし、
# rを用いて回転させ、元の座標に戻す
a = (p0-o) * r + o

print(f'{a.real:.10f} {a.imag:.10f}')