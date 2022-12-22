
# declaram si initializam un dict-dictionary (map in Java)

noteElevi={'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaygam elemente
noteElevi['Sebi'] = 7

# printam dictul
print(noteElevi)

# aflam note/elemente din interior
print(noteElevi['Gigel'])
print(noteElevi.get('Gigel'))

# actualizam valori
noteElevi['Costel'] = 10
print(noteElevi)

# aflam dimensiunea
print(len(noteElevi))

# stergem valori
noteElevi.pop('Gigel')
print(noteElevi)
print(noteElevi.get('Gigel', 'nu mai avem acest elev'))
print(noteElevi.pop('Gigel', 'nu mai avem acest elev'))

# returneaza doar cheile
print(noteElevi.keys())