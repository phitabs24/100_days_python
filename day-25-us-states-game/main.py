import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_text = turtle.Turtle()
state_text.hideturtle()
state_text.pu()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_values = data.x.to_list()
y_values = data.y.to_list()
guessed_states = []


answer_state = screen.textinput(title="Guess State", prompt="What's the name of the state?").title()
game_on = True

while len(guessed_states) < 50:
    if answer_state == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        new_list = pandas.DataFrame(missed_states)
        new_list.to_csv("learn.csv")
    if answer_state in states:
        guessed_states.append(answer_state)
        s_index = states.index(answer_state)
        new_x = x_values[s_index]
        new_y = y_values[s_index]
        state_text.goto(new_x, new_y)
        state_text.write(answer_state)
    score = len(guessed_states)
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()



screen.mainloop()
