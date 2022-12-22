# 1. for
# Dalmatienii
for i in range(1, 102):
    print(f'Dalmatianul cu nr {i}')

# Dalmatienii din 2 in 2 (ultimul parametru eset pasul)
for i in range(1, 102, 2):
    print(f'Dalmatianul cu nr {i}')


# parcurgerea unei liste cu for prin intermediul indexului
numere = [3, 7, 10, 20, 30]
for i in range(0, len(numere)):
    print(f'indexul curent este {i}, iar numarul atribuit este {numere[i]}')



# 2. for each
suma = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    suma = suma + numar
print(f'Suma este {suma}')


print(' ')
# TEMA: de cate ori apare 3 in [3, 2, 3, 5, 3, 4, 10, etc.]
setNumere = [3, 2, 3, 5, 3, 4, 10, 33, 3, 3, 21, 100, 0, 3]
for numar in range(setNumere.count(3)):
    print(f'Am gasit numarul 3')
print(f'In total am gasit numarul 3 de: {setNumere.count(3)}')
print()


