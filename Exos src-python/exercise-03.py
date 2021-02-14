# exo 3.1
# Calculez la moyenne des nombres suivants : 1, 1, 2, 3, 5, 8, 13.
# Affectez le résultat à une variable et affichez le résultat.

# réponse 3.1
average = (1 + 1 + 2 + 3 + 5 + 8 + 13) / 7
avg_rounded = round(average, 2)
print(f"La moyenne non-arrondie est : {average}")
print(f"La moyenne arrondie à 2 chiffres après la virgule est : {avg_rounded}")

# exo 3.2
# On est en vacance et on veut suivre ses dépenses quotidiennes.
# Stockez le montant de chacune des dépenses quotidiennes dans une variable différente :
# - day1 : 26,82
# - day2 : 42,00
# - day3 : 31,41
# - day4 : 63,7
# - day5 : 32
# Stockez le nombre de jours dans une variable.
# Calculez le montant total des dépenses.
# Calculez la moyenne des dépenses quotidiennes en utilisant la variable contenant le nombre de jours et le total.
# Affichez le nombre jours, le montant total et la moyenne des dépenses.

# réponse 3.2
day1 = 26.82
day2 = 42.00
day3 = 31.41
day4 = 63.7
day5 = 32

days = 5

total_spending = day1 + day2 + day3 + day4 + day5
average_daily_spending = total_spending / days

print(f"le nombre de jours est : {days}")
print(f"Le montant total des dépenses est : {total_spending}")
print(f"la moyenne des dépenses quotidiennes est : {round(average_daily_spending, 2)}")

# exo 3.3
# La formule suivante permet de convertir des mètres en miles :
# miles = meters / 1609.344
# Je dois marcher 2371 m pour aller jusqu'à la plus proche boulangerie.
# Combien cela fait-il en miles ?
# Affichez un résultat arrondi

# réponse 3.3
meters = 2371
miles = meters / 1609.344
print(f"2371 m = {round(miles, 3)} miles")
