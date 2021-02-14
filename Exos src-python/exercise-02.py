import time_message as time_m

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur null `None` à une variable
# Affichez ces variables

# réponse 2.1
# - le nombre 42 à une variable
number1 = 42
print(f"number1 = {number1}")

# - le nombre d'or 1,61 à une variable
golden_ratio = 1.61
print(f"golden_ratio = {golden_ratio}")

# - votre nom et prénom à une variable
full_name = "Jérôme Demuynck"
print(f"full_name = {full_name}")

# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# module time_message crée pour l'occasion grâce à l'enseignement de Python sur codecademy


time_m.time_message()

# - la valeur null `None` à une variable
null_value = None

# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez le valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi en un integer
# - float 1,62 en un float arrondi en un float à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2
a, b = 2, 1.62
# - integer 2 en un float
c = float(a)
print(f"c = {c}")
# - float 1,62 en un integer
d = int(b)
print(f"d = {d}")
# - float 1,62 en un float arrondi en un integer
e = round(b)
print(f"e = {e}")
# - float 1,62 en un float arrondi en un float à un chiffre après la virgule
f = round(b, 1)
print(f"f = {f}")