# Au jeu de pile ou face, il y a seulement 
# deux issues possibles : pile ou face.
# Pour afficher toutes les issues possibles, 
# on doit utiliser une boucle.

# code 2.1
for i in range(0, 2):
    if i == 0:
        print("pile")
    else:
        print("face")

# Il est possible d'ajouter un compteur, 
# pour savoir combien d'issues existent.

# code 2.2
# le nombre d'issues dont on veut calculer la probabilité
counter = 0

for i in range(0, 2):
    counter += 1

    if i == 0:
        print("pile")
    else:
        print("face")

print(f"il y a {counter} issues en tout\n")

# Si on ne fait qu'un seul lancer, le compteur ne sert pas à grand chose
# car on sait d'avance qu'il n'y a que 2 issues.

# Mais si on joue à pile ou face en faisant plusieurs lancers,
# il y a plus que 2 issues.
# Avec 2 lancers, on obtient 4 issues possibles :
# - pile & pile
# - pile & face
# - face & pile
# - face & face

# Pour afficher tous les cas possibles, 
# on peux utiliser deux boucles imbriquées.

# Rappel :
# - 0 est équivalent à pile
# - 1 est équivalent à face

# code 2.3
# Premier lancer
for i in range(0, 2):
    # Deuxième lancer
    for j in range(0, 2):
        
        if i == 0:
            # Le premier lancer donne pile
            # Le paramètre end='' permet de ne pas passer à la ligne
            print("pile", end='')
        else:
            # Le premier lancer donne face
            # Le paramètre end='' permet de ne pas passer à la ligne
            print("face", end='')

        if j == 0:
            # Le deuxième lancer donne pile
            print(" & pile")
        else:
            # Le deuxième lancer donne face
            print(" & face")

# exo 2.1 : Reprenez le code 2.3 et ajoutez-y un compteur 
# pour calculer le nombre total d'issues. 
# Inspirez-vous de l'exemple 2.2.

# réponse 2.1
print("\nExo 2.1: ")  

# Premier lancer
for i in range(0, 2):
    counter = 0
    # Deuxième lancer
    for j in range(0, 2):
        counter +=1           
        
        if i == 0:
            # Le premier lancer donne pile
            print("pile", end='')
        else:
            # Le premier lancer donne face
            print("face", end='')
            
        if j == 0:
            # Le deuxième lancer donne pile
            print(" & pile")
        else:
            # Le deuxième lancer donne face
            print(" & face")

print(f"Il y a {counter} issues en tout")

######################################################

# exo 2.2 : Maintenant, rédigez le code qui indique toutes les issues
# possibles d'un lancer de dé ainsi que le nombre total d'issues. 
# Inspirez-vous de l'exemple 2.2.

# réponse 2.2
print("\nExo 2.2: ")    

counter = 0

# le nombre d'issues dont on veut calculer la probabilité
for i in range(0, 6):
    counter += 1
    
    if i == 0:
        # le premier lancer donne 1
        print(" & un")
    elif i == 1:
        # le premier lancer donne 2
        print(" & deux")
    elif i == 2:
        # le premier lancer donne 3
        print(" & trois")
    elif i == 3:
        # le premier lancer donne 4
        print(" & quatre")
    elif i == 4:
        # le premier lancer donne 5
        print(" & cinq")
    else:
        # le premier lancer donne 6
        print(" & six")
   
print(f"Le nombre total d'issues d'un lancer de dé : {counter}.")

######################################################

# exo 2.3 : Rédigez le code qui indique toutes les issues possibles de 
# deux lancers d'un seul dé. Inspirez-vous des exemples 2.2 et 2.3.

# réponse 2.3
print("\nExo 2.3: ")     

counter = 0

# Premier lancer
for i in range(0, 6):
    
    # Deuxième lancer
    for j in range(0, 6):
        counter += 1           
        
        if i == 0:
            # le premier lancer donne 1
            print(" & un", end='')
        elif i == 1:
            # le premier lancer donne 2
            print(" & deux", end='')
        elif i == 2:
            # le premier lancer donne 3
            print(" & trois", end='')
        elif i == 3:
            # le premier lancer donne 4
            print(" & quatre", end='')
        elif i == 4:
            # le premier lancer donne 5
            print(" & cinq", end='')
        else:
            # le premier lancer donne 6
            print(" & six", end='')
            
        if j == 0:
            # le deuxième lancer donne 1
            print(" & un")
        elif j == 1:
            # le deuxième lancer donne 2
            print(" & deux")
        elif j == 2:
            # le deuxième lancer donne 3
            print(" & trois")
        elif j == 3:
            # le deuxième lancer donne 4
            print(" & quatre")
        elif j == 4:
            # le deuxième lancer donne 5
            print(" & cinq")
        else:
            # le deuxième lancer donne 6
            print(" & six")
       
print(f"Le nombre d'issues possibles de deux lancers \
d'un seul dé : {counter} en tout.")
