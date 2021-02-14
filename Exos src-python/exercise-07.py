import random

# code 7.1
# affectation d'un nombre aléatoire compris entre 1 et 10 inclus
number = random.randint(1, 10)

# exo 7.1
# en utilisant une boucle for, affichez les nombre de 0 à 99 inclus

# réponse 7.1
print("\n")
print("Exo 7.1")

for i in range(0, 100):
    if i == 99:
       print(i, end = '.') 
    else:
        print(i, end = ', ')

# exo 7.2
# en utilisant une boucle for, affichez les nombre de 0 à 100 inclus

# réponse 7.2
print("\n")
print("Exo 7.2")

for i in range(0, 101):
    if i == 100:
        print(i, end = '.')
    else:
        print(i, end = ', ')

# exo 7.3
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1

# réponse 7.3
print("\n")
print("Exo 7.3")

for i in range(0, 100):
    r = random.randint(1, 10)
    if r == 1:
        print(r, end = ', ')
        
# exo 7.4
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus petit ou égal à 5

# réponse 7.4
print("\n")
print("Exo 7.4")

for i in range(0, 50):
    r = random.randint(1, 10)
    if r <= 5:
        print(r, end = ', ')

# exo 7.5
# en utilisant une boucle for, on tire 20 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus grand ou égal à 6

# réponse 7.5
print("\n")
print("Exo 7.5")

for i in range(0, 20):
    r = random.randint(1, 10)
    if r >= 6:
        print(r, end = ', ')

# exo 7.6
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1 ou égal à 10

# réponse 7.6
print("\n")
print("Exo 7.6")

for i in range(0, 100):
    r = random.randint(1, 10)
    if r == 1 or r == 10:
        print(r, end = ', ')

# exo 7.7
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est compris entre 3 et 8 inclus

# réponse 7.7
print("\n")
print("Exo 7.7")

for i in range(0, 10):
    r = random.randint(1, 10)
    if r >= 3 and r <= 8:
        print(r, end = ', ')

# exo 7.8
# en utilisant une boucle for, on tire 50 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est égal à 7
# affichez la variable `count`

# réponse 7.8
print("\n")
print("Exo 7.8")

count = 0

for i in range(0, 50):
    r = random.randint(1, 10)
    if r == 7:
        count += 1 
        
print(count)

# exo 7.9
# en utilisant une boucle for, on tire 10 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 4
# affichez la variable `count`

# réponse 7.9
print("\nExo 7.9")

count = 0

for i in range(0, 10):
    r = random.randint(1, 10)
    if r <= 4:
        count += 1   
        
print(count)

# exo 7.10
# en utilisant une boucle for, on tire 33 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus grand ou égal à 7
# affichez la variable `count`

# réponse 7.10
print("\nExo 7.10")

count = 0

for i in range(0, 33):
    r = random.randint(1, 10)
    if r >= 7:
        count += 1
        
print(count)

# exo 7.11
# en utilisant une boucle for, on tire 66 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus petit ou égal à 2, ou plus grand ou égal à 9
# affichez la variable `count`

# réponse 7.11
print("\nExo 7.11")

count = 0

for i in range(0, 66):
    r = random.randint(1, 10)
    if r <= 2 or r >= 9:
        count += 1 
        
print(count)

# exo 7.12
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est compris entre 2 et 9 inclus
# affichez la variable `count`

# réponse 7.12
print("\nExo 7.12")

count = 0

for i in range(0, 100):
    r = random.randint(1, 10)
    if r >= 2 and r <= 9:
        count += 1   
        
print(count)

# exo 7.13
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 99 inclus

# réponse 7.13
print("\nExo 7.13")

for i in range(1, 100):
    if i % 2 == 0:
        print(i)

# exo 7.14
# en utilisant une boucle for, affichez tous les nombre pairs, de 1 à 100 inclus

# réponse 7.14
print("\nExo 7.14")

for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} est un nombre pair")

# exo 7.15
# en utilisant une boucle for, affichez tous les nombres divisibles par 3, de 2 à 99 inclus

# réponse 7.15
print("\nExo 7.15")

for i in range(2, 100):
    if i % 3 == 0:
        print(f"{i} est divisible par 3")

# code 7.2
# pour calculer la puissance 2 d'un nombre, on peut le multiplier par lui-même
# number = 5
# print(number * number)
# mais on peut aussi l'élever à la puissance 2 avec l'opérateur puissance `**`
# print(number ** 2)

# exo 7.16
# en utilisant une boucle for, affichez la puissance 2 des nombres de 0 à 99 inclus

# réponse 7.16
print("\nExo 7.16")

for i in range(0, 100):
    print(f"{i}² = {i ** 2}")

# code 7.3
# pour calculer la puissance 3 d'un nombre, on peut l'élever à la puissance 3 avec l'opérateur puissance `**`
# number = 3
# print(number ** 3)

# exo 7.17
# en utilisant une boucle for, affichez la puissance 3 des nombres de 1 à 100 inclus

# réponse 7.17

print("\nExo 7.17")

for i in range(1, 101):
    print(f"{i}³ = {i ** 3}")

# exo 7.18
# dans une boucle while, on tire un nombre entier `r` au hasard entre 1 et 100 inclus
# boucler jusqu'à ce que la valeur 100 soit tirée au hasard

# réponse 7.18
print("\nExo 7.18")

r = 0
while r != 100:
    r = random.randint(1, 100)

print("La valeur 100 a été tirée au hasard !")

# Méthode plus longue avec break:
# num = 100
# while True:
#     r = random.randint(1, 100)
#     if r == num:
#         break
#     print(r)

# print("100 a été tiré au hasard !")
    