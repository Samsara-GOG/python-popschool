# exercise-09-solution.py

import random

# exo 9.1
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé alphanumérique et un nombre entier
# - une clé alphanumérique et un nombre à virgule flottante
# - une clé alphanumérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.1
my_dict = {
    'boats': 5,
    'pi': 3.14,
    'singer': "Elvis Presley",
    'truth': True
}
print("Exo 9.1:")
print(my_dict)

# exo 9.2
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé booléenne et un nombre entier
# - une clé booléenne et un nombre à virgule flottante
# - une clé numérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.2
my_dict = { 
    False: 3,
    True: 6.5,
    10: 'fix',
    'Connected': False      
}

print("\nExo 9.2:")
print(my_dict)

# exo 9.3
# Ajoutez au dictionnaire un élément qui associe la clé alphanumérique `ipsum` à la valeur `2.71`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.3
print("\nExo 9.3:")

my_dict['ipsum'] = 2.71
print(my_dict)

# exo 9.4
# Supprimez du dictionnaire la clé `foo`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.4
print("\nExo 9.4:")

del my_dict['foo']
print(my_dict)

# exo 9.5
# Remplacez la valeur du dictionnaire associée à la clé `foo` par `123`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.5
print("\nExo 9.5:")

my_dict['foo'] = 123
print(my_dict)

# exo 9.6
# En utilisant une boucle `for`, affichez les clés (et pas les valeurs) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.6
print("\nExo 9.6")

for key in my_dict.keys():
    print(f"key: {key}")

print("\n")

for key in my_dict:
    print(f"key: {key}")

# exo 9.7
# En utilisant une boucle `for`, affichez les valeurs (et pas les clés) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.7
print("\nExo 9.7")

for value in my_dict.values():
    print(f"value: {value}")
print("\n")
for value in my_dict:
    print(f"value: {my_dict[value]}")

# exo 9.8
# En utilisant une boucle `for` et sans utiliser la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.8
print("\nExo 9.8:")
    
for key in my_dict:
    print(f"key: {key}, value: {my_dict[key]}")

# exo 9.9
# En utilisant une boucle `for` et la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.9
print("\nExo 9.9:")
for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")
