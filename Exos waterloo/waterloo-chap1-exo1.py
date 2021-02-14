# Coding Exercise: Heads, Shoulders, Knees and Toes

# Write a code fragment (a short part of a Python program) to count heads, shoulders, knees, and toes at a party. The grader will automatically define a variable people for you, counting the number of people at the party. Your code must define four variables, one called heads, one called shoulders, one called knees, and one called toes, equal to the number of heads, shoulders, knees, and toes in total at the party. Your program does not need to print any output. The grader will select a new random value for people each time your code runs.

# Correction :

# heads = 1 * people
# shoulders = 2 * people
# knees = 2 * people
# toes = 10 * people


# Adapté sur VSCode:
import random

people = random.randint(0, 99)

heads = 1 * people
shoulders = 2 * people
knees = 2 * people
toes = 10 * people

print(f"people = {people}")
print(f"number of people * number of heads = {heads} heads")
print(f"number of people * number of shoulders = {shoulders} shoulders")
print(f"number of people * number of knees = {knees} knees")
print(f"number of people * number of toes = {toes} toes")