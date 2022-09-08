from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="red/green/blue/yellow/purple - Who will win?: ")
y_coordinates = [-100, -50, 0, 50, 100]
colors = ['red', 'green', 'blue', 'yellow', 'purple']
all_turtles = []

for i in range(0, 5):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_coordinates[i])
    all_turtles.append(tim)

if user_bet:
    race_on = True

while race_on:
    for j in all_turtles:
        if j.xcor() > 230:
            race_on = False
            winner_turtle = j.pencolor()
            if winner_turtle == user_bet:
                print(f"You've won! {winner_turtle} turtle is the winner!")
            else:
                print(f"You've lost! {winner_turtle} turtle is the winner!")
        rand_speed = random.randint(0, 10)
        j.forward(rand_speed)

screen.exitonclick()
