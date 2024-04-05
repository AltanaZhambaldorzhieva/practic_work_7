import math
n = int(input('Объем: '))
n_ = int(math.cbrt(n))
for i in range(1, n_ + 1):
    if i**3 < n:
        print(i**3)
