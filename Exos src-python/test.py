import random

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
last_index = (len(matrix) - 1) 

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] <= 50:
            print(f"Exo 6.18 - Une valeur plus petite ou égale à 50 de \
la matrice avec ses coordonnées : {matrix[i][j]}, [{i}][{j}]")
            
            while last_index == matrix[4][4]:
                break