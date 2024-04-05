N, K, R = map(int, input().split())
P = 1 + (K / 100)
L = N
k = 1
while L <= R:
    L *= P
    k += 1
print(k)
