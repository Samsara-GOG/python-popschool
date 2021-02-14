# exercise-14.py
import random

# Il existe un type de données particulier en Python : le tuple.

# code 4.1
my_tuple = ('foo', 123)

# Les tuples ressemblent aux listes car on peut y lire des données à la façon d'une liste.

# code 4.2
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])

# Mais à la différence des listes, une fois que l'on a créé un tuple, on ne peut plus le changer.

# code 4.3
# Si vous activez le code suivante, vous verrez l'erreur "# TypeError: 'tuple' object does not support item assignment"
# my_tuple[0] = 'lorem'

# Cela ne vous empêche pas de changer complètement le contenu de la variable.
# Mais cela ne change rien au fait qu'on ne pas changer le tuple.

# code 4.4
my_tuple = None

# Malgré cette limitation, les tuples sont pratiques pour créer des objets composites à partir de données de base ("int", "float", "bool", "str")

# Par exemple, on peut s'en servir pour modéliser un jeu de carte à jouer.

# code 4.5
cards = []

for i in range(0, 4):
    # Dans un jeu, il y a les cartes de 1 à 10 et les têtes, dans 4 couleurs.
    # Pour les têtes : valet = 11, reine = 12 et roi = 13
    # Pour les couleurs : cœur = 0, carreau = 1, pique = 2, trèfle = 3
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'

        cards.append((symbol, color, j))

print(cards)

# Voici comment mélanger le jeu de carte.

# code 4.6
random.shuffle(cards)

# Voici comment tirer au hasard une carte du jeu.

# code 4.7
# sélection d'une carte au hasard
card = random.choice(cards)
print(card)

# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)

# Voici comment remettre une carte dans le jeu.

# code 4.8
cards.append(card)

# Voici comment tirer 1 carte du jeu, la mettre dans le paquet d'Alice et au final les remettre dans le jeu.

# code 4.9
# le paquet de carte d'Alice (au début, il est vide)
alice = []

# sélection d'une carte au hasard
card = random.choice(cards)

# suppression de la carte de la liste (la carte est dans les mains d'Alice)
cards.remove(card)

# ajout de la carte dans le paquet d'Alice
alice.append(card)

# remise des cartes d'Alice dans le jeu
cards.extend(alice)

# suppression de toutes les carte d'Alices de son paquet
alice.clear()

#############################################################################

# exo 4.1 : Rédigez le code qui affiche la valeur et la couleur de 
# chaque carte du jeu.

# réponse 4.1
print("Exo 4.1: ")

import random

cards = []

for i in range(0, 4):
    # Dans un jeu, il y a les cartes de 1 à 10 et les têtes, dans 4 couleurs.
    # Pour les têtes : valet = 11, reine = 12 et roi = 13
    # Pour les couleurs : cœur = 0, carreau = 1, pique = 2, trèfle = 3
    for j in range(1, 14):
        if i == 0:
            color = 'rouge'
            symbol = 'cœur'
        elif i == 1:
            color = 'rouge'
            symbol = 'carreau'
        elif i == 2:
            color = 'noir'
            symbol = 'pique'
        elif i == 3:
            color = 'noir'
            symbol = 'trèfle'
            
        if j == 1:
            value = "as"
            print(f" & {value})")
        elif j == 2:
            value = "deux"
            print(f" & {value})")
        elif j == 3:
            value = "trois"
            print(f" & {value})")
        elif j == 4:
            value = "quatre"
            print(f" & {value})")
        elif j == 5:
            value = "cinq"
            print(f" & {value})")
        elif j == 6:
            value = "six"
            print(f" & {value})")
        elif j == 7:
            value = "sept"
            print(f" & {value})")
        elif j == 8:
            value = "huit"
            print(f" & {value})")
        elif j == 9:
            value = "neuf"
            print(f" & {value})")
        elif j == 10:
            value = "dix"
            print(f" & {value})")
        elif j == 11:
            value = "valet"
            print(f" & {value})")
        elif j == 12:
            value = "reine"
            print(f" & {value})")
        else:
            value = "roi"
            print(f" & {value})")

        cards.append((symbol, color, value))

cards_length = len(cards)
print(f"La valeur et la couleur des {cards_length} cartes du jeu : \
{cards}")

        
#############################################################################

# exo 4.2 : Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Puis Alice tire 1 carte au hasard (sans la remettre dans le jeu).
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le nombre de cartes qui restent dans le jeu et enfin 
# remettez toutes les cartes dans le jeu.

# réponse 4.2
print("\nExo 4.2")
# le paquet de carte vide d'Alice
alice = []

# sélection d'une première carte au hasard
card = random.choice(cards)
print(f"La première carte tirée au hasard par Alice est : \
{card}")

# suppression de la première carte de la liste 
# (la carte est dans les mains d'Alice)
cards.remove(card)

# ajout de la première carte dans le paquet d'Alice
alice.append(card)
print(f"Carte(s) en possession d'Alice : {alice}")

# sélection d'une deuxième carte au hasard
card = random.choice(cards)
print(f"\nLa deuxième carte tirée au hasard par Alice est : \
{card}")

# suppression de la deuxième carte de la liste
cards.remove(card)

# ajout de la deuxième carte dans le paquet d'Alice
alice.append(card)
print(f"Carte(s) en possession d'Alice : {alice}")

# affichage du nombre de cartes restantes dans le jeu
cards_length = len(cards)

print(f"\nNombre de cartes restantes dans le jeu avant \
la remise des cartes prises par Alice : {cards_length}")

# remise de toutes les cartes d'Alice dans le jeu
cards.extend(alice)

# suppression de toutes les carte d'Alices de son paquet
alice.clear()
print("Alice remet ses cartes dans la pile")
cards_length = len(cards)
# jeu de 52 cartes
MAX_CARDS = 52

if cards_length == MAX_CARDS:
    print(f"Le jeu contient {cards_length} cartes, donc \
toutes les cartes ont été rendues dans la pile")
    
#############################################################################

# exo 4.3 : Bob tire 3 cartes au hasard (sans les remettre dans le jeu) 
# et les met dans son paquet.
# Rédigez le code qui effectue ces opérations.
# Ensuite affichez le paquet de Bob, le nombre de cartes qui restent 
# dans le jeu et remettez toutes les cartes dans le jeu.

# réponse 4.3
print("\nExo 4.3: ")

# le paquet de carte vide de Bob
bob = []

# sélection d'une première carte au hasard
card = random.choice(cards)
print(f"La première carte tirée au hasard par Bob est : {card}")

# suppression de la première carte de la liste 
# (la carte est dans les mains de Bob)
cards.remove(card)

# ajout de la première carte dans le paquet de Bob
bob.append(card)
print(f"Carte(s) en possession de Bob : {bob}")

# sélection d'une deuxième carte au hasard
card = random.choice(cards)
print(f"\nLa deuxième carte tirée au hasard par Bob est : {card}")

# suppression de la deuxième carte de la liste
cards.remove(card)

# ajout de la deuxième carte dans le paquet de Bob
bob.append(card)
print(f"Carte(s) en possession de Bob : {bob}")

# sélection d'une troisième carte au hasard
card = random.choice(cards)
print(f"\nLa troisième carte tirée au hasard par Bob est : {card}")

# suppression de la troisième carte de la liste
cards.remove(card)

# ajout de la troisième carte dans le paquet de Bob
bob.append(card)
print(f"Carte(s) en possession de Bob : {bob}")

# affichage du nombre de cartes restantes dans le jeu
cards_length = len(cards)

print(f"\nNombre de cartes restantes dans le jeu avant \
la remise des cartes prises par Bob : {cards_length}")

# remise de toutes les cartes de Bob dans le jeu
cards.extend(bob)

# suppression de toutes les carte de Bob de son paquet
bob.clear()
print("Bob a remis toutes ses cartes dans la pile")
cards_length = len(cards)

# Rappel MAX_CARDS = 52
if cards_length == MAX_CARDS:
    print(f"Le jeu contient {cards_length} cartes, donc \
toutes les cartes ont été remises dans la pile")

#############################################################################

# exo 4.4 : Alice et Bob parient en jouant aux cartes.
# Voici comment se déroule le jeu :
# 1. Bob mélange les cartes, puis Alice tire trois cartes.
# 2. Elle parie que si un 3 (de n'importe quelle couleur) ou deux cœurs 
# figurent parmi les cartes tirées, elle gagne.
# 3. Alice remets ses cartes dans le jeu, le mélange à nouveau, 
# puis Bob tire 3 cartes.
# 4. Il parie que si un 7 (de n'importe quelle couleur) ou deux piques 
# figurent parmi les cartes tirées, il gagne.
# 5. Bob remet ses cartes dans le jeu, ce qui termine une manche.
# Ils décident de faire trois manches.
# Rédigez le code qui modélise ce jeu et indiquez qui sera 
# le gagnant des trois manches.

# réponse 4.4
##################################################################################""
################################################################################
print("\nExo 4.4: ")

# 1. Bob mélange les cartes
random.shuffle(cards)

def tirer_cartes(game, player, use):
    i = 0
    while i < use:
        card = random.choice(cards)
        print(f"La carte tirée au hasard par {player} est : {card}")
        # suppression de la carte de la liste 
        cards.remove(card)
        # ajout de la carte dans le paquet
        game.append(card)
        i += 1
    
def afficher_cartes(game, player):
    print(f"Carte(s) en possession de {player}: {game}\n")
    
def verif_max_pile():
    MAX_CARDS = 52
    cards_length = len(cards)
    if cards_length == MAX_CARDS:
        print(f"Le jeu contient {cards_length} cartes, donc \
toutes les cartes ont été remises dans la pile")

def rendre_cartes(game, player):
    cards.extend(game)
    game.clear()
    print(f"{player} remet ses cartes dans la pile")
    verif_max_pile()

def melanger_cartes(player):
    random.shuffle(cards)
    print(f"\n***{player} mélange les cartes***\n")
    

# initialisation du compteur de victoire à l'issue d'une manche
score_alice = 0
score_bob = 0
# boucle des 3 manches pour le programme principal de la partie
k = 1
while k < 4:
    print(f"\n\"Manche {(k)}\"\n")
    
    print("***********  Alice parie que si un 3 ou deux cœurs figurent \
parmi les cartes tirées, elle gagne la manche.  ***********\n")
    
    #1 Alice tire trois cartes.
    tirer_cartes(alice, "Alice", 3)
    afficher_cartes(alice, "Alice")

    # initialisation du compteur de coeurs
    count = 0
    # initialisation du compteur de victoire pour les paris
    win_alice = 0
    
    for i in range(len(alice)):
        for j in range(len(alice[i])):
            # 2.Alice gagne si 3 (de n'importe quelle couleur)
            if alice[i][j] == "trois":
                print("Alice est en train de gagner car elle a un 3 dans son jeu!\n")
                win_alice += 1
                break
            elif alice[i][j] == "cœur":
                count += 1
                continue
            # 2.Alice gagne si 2 cœurs          
            elif count == 2:
                print(f"Alice est en train de gagner car elle a {count} cœurs dans son jeu!\n")
                win_alice += 1
                break

    print("win_alice = ", win_alice)           
    # 3. Alice remets ses cartes dans le jeu, le mélange à nouveau.
    rendre_cartes(alice, "Alice")
    melanger_cartes("Alice")

    print("\n***********  Bob parie que si un 7 ou deux piques figurent \
parmi les cartes tirées, il gagne la manche  ***********\n")

    # Bob tire 3 cartes
    tirer_cartes(bob, "Bob", 3)
    afficher_cartes(bob, "Bob")

    # initialisation du compteur de piques
    count = 0
    # initialisation du compteur de victoire pour les paris
    win_bob = 0
    
    for i in range(len(bob)):
        for j in range(len(bob[i])):
            # 4. Bob gagne si 7 (de n'importe quelle couleur)
            if bob[i][j] == "sept":
                print("Bob est en train de gagner car il a un 7 dans son jeu!\n")
                win_bob += 1
                print(win_bob) 
                
            if bob[i][j] == "pique":
                count += 1
            # 4. Bob gagne si 2 piques          
            elif count == 2:
                print(f"Bob est en train de gagner car il a {count} piques dans son jeu!\n")
                win_bob += 1
                print(win_bob) 
                
    print("win_bob = ", win_bob)           
    # 5. Bob remet ses cartes dans le jeu, ce qui termine une manche.
    rendre_cartes(bob, "Bob")
    melanger_cartes("Bob")

    if win_alice < win_bob :       
        print("Bob remporte cette manche !\n")
        score_bob += 1
    elif win_alice > win_bob :
        print("Alice remporte cette manche !\n")
        score_alice += 1
    else:
        print("Alice et Bob sont à égalité pour cette manche!\n")
        
    print("score_alice = ", score_alice)
    print("score_bob = ", score_bob)
    
    if k == 3 and score_alice > score_bob :
        print(f"Alice est la gagnante des {k} manches !")
        break
    elif k == 3 and score_alice < score_bob :
        print(f"Bob est le gagnant des {k} manches !")
        break
    elif k == 3 and score_alice == score_bob :
        print(f"Alice et Bob sont à égalité parfaite au bout des {k} manches! \
Une autre partie pourrait les départager..")

    # Rédigez le code qui modélise ce jeu et indiquez qui sera le gagnant des trois manches.

    k += 1
#########"
# question sur break, continue
print("Apres score_alice = ", score_alice)
print("Apres score_bob = ", score_bob)
