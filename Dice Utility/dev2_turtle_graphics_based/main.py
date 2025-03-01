from turtle import Screen
from menu import Menu
import time

# https://stackabuse.com/python-circular-imports/
# ^ Used this to better understand importing
# ^ Since I had an issue known as circular importing

# makes sure program_status.txt is written to "True"
with open("./data/program_status.txt", mode="w") as status:
    status.write("True")

# Screen Window Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Dice Ultility: DEV 2")
screen.tracer(0)

screen.listen()

# Class Object Set up
menu = Menu()

# determines if the program loop continues
with open("./data/program_status.txt") as status:
    program_is_on = bool(status.read())

# main program
menu.load_menu()
while program_is_on:
    screen.update()
    time.sleep(0.001)


screen.exitonclick()
