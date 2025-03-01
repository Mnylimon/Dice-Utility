from turtle import Turtle
from dice import Dice

# https://www.geeksforgeeks.org/turtle-onclick-function-in-python/
# ^ is where I figured out how turtle.onclick works

MENU_FONT = ("Rockwell", 48, "bold")
TITLE_FONT = ("Rockwell", 36, "bold")
PAGE_FONT = ("Rockwell", 24, "normal")
FONT = ("Rockwell", 12, "normal")


TITLE_POSITION = (0, 200)
RESET_POS = (0, 0)
PAGE_POSITION = (30, -175)
MENU_POSIITIONS = [(0, 100), (0, 40), (0, -20), (0, -80), (0, -140)]
BACK_BUTTON_POS = (-200, -250)


class MenuObject(Turtle):
    def __init__(self, name, content) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.pencolor("black")
        self.hideturtle()
        self.name = name
        self.content = content

    def refresh(self):
        '''Hides the menu object and clears any writing done by the object'''
        self.clear()
        self.hideturtle()

    def load(self):
        '''unhides the menu object'''
        self.showturtle()
        self.display_name()

    def display_name(self):
        '''writes the object's name to the screen'''
        self.write(f"{self.name}\n", align="center", font=FONT)

    def load_page(self):
        self.load_title()
        self.goto(PAGE_POSITION)
        self.write(f"{self.content}", align="center", font=FONT)

    def load_title(self):
        self.goto(TITLE_POSITION)
        self.write(f"{self.name}", align="center", font=TITLE_FONT)


class Menu(MenuObject):
    def __init__(self) -> None:
        super().__init__(name="Go to Main Menu", content=[
            main_function, option, about, end_program
        ])
        self.title = "DICE UTILITY"
        with open("./data/current_dice.txt") as data:
            self.current_die = data.read()

        self.onclick(self.click_menu)
        self.content[0].onclick(self.click_roll)
        self.content[1].onclick(self.click_option)
        self.content[2].onclick(self.click_about)
        self.content[3].onclick(self.click_end)

    def load_menu(self):
        '''displays the main menu'''
        self.unload_menu()
        counter = 0
        self.goto(TITLE_POSITION)
        self.write(f"{self.title}", align="center", font=MENU_FONT)
        self.goto(0, 160)
        with open("./data/current_dice.txt") as data:
            self.current_die = data.read()
        self.write(
            f"Current Dice: {self.current_die}",
            align="center",
            font=PAGE_FONT
          )
        for object in self.content:
            object.goto(MENU_POSIITIONS[counter])
            object.load()
            counter += 1

    def unload_menu(self):
        '''Hides the main menu'''
        self.refresh()
        for object in self.content:
            object.refresh()

    def menu_button(self):
        '''reveals the go to main menu button'''
        self.goto(BACK_BUTTON_POS)
        self.load()

    def unload_to_button(self):
        '''unloads the page but shows the menu button'''
        self.unload_menu()
        self.menu_button()

    def click_menu(self, x, y):
        '''loads the main menu when the button is clicked'''
        self.content[0].clear_dice()
        self.content[1].clear_dice()
        self.load_menu()

    def click_roll(self, x, y):
        '''causes the currently selected dice to be rolled'''
        self.unload_to_button()
        self.content[0].click_dice()

    def click_option(self, x, y):
        '''unloads the main menu and goes to the select dice page'''
        self.unload_to_button()
        self.content[1].load_select()

    def click_about(self, x, y):
        '''unloads the main menu and shows the button with the about page'''
        self.unload_to_button()
        self.content[2].load_page()

    def click_end(self, x, y):
        '''sends a goodbye message when quit is clicked'''
        self.unload_menu()
        self.goto(RESET_POS)
        self.write("See you again soon.", align="center", font=TITLE_FONT)


class End_program(MenuObject):
    def __init__(self) -> None:
        super().__init__(name="Quit", content=None)
        self.color("red")
        self.pencolor("black")
        self.onclick(self.end_session)

    def end_session(self, x, y):
        '''updates the txt file that ends the programs loop'''
        with open("./data/program_status.txt", mode="w") as status:
            status.write("False")


# Class Objects
about = MenuObject(
    "About",
    ("Dice Utility is a program\n"
     "meant to mimic dices and their\n"
     "applications. Anything from simply\n"
     "rolling a dice to get a result.\n"
     "Or for board game purposes. There\n"
     "is more things you can do with the\n"
     "Dice Utility. You can make custom\n"
     "dices that can have any value on\n"
     "their sides or faces. You can\n"
     "also tally up the amount of times\n"
     "you've rolled a certain result.\n"
     "Or you can get the sum of all the\n"
     "rolls you've done in a single session.\n"
     "There is also special options that\n"
     "let you change the results of a roll\n"
     "with addition or subtraction")
    )

end_program = End_program()
#

# Dice objects
d4 = Dice(4, "4 Sided Dice")
d6 = Dice(6, "Regular Dice")
d8 = Dice(8, "8 Sided Dice")
d12 = Dice(12, "12 Sided Dice")
d20 = Dice(20, "20 sided Dice")
d100 = Dice(100, "100 sided Dice")
#

# CONSTANTS for the following superclasses
DICE_LIST = [d4, d6, d8, d12, d20, d100]
SELECT_POS = [(0, 100), (0, 40), (0, -20), (0, -80), (0, -140), (0, -200)]


class Options_menu(MenuObject):
    def __init__(self, name) -> None:
        super().__init__(name, content=DICE_LIST)
        with open("./data/current_dice.txt") as data:
            self.current_die = data.read()
        for dice in self.content:
            if dice.name == self.current_die:
                self.selected_dice = dice

        self.content[0].onclick(self.click_dice1)
        self.content[1].onclick(self.click_dice2)
        self.content[2].onclick(self.click_dice3)
        self.content[3].onclick(self.click_dice4)
        self.content[4].onclick(self.click_dice5)
        self.content[5].onclick(self.click_dice6)

    def update_dice(self):
        '''updates the current selected dice'''
        with open("./data/current_dice.txt") as data:
            self.current_die = data.read()
        for dice in self.content:
            if dice.name == self.current_die:
                self.selected_dice = dice

    def load_select(self):
        '''loads the select screen'''
        self.load_title()
        self.goto(0, 160)
        self.update_dice()
        self.write(
            f"Current Dice: {self.current_die}",
            align="center",
            font=PAGE_FONT
          )
        counter = 0
        for dice in self.content:
            dice.goto(SELECT_POS[counter])
            dice.load()
            counter += 1

    def unload_select(self):
        '''unloads the select menu'''
        self.refresh()
        for object in self.content:
            object.unload()

    def clear_dice(self):
        '''clears the dice objects and their writing'''
        for dice in self.content:
            dice.clear_display()

    def change_dice(self, n):
        '''the function that actually changes the active dice'''
        self.content[n].change_selected_dice()
        self.unload_select()
        self.goto(RESET_POS)
        self.write("Go back to main menu to see changes", align="center",
                   font=PAGE_FONT)

# the same function but for different objects in a list
    def click_dice1(self, x, y):
        self.change_dice(0)

    def click_dice2(self, x, y):
        self.change_dice(1)

    def click_dice3(self, x, y):
        self.change_dice(2)

    def click_dice4(self, x, y):
        self.change_dice(3)

    def click_dice5(self, x, y):
        self.change_dice(4)

    def click_dice6(self, x, y):
        self.change_dice(5)


class Roll_dice(Options_menu):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.color("white")
        self.pencolor("black")

    def click_dice(self):
        '''updates the selected dice and rolls it'''
        self.update_dice()
        self.selected_dice.roll()


# class objects
option = Options_menu("Select a Dice")
main_function = Roll_dice("Roll Dice")
