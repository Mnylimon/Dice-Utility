# # # Dev 1

# # Imports
import random
from os import system
from list_of_characters import chars_list, menu_list

# #

# # Variables

# d4 stands for dice with 4 sides
# as such every dice is named d+number to mean dice with number of sides
list_of_dice = {
    0: {"4 sided dice": {1: '1', 2: '2', 3: '3', 4: '4'}
        },
    1: {"regular dice": {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6'}
        },
    2: {"8 sided dice": {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                         7: '7', 8: '8'}
        },
    3: {"12 sided dice": {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                          7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12'}
        },
    4: {"20 sided dice": {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                          7: '7', 8: '8', 9: '9', 10: '10', 11: '11', 12: '12',
                          13: '13', 14: '14', 15: '15', 16: '16', 17: '17',
                          18: '18', 19: '19', 20: '20'}
        },
    }


current_select = 1
current_dice = list_of_dice[current_select]
dice_fr = ""  # Stands for Dice for roll. Is the dictionary used for rolls
past_rolls = []
rolls = []
dupe = []
total = 0
special_options = False
end_program = False
end_roll = False


# #

# # Functions


def menu():
    '''
    returns the main menu of the program and all it's options
    '''
    return(
        "     -------------------------\n"
        "     -      Dice Utility     -\n"
        "     -------------------------\n"
        "     - 1: Roll Dice          -\n"
        "     - 2: Choose Dice        -\n"
        "     - 3: Make Your Own Dice -\n"
        "     - 4: About              -\n"
        "     - 5: Exit               -\n"
        "     -------------------------")


def clmepcd():
    '''
    stands for menu(), clear() and returns a string that
    tells the user their current selected dice. Does each in order.
    '''
    system('cls')
    print(menu())
    return f"\nCurrent Selected Dice: {only_key(current_select)}"


def funky_dice():
    '''
    using user input, this creates a new dice and adds it to list_of_dice.
    '''
    # was the original inspiration for my week10 learn together though
    # this function was alot harder to figure out since nested dictionaries
    # made it a nightmare for me.
    custom_dice = {}

    print("Here's a blank dice. You are free to customize this dice."
          "\nThe sides can be anything you want them to be."
          "\nThe only limits are that your dice can't have less than 4 sides."
          "\nOtherwise, your dice wouldn't really be a dice now.\n\n")

    amount_of_sides = input("How many sides do you want this dice to"
                            " have?\n>> ")

    if amount_of_sides in chars_list:
        amount_of_sides = 0
    if int(amount_of_sides) > 3:
        new_dice = input("\nWhat do you want to name this dice?\n>> ")
        new_index = len(list_of_dice)
        for number in range(1, int(amount_of_sides) + 1):
            face = input(f"\nWhat do you want side {number} to be?\n>> ")
            custom_dice[number] = face
            print(f"The value of side {number} is set to {face}")

        # After struggling for a good amount of time, I was able to discover
        # this python function on stackoverflow that solved my issue.
        # https://stackoverflow.com/questions/62867106/how-to-add-an-existing-dictionary-as-a-nested-dictionary-to-an-already-existing
        list_of_dice.update({new_index: {new_dice: custom_dice}})
        print(clmepcd())
        return f'{new_dice} is now available to be selected in "2: Choose"'
    else:
        system('cls')
        funky_dice()


def only_key(number):
    '''
    using a number it returns a key for a nested
    dictionary inside list_of_dice
    '''
    for key in list_of_dice[number]:
        return key


def select_menu():
    '''
    takes the keys inside list_of_dice and prints them to the screen more
    clearly
    '''
    dice_menu = []
    for number in range(len(list_of_dice)):
        dice_menu.append(f"{number}: {only_key(number)}")
    for item in dice_menu:
        print(item)


def about():
    '''
    returns a large block of text that informs user about the program
    '''
    system('cls')
    return ("\nDice Utility is a program meant to mimic dices and their "
            "applications."
            "\nAnything from simply rolling a dice to get "
            "a result."
            "\nOr for board game purposes.\nThere is more things"
            " you can do with the Dice Utility."
            "\nYou can make custom dices"
            " that can have any value on their sides or faces."
            "\nYou can also tally up the amount of times you've rolled a"
            "certain result."
            "\nOr you can get the sum of all the rolls you've done in a single"
            " session."
            "\nThere is also special options that can be turned on or off that"
            " let you change the result of a roll with addition or subtraction"
            ".\nThey are also turned off by default."
            "\nIt is currently not available for custom dice."
            "\nOverall the Dice Utility is a versitile dice tool.")


def select_dice():
    '''
    Gives user prompts and returns an integer
    '''
    select_menu()
    select = input("Type the number next to the dice you wish to use."
                   "\n>> ")
    if select in chars_list or int(select) > len(list_of_dice) - 1:
        print(clmepcd())
        print("Your input was invalid")
        local_select = 1
        return local_select
    else:
        local_select = int(select)
        return local_select


def options():
    '''
    prompts the user and returns a string that depends on the input
    '''
    # Only available for non custom dice
    global special_options
    if special_options is False:
        onof1 = "on"
        onof2 = "on"
    else:
        onof1 = "off"
        onof2 = "off"
    s_option = input(f"Do you want to turn {onof1} special options?\n"
                     "Type 'Y' for Yes or 'N' for No"
                     "\n>> ").lower()
    if s_option == 'y':
        special_options = True
    elif s_option == 'n':
        special_options = False
    else:
        return ""
    print(clmepcd())
    return f"\nSpecial Options are {onof2}."


def roll():
    '''
    gets a random value from the dictionary dice_fr and returns it
    '''
    result = ""
    result = dice_fr[random.randint(1, int(dice_length))]
    return result


def get_result():
    '''
    gets a value, appends it to past_rolls and returns a string
    '''
    roll_result = roll()
    # only applies if special_options is True
    if special_options is True:
        f"\nYour roll was a {roll_result}."
        change = input("Do you want to change the value of your roll?"
                       "\nType 'Y' for Yes and 'N' for No\n"
                       ">> ").lower()
        if change == "y":
            amount = input("Type the number you want to use to change the "
                           "current roll you have with.\n>> ")
            if amount in chars_list:
                print("That's not a valid response. Nothing will happen then.")
            else:
                addsub = input("Type a 1 to add or a 2 to subtract from the"
                               " current roll.\n>> ")
                if addsub == "1":
                    roll_result = str(int(roll_result) + int(amount))
                elif addsub == "2":
                    roll_result = str(int(roll_result) - int(amount))
                else:
                    print("Nothing happened.")
    past_rolls.append(roll_result)
    return f"\nYou roll the dice and get {roll_result}."


def tally_rolls():
    '''
    prints the total amount of times a certain value of a dice appeared after a
    dice rolling session.
    '''
    total = 0
    for number in rolls:
        tally = 0
        if number not in dupe:
            dupe.append(number)
            for value in rolls:
                if value in dupe and value == number:
                    tally += 1
                    total += 1
            if tally == 1:
                time = "time"
            elif tally > 1:
                time = "times"
            print(f"You rolled a {number}, {tally} {time}.")
    return f"You rolled a total of {total} {time}."


# #

# # Program

print(clmepcd())

print("\nWelcome. You ever need to do things with dice?\n"
      "Well this is the place for you.\n"
      "Because dices are all I know.")

while not end_program:
    dice_fr = list_of_dice[current_select][only_key(current_select)]

    user = input(
        "\nType the number next to the menu option you want to access."
        "\n>> ")

    if user in menu_list:
        if user == "5":
            end_program = True
            print("\nHave a nice day and come back soon.")

        elif user == "4":
            print(about())
            input("\nType anything to go back to the main menu.\n>> ")
            print(clmepcd())

        elif user == "3":
            print(funky_dice())

        elif user == "2":
            old_select = current_select
            current_select = select_dice()
            current_dice = list_of_dice[current_select]
            if old_select != current_select:
                if current_select <= 4 and current_select >= 0:
                    print(options())
                else:
                    print(clmepcd())

        else:
            rolls = []
            past_rolls = []
            dupe = []
            dice_length = len(dice_fr)
            print(get_result())

            while not end_roll:
                again = input("Roll again?\nType 'Y' for Yes and 'N' for no"
                              "\n>> ").lower()
                if again == "y":
                    print(get_result())
                elif again == "n":
                    end_roll = True
                    rolls = sorted(past_rolls)
                    if len(rolls) > 1:
                        question = input("Do you want to see the sum of your "
                                         "rolls and the total times you rolled"
                                         "?\n Type 'Y' for Yes and 'N' for no."
                                         "\n>> ").lower()
                        if question == "y":
                            print(tally_rolls())
                            for number in rolls:
                                total += int(number)
                            print(f"The sum of your rolls is {total}.")
                        elif question == "n":
                            print("Okay continue on.")
                        else:
                            print("That was not a valid response.")

                else:
                    print("That wasn't a valid option.")

    else:
        print("\nThat is not a valid option.")
