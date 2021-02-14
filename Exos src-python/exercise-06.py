# exercise-06.py

# Note pour Daishi : en lançant le Run Python File, il y a la possibilité 
# de lire en même temps et clairement toutes les réponses des exercices 
# avec le numéro des exercices et une phrase accompagnative pour 
# la compréhension des réponses. Même si je sais au final que tu préfère 
# lire seulement la qualité du code sans passer par l'interpréteur 
# pour l'exécution du code ;)

import random

# exo 6.1
# Créez une liste nommée `my_list` contenant un nombre entier, un nombre à virgule flottante, une chaîne de caractères et un booléen

# réponse 6.1
my_list = [10, 3.14, "chat", False]
print(f"Exo 6.1 - Nouvelle liste créée : {my_list}")

# exo 6.2
# Affichez l'élément qui se trouve à la troisième position de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.2
print(f"Exo 6.2 - Elément en 3e position de la liste : {my_list[2]}")

# exo 6.3
# Ajoutez une chaîne de caractères à la liste `my_list` 
# (sans modfier le code d'initialisation) et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.3
print(f"Exo 6.3 - Avant l'ajout de la chaîne de caractères : {my_list}")

my_list.append('chien')

print(f"Exo 6.3 - Après l'ajout de la chaîne de caractères : {my_list}")

# exo 6.4
# Supprimez l'élément qui se trouve en deuxièm position de la liste 
# et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.4
print(f"Exo 6.4 - Avant la suppression de l'élément en 2e position de la \
liste : {my_list}")

del my_list[1]

print(f"Exo 6.4 - Après la suppression de l'élément en 2e position de la \
liste : {my_list}")

# exo 6.5
# Remplacez l'élément qui se trouve en deuxième position de la liste par un nombre entier et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.5
print(f"Exo 6.5 - Avant le remplacement de l'élément en 2e position de la \
liste : {my_list}")

my_list[1] = 50

print(f"Exo 6.5 - Après le remplacement de l'élément en 2e position de la \
liste : {my_list}")

# exo 6.6
# Affichez la taille de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.6
print(f"Exo 6.6 - La taille de la liste est : {len(my_list)}")

# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` 
# puis affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
print(f"Exo 6.7 - Avant la permutation des positions : {my_list}")

temp = my_list[1]
my_list[1] = my_list[3]
my_list[3] = temp 

# Autre méthode :
# my_list[1], my_list[3] = my_list[3], my_list[1]

print(f"Exo 6.7 - Après la permutation des positions : {my_list}")

# Remarque : les exercices suivants nécessitent l'utilisation 
# d'une boucle `for`

# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42]

# réponse 6.8
sum = 0

for num in my_list:
    sum += num
    
print(f"Exo 6.8 - La somme des nombres de la liste : {sum}")

# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9
sum = 0

for num in my_list:
    sum += num
    
print(f"Exo 6.9 - La somme des nombres de la liste : {sum}")

# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
sum = 0

for num in my_list:
    sum += num
avg = sum / len(my_list)

print("Exo 6.10 - La moyenne des nombres de la liste est : " + "%.2f" % avg)

# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et 
# affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11
for i, num in enumerate(my_list):
    if num == 3.14:
        print("Exo 6.11 - l'index de la valeur 3.14 dans la liste est : %d" %i)
        break
        # Autre méthode avec .index():
        # print("Exo 6.11 - l'index de la valeur 3.14 dans la liste est : \
                # %d" %(my_list.index(3.14)))

# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste 
# et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.12
count = 0

for num in my_list:
    if num <= 10:
        count += 1
        
print("Exo 6.12 - Le compte des nombres les plus petits ou égaux à 10 dans \
la liste est : %d" % count)   

# exo 6.13
# Multipliez chacun des nombres par 100 dans la liste 
# et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
print(f"Exo 6.13 - Avant la multiplication de chacun des nombres de la liste \
par 100 : {my_list}") 

for i, num in enumerate(my_list):
    my_list[i] *= 100
    
print(f"Exo 6.13 - Après la multiplication de chacun des nombres de la liste \
par 100 : {my_list}") 

# exo 6.14
# Créez une deuxième liste ne contenant que les nombres entiers 
# de la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14
my_list2 = []

for i, num in enumerate(my_list):
    if type(num) is int:
        my_list2.append(num)
        
print(f"Exo 6.14 - Les nombres entiers contenus dans la deuxième liste : \
{my_list2}")

# exo 6.15
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.15
print(f"Exo 6.15 - Avant la permutation des éléments de la liste: {my_list}")

n = len(my_list)

for i in range(n):
    for j in range(0, n-i-1, 2):
        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]     
        
print(f"Exo 6.15 - Après la permutation des éléments de la liste: {my_list}")

# exo 6.16
# Triez la liste en utilisant l'algorithme du tri bulle 
# puis affichez la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
# Première version non-optimisée :
# print(f"Exo 6.16 - Avant l'application de l'algorithme du tri bulle : \
# {my_list}")

# n = len(my_list)

# for i in range(n):
#     for j in range(0, n-i-1):
#         if my_list[j] > my_list[j+1]:
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]         
            
# print(f"Exo 6.16 - Après l'application de l'algorithme du tri bulle : \
# {my_list}")

# exo 6.16
# réponse 6.16
print(f"Exo 6.16 - Avant l'application de l'algorithme du tri bulle : {my_list}")

n = len(my_list)

while True:
    loop = False
    
    for i in range(0, n-1):
        if my_list[i] > my_list[i+1]:
            loop = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]  
            
    if not loop:   
        break    
            
print(f"Exo 6.16 - Après l'application de l'algorithme du tri bulle : {my_list}")

# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
# Attention : il faut faire `- 1` pour obtenir les index correspondant
size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)
    
# réponse 6.17
print(f"Exo 6.17 - Matrice : {matrix}\n")

# Repère visuel en mettant en forme la matrice :
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print()
    
print(f"\nExo 6.17 - Valeur qui se trouve à la colonne 4, ligne 3 de \
la Matrice : {matrix[2][3]}")

# exo 6.18
# Avec le même tableau en 2 dimension, 
# affichez toutes les valeurs plus petites ou égales à 50 
# ainsi que leur cordoonnées (ligne et colonne)

# réponse 6.18
# last_index = (len(matrix) - 1) 

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] <= 50:
            print(f"Exo 6.18 - Une valeur plus petite ou égale à 50 de \
la matrice avec ses coordonnées : {matrix[i][j]}, [{i}][{j}]")
            
            # while last_index == matrix[4][4]:
            #     break
