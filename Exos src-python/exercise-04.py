# exercise-06-solution.py

# exo 4.1
# Ajoutez de la documentation à la fonction suivante

# réponse 4.1
def addition(a, b):
    """Renvoie la somme de deux valeurs."""
    return a + b

# exo 4.2
# Trouvez la position de la chaîne de caractères `ipsum`
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

# réponse 4.2
print("\nExo 4.2")
print(f"Position de la chaîne de caractères 'ipsum' : {my_text.find('ipsum')}")

# exo 4.3
# Affectez les caractères de l'index 12 à 20 inclus, de la variable `my_text`, à une autre variable
# Affichez le résultat ; le résultat devrait être `dolor sit`
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

# réponse 4.3
my_text2 = my_text[12:21]
print("\nExo 4.3")
print(f"Résultat de my_text[12:21] : {my_text2}")

# code 4.1
# La méthode `str.split()` permet de scinder une chaîne de caractères en tableau de chaînes de caractères en utilisant un séparateur
# Example : ici on scinde une chaîne de caractères en utilisant l'espace ' ' comme séparateur
# print("foo bar baz".split(' '))

# exo 4.3
# Scindez la variable `my_text` en utilisant l'espace comme séparateur et affectez le résultat à une autre variable.
# Affichez le mot qui se trouve à l'index 5 du tableau ; le résultat devrait être `consectetur`
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

# réponse 4.3
print("\nExo 4.3?")
my_text3 = my_text.split(' ')
print(f"my_text3[5] = {my_text3[5]}")

# code 4.2
# En python, un saut de ligne dans une chaîne de caractères peut être obtenu en utilisant un caractère échappé
my_text1 = "texte\nmulti\nligne"
# Ou en utilisant une chaîne de caractères multiligne
my_text2 = """texte
multi
ligne"""
# Mais dans la mémoire de python, les deux chaînes de caractères sont encodées de la même façon
# print('\n' in my_text1)
# print('\n' in my_text2)

# code 4.3
# La méthode `str.find()` permet de retrouver la position d'une chaîne caractères dans une autre chaîne de caractères
# print("foo bar baz".find('bar'))
# Quand `str.find()` ne trouve pas de résultat, la méthode renvoit `-1`
# Mais on peut aussi borner la recherche.
# Exemple : ici on démarre la recherche à partir du caractère de la position 5
# print("foo bar baz".find('bar', 5))

# exo 4.4
# Trouvez au moins une façon (et deux au plus) de compter le nombre de lignes de la chaîne de caractère suivante :
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(my_text)

# réponse 4.4
print("\nExo 4.4")
# Première méthode simple
count = 0

for i in my_text:
    if i == ".":
        count += 1
        
print("Première méthode :")
print(f"Il y a {count} lignes, car {count} \".\" sont présents.\n")

# Deuxième méthode simple
# avec "\n" la dernière ligne dans la chaîne de caractères 
# n'est pas comptée comme saut de ligne, 
# donc on incrémente count de 1  par avance
count = 1

for i in my_text:
    if i == "\n":
        count += 1
    
print("Seconde méthode :")
print(f"Avec saut de ligne : il y a {count} lignes.")

# Troisième méthode plus compliquée et inutile(?)
count = 1
my_text6 = my_text.split(' ')

for i in range(len(my_text6)):
    for j in range(len(my_text6[i])):
        if my_text6[i][j] == "\n":
            count += 1

print("\nTroisième méthode : ")
print(f"Avec saut de ligne : il y a {count} lignes.")

# Quatrième méthode avec le repérage de la majuscule
count = 0

for i in my_text:
    if i.isupper() :
        count += 1

print("\nQuatrième méthode : ")
print(f"Avec la majuscule : il y a {count} lignes.")