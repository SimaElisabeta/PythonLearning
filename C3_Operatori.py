
#Recap:
'''
variabile
tipuri de date: string, int, float/double, boolean, char
'''

#Operatori:
'''
artitmetici: +, -, *, /, % (modulo - doar pentru nr intregi=rest)
de comparare < >, == (egal), != (diferit), >=, <=
logici: and (and / si), or (or / sau), ! (not/ inverseaza)
'''


a = 3
b = 5

# operatori aritmetici:
'''
print(a + b) # 3 + 5 = 8
print(a - b) # 3 - 5 = -2
print(a * a) # 3 * 3 = 9
print(15 / a) # 15 / 3 = 5 rezulta 5.0?? de ce?
print(21 % b) # 21 modulo 5 = 4.1 => rest 1
'''

# operatori de comparare:
'''
print(a < b) # 3 este mai mic ca 5 => true
print(a > b) # 3 este mai mare ca 5 => false
print(a == a) # 3 este egal cu 3 => true
print(a != b) # 3 este diferit de 5 => true
print(6 >= b) # 6 este mai mare sau egal cu 5 => true
print(a <= b) # 3 este mai mic sau egal cu 5 => true
'''

# operatori logici:
'''
print(3 == 3 and a > 1)
print(3 < 5 and a == b)
print(2 != 1 or 10 < b)
print(a <= 2 or b == a)
'''