
# EXEMPLU 1:
# o functie simpla care ne printeaza ceva pe ecran si nu returneaza
# nu ne da nici un raspuns (nu are retunr/ nu returneaza)
# nu are parametri
def printGeeting ():
    print('Buna ziua! Bine ati venit!')


# EXEMPLU 2:
# o functie care saluta clientul in functie de numele lui
# nu ne da nici un raspuns (nu are retunr/ nu returneaza)
# are nevoie de parametri

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')


# EXEMPLU 3:
# o functie care calculeaza media a 3 numere
# ne da un raspuns - suma numerelor, va avea return (o functie returneaza)
# ce tip de date va avea raspunsul? 3 + 5 = 8 => int
# are nevoie de parametri
def mediaNr(a, b, c):
    return (a + b + c) / 3


# EXEMPLU 4:
# o functie care ne da valoarea lui pi
# ne da un raspuns
# raspunsul va fi double
# nu are nevoie de parametri
def piValue():
    return 3.14


# EXERCITIU:
# daca persoana e majora returnati true, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False


# zona de alepare (ca si cum ar fi un desktop)

# print EXEMPLU 1:
printGeeting()
printGeeting()
print()


# print EXEMPLU 2:
printGreetingByName('Sima', 'Elisabeta')
printGreetingByName('Varga', 'Lorand')
print()


# print EXEMPLU 3:
print(mediaNr(3, 3, 4))
print((mediaNr(123,3251,1125)))
print()


# print EXEMPLU 4:
print(piValue())
print()


# print EXERCITIU:
print(verificareMajor(17))
print(verificareMajor(18))
# se ia varsta utilizatorului
age = int(input('Introduceti varsta dumneavoastra: '))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie!')
else:
    print('Nu ai varsta minima (18 ani) necesara pentru a paria')

