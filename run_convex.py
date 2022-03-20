#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

f = Void()
try:
    while True:
        a = R2Point()
        print(f"Лежит ли точка внутри выпуклой оболочки? ---> {f.point_is_inside(a)}")
        f = f.add(a)
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
