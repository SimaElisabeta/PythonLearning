
# listele in Python pot sa cuprinda elemente de tipuri diferite si au dimensiune dinamica: adica in valoarea variabilei putem introduce: string, int, boolean etc. fara nici o problema

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie') # append = adauga un nou element listei
print(fructe)

# suprascriem un element
fructe[0] = 'para' # suprascriem elementul dand o noua valoare index-ului
print(fructe)

# aflam dimensiunea
print(len(fructe)) # len = lenght

# scoate si ne returneaza ultimul element
last = fructe.pop() # valoare pop scoate din lista elementul si il tine minte => il face doar invizibil nu il sterge complet

print('ultimul element care este invizibil: ', last)
print('lista finala: ', fructe)

# de cate ori apare un element?
print('de cate ori apare 3 in lista?:', fructe.count(3))

# extindem lista (combinam 2 liste)
fructeExotice = ['ananas', 'kiwi']
fructe.extend(fructeExotice)
print('Lista fructe exotice:', fructeExotice)
print('Lista de fructe si fructe exotice este:', fructe)
