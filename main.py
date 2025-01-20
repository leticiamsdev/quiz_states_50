import  turtle

screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")