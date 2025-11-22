import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []


while len(guessed_states) <50:
    answer = screen.textinput(title= f"{len(guessed_states)}/ 50. Guess The U.S State", prompt= 'Type the name of a U.S State').title()
    if answer == "Exit":
        unguessed_states = [x for x in states if x not in guessed_states]
        g = pandas.DataFrame(unguessed_states)
        print(unguessed_states)
        # g.to_csv("Unguessed states.csv")
        break

    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(x= state_data.x.item(), y = state_data.y.item())
        t.write(state_data.state.item())
    else:
        answer = screen.textinput(title=f"{len(guessed_states)}/ 50. Guess The U.S State", prompt='You got it wrong,Type the name of a U.S State')







turtle.mainloop()










