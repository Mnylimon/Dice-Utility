from turtle import Turtle
import random

# Constants
MENU_FONT = ("Rockwell", 36, "bold")
PAGE_FONT = ("Rockwell", 24, "normal")
FONT = ("Rockwell", 12, "normal")
BUTTON_POS = [(150, 160), (150, 100), (150, 40),
              (150, -20), (150, -80), (150, -140), (150, -200)]
BUTTON_LIST = [0, 1, 2, 3, 4, 5, 6]


class Dice(Turtle):
    def __init__(self, sides, name) -> None:
        super().__init__()
        # General Turtle Things
        self.shape("square")
        self.color("white")
        self.pencolor("black")
        self.penup()
        self.hideturtle()
        #

        self.sides = sides  # num of sides a dice has
        self.name = name  # name of the dice
        self.roll_results = []  # num of rolls
        self.current_roll = 0  # current roll result
        self.total_roll = 0  # sum of rolls
        # list for add and subtract buttons
        self.roll_change = []
        self.create_buttons()

        # function for buttons
        self.roll_change[0].onclick(self.click_add10)
        self.roll_change[1].onclick(self.click_add5)
        self.roll_change[2].onclick(self.click_add1)
        self.roll_change[3].onclick(self.click_roll)
        self.roll_change[4].onclick(self.click_sub1)
        self.roll_change[5].onclick(self.click_sub5)
        self.roll_change[6].onclick(self.click_sub10)

    def create_buttons(self):
        '''creates the menuObjects that act as buttons'''
        from menu import MenuObject

        add10 = MenuObject("+10 to roll", None)
        add5 = MenuObject("+5 to roll", None)
        add1 = MenuObject("+1 to roll", None)

        finish = MenuObject("Roll Again", None)

        sub1 = MenuObject("-1 to roll", None)
        sub5 = MenuObject("-5 to roll", None)
        sub10 = MenuObject("-10 to roll", None)

        self.roll_change.append(add10)
        self.roll_change.append(add5)
        self.roll_change.append(add1)
        self.roll_change.append(finish)
        self.roll_change.append(sub1)
        self.roll_change.append(sub5)
        self.roll_change.append(sub10)

    def change_selected_dice(self):
        '''changes the txt file that holds the name of the selected dice'''
        with open("./data/current_dice.txt", mode="w") as data:
            data.write(f"{self.name}")

    def roll(self):
        '''gets a random value from the faces list'''
        self.current_roll = random.randint(1, int(self.sides))
        self.update_display()

    def load(self):
        '''same as load for menuobject class objects'''
        self.showturtle()
        self.write(f"{self.name}\n", align="center", font=FONT)

    def unload(self):
        '''hides the turtle and clears all writing from turtle'''
        self.hideturtle()
        self.clear()

    def update_display(self):
        '''updates the current roll value'''
        self.clear()
        self.goto(0, 0)
        self.write(f"{self.current_roll}", align="center", font=MENU_FONT)
        self.goto(-150, 200)
        self.write(f"Total: {self.total_roll}", align="center", font=FONT)
        self.goto(-150, 140)
        self.write(f"Times Rolled: {len(self.roll_results)}",
                   align="center", font=FONT)
        self.goto(0, 240)
        self.write(
            f"Current Dice: {self.name}",
            align="center",
            font=PAGE_FONT
          )
        self.load_buttons()

    def clear_display(self):
        '''clears the screen'''
        self.unload()
        for object in self.roll_change:
            object.refresh()

    def new_roll(self):
        '''the roll that is used to continue rolling after the initial roll'''
        self.roll_results.append(self.current_roll)
        self.current_roll = 0
        self.get_total()
        self.roll()
        self.update_display()

    def get_total(self):
        '''gets the total from all your rolls'''
        self.total_roll = 0
        for num in self.roll_results:
            self.total_roll += num

    def load_buttons(self):
        '''displays the roll change buttons'''
        counter = 0
        for button in self.roll_change:
            button.goto(BUTTON_POS[counter])
            button.load()
            counter += 1

    def click_add1(self, x, y):
        '''applies the add1'''
        self.current_roll += 1
        self.update_display()

    def click_add5(self, x, y):
        '''applies the add5'''
        self.current_roll += 5
        self.update_display()

    def click_add10(self, x, y):
        '''applies the add10'''
        self.current_roll += 10
        self.update_display()

    def click_sub1(self, x, y):
        '''applies the sub1'''
        self.current_roll -= 1
        self.update_display()

    def click_sub5(self, x, y):
        '''applies the sub5'''
        self.current_roll -= 5
        self.update_display()

    def click_sub10(self, x, y):
        '''applies the sub10'''
        self.current_roll -= 10
        self.update_display()

    def click_roll(self, x, y):
        '''roll but for on click'''
        self.new_roll()
