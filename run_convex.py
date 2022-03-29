#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

f = Void()
print('Введите координаты точки')
point = R2Point()
print('Введите координаты точек, образующих оболочку')
try:
    while True:
        a = R2Point()
        f = f.add(a)
        t = f.point_is_inside(point)
        print(f"Лежит ли точка внутри выпуклой оболочки? ---> {t}")
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
