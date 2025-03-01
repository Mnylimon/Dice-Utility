# Dev0

# Dice Utility Program for board games and other games

import random

# imports a list that has the alphabet and special characters for use later
import list_of_characters

# List for different dice
dice_4 = ['1', '2', '3', '4']
dice_6 = ['1', '2', '3', '4', '5', '6']
dice_8 = ['1', '2', '3', '4', '5', '6', '7', '8']
dice_10 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
dice_12 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
dice_20 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20']

# empty values for later
dice_roll = []
total_value = 0
roll_count = 0
# condition that ends or keeps program running
end_program = False

# functions


def typo():
    # Function that determines if user inoutted a typo
    # global variable just calls the global version
    global end_program
    typo = input('Was that a typo?\nType "y" or "n"\n>> ').lower()
    if typo == "y":
        print("Alright.\n")
    elif typo == "n":
        print("Come again next time.")
        end_program = True
    else:
        print("I guess that's a no. Come again.")
        end_program = True


def roll_dice():
    # function that takes user input and rolls a dice
    dice_type = input("\nWhich dice do you want to roll?"
                      "\nType one of the options: 4, 6, 8, 10, 12, 20"
                      "\n>> ")

    if dice_type == "4":
        roll_value = random.choice(dice_4)
        dice_roll.append(roll_value)
        print(f"\nWith a four sided dice, You rolled a {roll_value}.\n")
    elif dice_type == "6":
        roll_value = random.choice(dice_6)
        dice_roll.append(roll_value)
        print(f"\nWith a regular dice, You rolled a {roll_value}.\n")
    elif dice_type == "8":
        roll_value = random.choice(dice_8)
        dice_roll.append(roll_value)
        print(f"\nWith an eight sided dice, you rolled a {roll_value}\n")
    elif dice_type == "10":
        roll_value = random.choice(dice_10)
        dice_roll.append(roll_value)
        print(f"\nWith a ten sided dice, you rolled a {roll_value}.\n")
    elif dice_type == "12":
        roll_value = random.choice(dice_12)
        dice_roll.append(roll_value)
        print(f"\nWith a twelve sided dice, you rolled a {roll_value}.\n")
    elif dice_type == "20":
        roll_value = random.choice(dice_20)
        dice_roll.append(roll_value)
        print(f"\nWith a twenty sided dice, you rolled a {roll_value}.\n")
    else:
        typo()


def add_n_subtract_roll():
    # Function that prompts the user if they want to add
    # or subtract a certain value from their roll.
    prompt1 = input('Do you want to add or subtract to your dice'
                    ' roll?\nType "y" or "n"\n>> ').lower()
    if prompt1 == "y":
        prompt2 = input('Add or Subtract?\nType "a" or "s"\n>> '
                        ).lower()
        while prompt2 == "a":
            add_roll = int(input("Type the number you want to add to"
                                 " your roll.\n>> "))
            if add_roll in list_of_characters.chars_list:
                typo()
            else:
                dice_new_value = int(dice_value) + add_roll
                print(f"Your new roll is {str(dice_new_value)}.")
                prompt2 = ""
        while prompt2 == "s":
            subtract_roll = int(input("Type the number you want to"
                                      "subtract from your roll.\n>> "))
            if subtract_roll in list_of_characters.chars_list:
                typo()
            else:
                dice_new_value = int(dice_value) - subtract_roll
                print(f"Your new roll is {str(dice_new_value)}.")
                prompt2 = ""
    elif prompt1 == "n":
        print("Alright\n")
    else:
        typo()


def total_of_rolls():
    # function that gets the sum of the user's rolls
    global total_value
    prompt3 = input("Do you want the sum of your dice rolls?\n"
                    'Type "y" or "n"\n>> ').lower()
    if prompt3 == "y":
        for number in dice_roll:
            total_value += int(number)
        print(f"The sum of all your dice rolls is {total_value}.")
    elif prompt3 == "n":
        print("Alright.")
    else:
        typo()


# Welcome message to users
print("Welcome to the Dice Utility.")
print("Useful for rolling a dice, adding up dice rolls,"
      " and subtracting from dice rolls.")

# While loop for program
while not end_program:
    length_of_dice_roll = int(len(dice_roll))

    start = input('\nDo you want to roll a dice?\nType "y" or "n"\n>> '
                  ).lower()

    if start == "y":
        roll_dice()
        roll_count += 1
        for roll in dice_roll:
            dice_value = roll
        if length_of_dice_roll >= 0:
            add_n_subtract_roll()
        if length_of_dice_roll > 0:
            total_of_rolls()
        print(f"Your dice rolls {dice_roll}")
        print(f"The amount of times you have rolled a dice: {roll_count}")
    elif start == "n":
        print("Come again next time.")
        end_program = True
    else:
        typo()
