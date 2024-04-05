import math
a = int(input('Введите число: '))
n = math.sqrt(a)

while not (n*n == a):
    a = int(input('Введите число: '))
    n = math.sqrt(a)
else:
    print('Число явл полным квадратом ура')



