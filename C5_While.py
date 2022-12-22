# while = loop sau un ciclu repetitiv (o zona de cod care se repeta atat timp cat o conditie este true)

# EXERCITIU: masina merge cat timp inca are benzina

litriBenzina = 5
while litriBenzina > 0:
    # acceleram
    print('Vrum, vrum!')

    # scadem benzina
    litriBenzina = litriBenzina - 1
    print('Ai ramas cu:', litriBenzina, 'litrii de benzina')

    # aprindem beculetul cand avem <= 3 litri
    if litriBenzina <= 3:
        print("Se aprinde becul rosu. Esti la limita cu benzina!")
        print("Alimenteaza cat mai repede")

print("Stop! Ai ramas fara benzina!")