import math as m

for degree in range(0, 181, 10):
    print(f"sin({degree:3d}) = {m.sin(m.radians(degree)):.3f}, cos({degree:3d}) = = {m.cos(m.radians(degree)):.3f}, tan({degree:3d}) = = {m.tan(m.radians(degree)):.3f}")