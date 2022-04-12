#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void

f = Void()
print("Заданная точка")
Figure.fixed_point = R2Point()
print("\nТочки плоскости")
try:
    while True:
        a = R2Point()
        f = f.add(a)
        print(f"{f.point_is_inside()}")
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
