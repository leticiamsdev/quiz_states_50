import  turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
score = 0
answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")

data = pandas.read_csv("50_states.csv")
if data[data["state"]== answer_state]:
    print("ok")

screen.exitonclick()
