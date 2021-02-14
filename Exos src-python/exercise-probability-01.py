# Chargement du module random (pour générer des nombres aléatoires).
import random

# L'appel à la fonction random.randint(0, 1) renvoit 
# un nombre entier aléatoire compris entre 0 et 1 inclus.
number = random.randint(0, 1)

# Pour savoir si la variable "number" vaut 1, je peux utiliser 
# un bloc conditionnel.

# code 1.1
if number == 0:
    print("le nombre vaut 0")

# Pour savoir quel nombre la variable "number" vaut, je peux 
# utiliser une boucle.

# code 1.2
for i in range(0, 2):
    if number == i:
        # affichage avec interpolation de la variable au moyen 
        # d'une "f-string"
        print(f"le nombre vaut {number}")

# exo 1.1 : Alice et Bob veulent jouer à pile ou face.
# - si la variable "head_or_tail" vaut 0, cela équivaut à pile
# - si elle vaut 1, cela équivaut à face
# Alice parie pile et Bob parie face.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

# réponse 1.1
head_or_tail = random.randint(0, 1)
pile, face = 0, 1

print("Exo 1.1: ")

if head_or_tail == pile:
    # Alice parie sur pile
    print("Alice gagne, car c'est tombé sur Pile!")
else:
    # Et Bob donc sur Face
    print("Bob gagne, car c'est tombé sur Face!")


# exo 1.2 : Alice et Bob veulent jouer aux dés.
# Alice parie qu'elle va faire au moins 4. Bob parie qu'il va faire 3 au plus.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

# réponse 1.2
head_or_tail = random.randint(1, 6)

print("Exo 1.2: ")

if head_or_tail >= 4:
    print(f"Alice gagne car elle a fait {head_or_tail}")
elif head_or_tail >= 3:
    print(f"Bob gagne car il a fait {head_or_tail}")
else:
    print(f"Personne ne gagne car la pièce est tombée sur \
{head_or_tail}!")

# exo 1.3 : Alice et Bob jouent à pierre papier ciseaux.
# - 1 équivaut à pierre
# - 2 équivaut à papier
# - 3 équivaut à ciseaux
# Rédigez le code qui indique qui gagne.
# réponse 1.3

# rock_scissor_paper = random.randint(1, 3)
alice = random.randint(1, 3)
bob = random.randint(1, 3)
rock = 1
paper = 2
scissor = 3

print("Exo 1.3: ")

# longueur max des lignes inférieurs à 79 caractères, 
# commentaires 72 caractères au max
# pour respecter les recommandations du PEP8
if (alice == rock and bob == rock):
    print(f"Alice et Bob sont à égalité, pierre({rock}) contre \
pierre ({rock})!")
    
elif (alice == paper and bob == paper):
    print(f"Alice et Bob sont à égalité, papier({paper}) contre \
papier({paper})!")
    
elif (alice == scissor and bob == scissor):
    print(f"Alice et Bob sont à égalité, ciseau({scissor}) contre \
ciseau({scissor})!")
    
elif alice == rock and bob == paper:
    print(f"Bob gagne le combat car le papier({paper}) s'enroule \
autour de la pierre({rock})!")
    
elif alice == paper and bob == rock:
    print(f"Alice gagne le combat car le papier({paper}) s'enroule \
autour de la pierre({rock})!")
    
elif alice == rock and bob == scissor:
    print(f"Alice gagne le combat car la pierre({rock}) casse \
le ciseau({scissor})!")
    
elif alice == scissor and bob == rock:
    print(f"Bob gagne le combat car la pierre({rock}) casse \
le ciseau({scissor})!")
    
elif alice == scissor and bob == paper:
    print(f"Alice gagne le combat car le ciseau({scissor}) \
découpe le papier({paper})!")
    
elif alice == paper and bob == scissor:
    print(f"Bob gagne le combat car le ciseau({scissor}) \
découpe le papier({paper})!")