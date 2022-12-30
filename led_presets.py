# led_presets.py
from time import time
from math import sin
n = (0, 0, 0)
rsin = ((sin(time()) + 1) / 2)
rsin *= 255.0
rsin = int(rsin)
r = (rsin, 0, 0)  # colour
heart = [
    n, n, n, n, n, n, n, n,
    n, r, r, n, n, r, r, n,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    n, r, r, r, r, r, r, n,
    n, n, r, r, r, r, n, n,
    n, n, n, r, r, n, n, n,
    n, n, n, n, n, n, n, n,
]
