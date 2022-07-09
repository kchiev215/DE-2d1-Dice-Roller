# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import math
import random

class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        dice1 = random.randint(1, self.num_sides)
        sum = dice1
        print(f"Dice 1: {dice1}")
        print(f"Total: {sum}")

    def rolltwice(self):
        dice1 = random.randint(1, self.num_sides)
        print(f"Dice 1: {dice1}")
        dice2 = random.randint(1, self.num_sides)
        print(f"Dice 2: {dice2}")
        sum = dice1 + dice2
        print(f"Total: {sum}")
    def rollthrice(self):
        dice1 = random.randint(1, self.num_sides)
        print(f"Dice 1: {dice1}")
        dice2 = random.randint(1, self.num_sides)
        print(f"Dice 2: {dice2}")
        dice3 = random.randint(1, self.num_sides)
        print(f"Dice 3: {dice3}")
        sum = dice1 + dice2 + dice3
        print(f"Total: {sum}")










die = Dice()

"""Dice game"""
diceOn = True
while diceOn == True:
    print("How many time would you like to roll a dice? (1-3) press 0 to quit")
    diceToss = int(input(">> "))
    if diceToss == 1:
        die.roll()
    elif diceToss == 2:
        die.rolltwice()
    elif diceToss == 3:
        die.rollthrice()
    elif diceToss == 0:
        diceOn = False
    else:
        print("not enough dice")
    print("would you like to roll again? y or n")
    response = input(">> ")
    response.lower()
    if response == 'y':
        continue
    elif response == 'n':
        break
    else:
        print("That's not a valid response")
print("Thanks for playing")




