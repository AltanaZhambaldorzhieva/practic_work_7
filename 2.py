st = input('Слово: ')
k = ''
for _ in st:
    if _ in ['p', 'b', 'i', 'l']:
        k += _
print(k[1::])

