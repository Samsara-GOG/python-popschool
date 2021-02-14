# exercise-10.py

# exo 10.1
# Créer une fonction nommée `my_sum()` qui :
# - prend deux paramètres
# - additionne ces deux paramètres
# - renvoit le résultat
# Appelez la fonction et affichez le résultat

# réponse 10.1
print("Exo 10.1")

def my_sum(a, b):
    """Renvoit l'addition de a et b"""
    return a + b

num1, num2 = 2, 8
sum = my_sum(num1, num2)

print(f"{num1} + {num2} = {sum}")

#######################################################

# exo 10.2
# Créer une fonction nommée `my_diff()` qui :
# - prend deux paramètres de type `int`
# - soustrait `b` de `a`
# - renvoit le résultat de type `int`
# Notez bien le type hinting dans la déclaration de la fonction
# Appelez la fonction et affichez le résultat

# réponse 10.2
print("\nExo 10.2")

def my_diff(a: int, b: int) -> int:
    """Renvoit la soustraction de b à a"""
    return a - b

num2, num3 = 20, 10
diff = my_diff(num2, num3)
print(f"{num2} - {num3} = {diff}")
#######################################################

# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoit `oui` si le booléen est égal à True
# - renvoit `non` si le booléen est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3
print("\nExo 10.3:")

def oui_non(working: bool):
    """Renvoit oui ou non en fonction du paramètre booléen"""
    if working: 
        return "oui"
    else:
        return "non"

marketing = True 
market = oui_non(marketing)
print(f"Marketing is ok = {market}")

traders = False
trad = oui_non(traders)
print(f"Traders are ok = {trad}")

#######################################################

# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit True si `a` est plus grand que `b`
# Appelez la fonction et affichez le résultat

# réponse 10.4
print("\nExo 10.4:")

def is_greater(a: float, b: float):
    """Renvoit True si a est plus grand que b, sinon False"""
    if a > b:
        return True
    else:
        return False

num4, num5 = 10.55, 3.66 
great1 = is_greater(num4, num5)
print(f"{num4} > {num5} ? : {great1}")

num4, num5 = 3.66, 10.55
great2 = is_greater(num4, num5)
print(f"{num4} > {num5} ? : {great2}")

#######################################################

# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit 1 si `a` est plus grand que `b`
# - renvoit -1 si `a` est plus petit que `b`
# - renvoit 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
print("\nExp 10.5:")

def compare(a: float, b: float):
    """Renvoit une valeur en fonction du résultat de la comparaison entre a et b"""
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
    
# Test a < b
num6, num7 = 25, 50
compare1 = compare(num6, num7)
print(f"Test {num6}(a) < {num7}(b) : {compare1}")

# Test a > b
num6, num7 = 50, 25 
compare2 = compare(num6, num7)
print(f"Test {num6}(a) > {num7}(b) : {compare2}")

# Test a == b
num6, num7 = 50, 50 
compare3 = compare(num6, num7)
print(f"Test {num6}(a) == {num7}(b) : {compare3}")

#######################################################

# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire le contraire :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - metersToMiles() permettant de convertir des mètres en miles
# - milesToMeters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 100 mètres en miles
# - 100 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6
print("\nExo 10.6:")

def metersToMiles(meters):
    """Renvoit la conversion d'une valeur en mètres en miles"""
    return meters / 1609.344

def milesToMeters(miles):
    """Renvoit la conversion d'une valeur en miles en mètres"""
    return miles * 1609.344

distance_meters = 100
meters_to_miles1 = metersToMiles(distance_meters)
print(f"{distance_meters} mètres = {meters_to_miles1:.5f} miles")

distance_miles = 100
miles_to_meters2 = milesToMeters(distance_miles)
print(f"{distance_miles} miles = {miles_to_meters2} mètres ou {miles_to_meters2 / 1000:.3f} km")
#######################################################

# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` ets égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` ets égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` ets égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` ets égal à `4`
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe

# réponse 10.7
print("\nExo 10.7:")

def compute_tax(price: float, tax_type: int):
    """Renvoit le résultat d'une taxe calculée en fonction du type de TVA et d'un montant"""
    # TVA à 2,1 %
    if tax_type == 1:
        price += price * .021
    # TVA à 5,5 %
    elif tax_type == 2:
        price += price * .055
    # TVA à 10 %
    elif tax_type == 3:
        price += price * .10
    # TVA à 20 %
    elif tax_type == 4:
        price += price * .20
        
    return price

revenue = 100
compute_tax1 = compute_tax(100, 1)
print(f"Taxe de 2,1 % sur {revenue}€: {compute_tax1}€")

compute_tax2 = compute_tax(100, 2)
print(f"Taxe de 5,5 % sur {revenue}€: {compute_tax2}€")

compute_tax3 = compute_tax(100, 3)
print(f"Taxe de 10 % sur {revenue}€: {compute_tax3}€")

compute_tax4 = compute_tax(100, 4)
print(f"Taxe de 20 % sur {revenue}€: {compute_tax4}€")