tmprch = float(input())
k = 0
while tmprch != 0:
    t_0 = tmprch
    tmprch = float(input())
    if tmprch == 0:
        break
    if tmprch < t_0:
        k += 1
print(k)
