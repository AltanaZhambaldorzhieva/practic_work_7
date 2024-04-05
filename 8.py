n = int(input())
k = 1
n_1 = 100000000
while n_1 > 1:
    n /= 2
    k += 1
    n_1 = n
    n_1 /= 2
print(k)

