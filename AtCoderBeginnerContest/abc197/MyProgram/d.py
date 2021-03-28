import math

N = int(input())
x0, y0 = map(int, input().split())
x_t, y_t = map(int, input().split())

centerX = (x0 + x_t)/2
centerY = (y0 + y_t)/2

x0 -= centerX
y0 -= centerY

rot = math.pi/int(N/2)

ansX = math.cos(rot) * x0 + -math.sin(rot) * y0 + centerX
ansY = math.sin(rot) * x0 + math.cos(rot) * y0 + centerY

print(f'{ansX:.10f} {ansY:.10f}')