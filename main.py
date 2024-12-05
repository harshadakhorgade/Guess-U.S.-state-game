import turtle
import pandas as pd
screen =turtle.Screen()
screen.title("U.S. state game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data =pd.read_csv("50_states.csv")
state_data_list =data.state.to_list()
guessed_state =[]





while len(guessed_state) <=50:
    answer_state = screen.textinput(title=f"{guessed_state}/50 Guess the state..", prompt="What is another state's name ?").title()
    print(answer_state)

    if answer_state == "Exit":
        missed_state =[]
        for state in state_data_list:
            if state not in guessed_state:
                missed_state.append(state)
        df =pd.DataFrame(missed_state)
        df.to_csv("new_data.csv")
        break
    if answer_state in state_data_list:
        guessed_state.append(answer_state)
        t =turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row_data =(data[data.state == answer_state])
        t.goto(state_row_data.x.item(),state_row_data.y.item())
        t.write(answer_state)
        print(type(answer_state))









