# Exchange Program
# Here is the last exercise in this lesson.

# You have completed this problem at least once.
# Coding Exercise: Exchange Program
# Write a program to swap the values of two variables. The grader will automatically define variables x and y for you, with numerical values. You must write code that exchanges their values: the value of x after your code runs must equal the value that y had before your code ran, and the value of y after your code runs must equal the value that x had before your code ran. Your program does not need to print any output.
# The most common solution is short, but can be hard to find. Click on each hint if you want to read it. 

# Exo fait sur le site :

# tmp = x
# x = y
# y = tmp

# Adapté sur VSCode:
import random

x = random.randint(0, 99)
print(f"Avant x = {x}")

y = random.randint(0, 99)
print(f"Avant y = {y}")
print("\n")
tmp = x
x = y
y = tmp
print(f"Après x = {x}")
print(f"Après y = {y}")