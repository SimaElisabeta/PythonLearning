
# TEMA: de cate ori apare 3 in [3, 2, 3, 5, 3, 4, 10, etc.]
setNumere = [3, 2, 3, 5, 3, 4, 10, 33, 3, 100, 3]
sumDe3 = 0
for numar in setNumere:
    if numar == 3:
        print('Am gasit numarul 3')
        sumDe3 = sumDe3 + 1
print(sumDe3)
print(' ')
# (f'In total am gasit numarul 3 de: {setNumere.count(3)}')



for numar in range (setNumere.count(3)):
    print(f'Am gasit numarul 3')
print(f'In total am gasit numarul 3 de: {setNumere.count(3)}')
print(' ')



# EXERCITIU 1: se da o lista, array. [7, 10, 1, 3, 17, 20, 100, 27, 30, 43]
# printeaza cate elemente sunt divizibile cu 3 si cu 5... 2 printuri

numereA = [7, 10, 1, 3, 17, 20, 100, 27, 30, 43]

counter3 = 0
counter5 = 0

for div in range(0, len(numereA)):
    element = numereA[div]

    if element % 3 == 0:
        print(f'Am gasit un numar divizibil cu 3: {element} ')
        counter3 = counter3 + 1
    if element % 5 == 0:
        counter5 = counter5 + 1
        print(f'Am gasit un numar divizibil cu 5: {element} ')


print(f'Total numere divizibile cu 3: {counter3} ')
print(f'Total numere divizibile cu 5: {counter5} ')
print()


# EXERCITIU 2:
# afla media aritmetica [7, 10, 1, 3, 17, 20, 100, 27, 30, 43]
numereB = [7, 10, 1, 3, 17, 20, 100, 27, 30, 43]

numarCurent = 0

for numarB in numereB:
    print(f'Numarul urmator din Array este {numarB}')
    print(f'Vom aduna {numarB} + {numarCurent}')
    numarCurent = numarCurent + numarB
    print(f'Dupa adunare rezulta totalul de: {numarCurent}')
print(f'Vom imparti: {numarCurent}, la total numere din Array: {len(numereB)}. Astfel rezulta {numarCurent} : {len(numereB)}')

mediaAritmetica = numarCurent / len(numereB)
print(f"Media aritmetica este: {mediaAritmetica}")
print()


# EXERCITIU 3:
# afla care este cel mai mare numar din lista/array [7, 10, 1, 3, 17, 20, 100, 27, 30, 43]
lista = [7, 10, 1, 3, 17, 20, 100, 27, 30, 43]

max = -100
print('Lista mea conine numerele: 7, 10, 1, 3, 17, 20, 100, 27, 30, 43 ')
for nr in lista:
    if nr > max:
        max = nr
        # print(f'Noul numar mai mare este: {nrGasit}')
print(f'Cel mai mare numar din Lista este: {max}')
print()

# EXERCITIU 4:
# afla care este cel mai mic numar din lista/array [43, 7, 10, 3, 17, 20, 100, 1, 27, 30]
listaS = [43, 7, 10, 3, 17, 20, 100, 1, 27, 30]
print('Lista mea conine numerele: 43, 7, 10, 3, 17, 20, 100, 1, 27, 30')

min = 1000000

for nrS in listaS:
    if nrS < min:
        min = nrS
print(f'Cel mai mic numar din Lista este: {min}')
print()



# EXERCITIU 5:
# folosind o bucla for calculeaza cate numere sunt divizibile cu 3 intre 1 - 10000

counter = 0
for nrDiv in range (1, 10001 ):
    if nrDiv % 3 == 0:
        counter = counter + 1

print(f'Total numere divizivbile cu 3 sunt: {counter}')
print()



# EXERCITIU 6:
# se dau 2 array de stringuri, printeaza toate combinatiile din continutul celor 2 array-uri
substantive = ['minge', 'farfurie', 'lampa', 'masa']
adjective = ['mare', 'frumoasa', 'preferata']

for substantiv in substantive:
    for adjectiv in adjective:
        print(f'{substantiv} {adjectiv}')
