
'''
Flow control:
if; else (evalueaza conditii si bifurca codul in functie de rezultat
'''

# if
print('exemplu if:') # if
# EXERCITIU: radioul
# prin boolean invat calculatorul daca piesa e faina sau nu (adevarat/fals)
piesaFaina = True
print('pornim radioul')
if piesaFaina == True:
    print('dau mai tare radioul')
    print('incep sa fredonez piesa')

print('oprim radioul')
print(' ')


# if else
print('exemplu if else:') # if else
# EXERCITIU: daca nr este par printam acest lucru, altfel printam impar

nr = 2
# ce inseamna par? => se imparte exact la 2
# ce inseamna ca se imparte la 2? => ne da rest 0
if nr % 2 == 0:
    print('numarul este par')
else:
    print('numarul este impar')

if nr > 0:
    print('numarul este pozitiv')
else:
    print('numarul nu este pozitiv')

varsta = 18
# EXERCITIU: daca utilizatorul are 18 ani poate paria, daca nu are atunci nu poate
if varsta >= 18:
    print('Felicitari, te incadrezi in varsta necesara pentru a paria!')
else:
    print('Ne pare rau, inca esti minor si nu ai dreptul sa pariezi!')
print(' ')


# if, else if, else (daca, altfel daca, altfel)
print('exemplu if, else if, else:') # if, else if, esle
# EXERCITIU: cum ne saluta robotelul in functie de ora?

# 1. creem variabila ora, luam date de la tastatua - prin comanda: input
# 2. ne asiguram ca sunt transformate din string in int! - prin comanda : float('pt zecimale') respectiv int('pt nr intreg')
ora = float(input('Introdu ora:'))

if ora < 0:
    print('ora invalida')
    print('introdu o ora intre 0-24')
elif ora > 24:
    print('ora invalida')
    print('introdu o ora intre 0-24')
elif ora < 12:
    print('Buna dimineata!')
elif ora <= 17:
    print('Buna ziua!')
elif ora <= 18:
    print('Buna seara!')
else:
    print('Ne pare rau am inchis')


# CTRL + / - pentru a comenta toate liniile de text

optiunea = float(input('Tasteaza tasta:'))

if optiunea == 0:
    print('Ati revenit la meniul anterior')
elif optiunea == 1:
    print ('Ati ales limba Romana')
elif optiunea == 2:
    print ('Ati ales limba Engleza')
else:
    print ('Nu am indentificat aceasta comanda, te rog mai incearca')
