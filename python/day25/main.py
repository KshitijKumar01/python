import pandas as pd
import turtle

PATH1 = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day25\\50_states.csv"
PATH2 = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day25\\blank_states_img.gif"
PATH3 = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day25\\"



screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(PATH2)
turtle.shape(PATH2)

data = pd.read_csv(PATH1)
# print(data)

states = data["state"].tolist()
x_coor = data["x"].tolist()
y_coor = data["y"].tolist()
print(states)
score = 0
guessed_states = []
missing_states = []
while len(guessed_states) < 50:
    score = len(guessed_states)

    answer = screen.textinput(title=f"{score}/{len(states)} States Correct", prompt="What is you next choice?")
    answer = answer.title()

    if answer == "Exit":
        for state in states:
            if(state not in guessed_states):
                missing_states.append(state)
        break


    if(answer in states):
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        answer_index = states.index(answer)
        state_coor = (int(x_coor[answer_index]), int(y_coor[answer_index]))
        t.goto(state_coor)
        t.write(answer)
        guessed_states.append(answer)

data_dict = {"missing_states" : missing_states}
df = pd.DataFrame(data_dict)
print(df)

df.to_csv(PATH3 + "Missing_states.csv")