from turtle import Turtle, Screen
import random


def move_all_turtle_to_the_start_point(start_point_y, list_turtles):
    index = 0
    for turtle in list_turtles:
        turtle.up()
        turtle.color(ranbow_colors[index])
        turtle.goto(-390, start_point_y)
        start_point_y += 66
        index += 1


def race_turtle():

    got_to_goal = False
    while not got_to_goal:
        for turtle in list_turtles:
            move_forward = random.choice(list_steps)
            turtle.forward(move_forward)
            print(turtle.position())
            if turtle.xcor() >= 365:
                got_to_goal = True
                color_turtle_who_won = turtle.pencolor()
                break
    if bet_color == color_turtle_who_won:
        turtle.write("YOU WON!!!", True, align="center",
                     font=("Arial", 12, "normal"))
    else:
        turtle.write("YOU LOST!!!", True, align="center",
                     font=("Arial", 8, "normal"))


def main():
    global bet_color
    screen = Screen()
    screen.setup(800, 400)
    screen.bgcolor('grey')
    bet_color = screen.textinput('Turtle Race', 'Who would you bet? '
                                 'yellow, red, orange, purple, blue or pink '
                                 'turtle?: ')

    start_point_y = -160
    move_all_turtle_to_the_start_point(start_point_y, list_turtles)
    race_turtle()
    screen.mainloop()


tim = Turtle('turtle')
jason = Turtle('turtle')
marly = Turtle('turtle')
pluton = Turtle('turtle')
wasock = Turtle('turtle')
pepe = Turtle('turtle')
list_steps = [5, 10, 15, 20]
list_turtles = [tim, jason, marly, pluton, wasock, pepe]
ranbow_colors = ['yellow', 'red', 'orange', 'purple', 'blue', 'pink']
main()
