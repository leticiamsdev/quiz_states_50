import  turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
t =  turtle.Turtle()
t.hideturtle()
score = 0
data = pandas.read_csv("50_states.csv")
guessed_states = []
while score<50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct"
                                    , prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break

    for row in data["state"]:
        if row == answer_state:
            guessed_states.append(row)
            score = score +1
            t.penup()
            line = data[data.state == row]
            t.goto(line.x.item(), line.y.item())
            t.write(row,  font=("Arial", 16, "bold"))


states_to_learn = pandas.Series()

states_to_learn = data["state"]

for row in guessed_states:
    states_to_learn = states_to_learn[states_to_learn != row]

states_to_learn.to_csv("states_to_learn.csv")


