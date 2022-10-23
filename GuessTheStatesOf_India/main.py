from turtle import Turtle, Screen
import pandas

# data = pandas.read_csv("india_data.csv")
# state_name = data["State Name"].tolist()
# state_x = data["x"].tolist()
# state_y = data["y"].tolist()
# dic = {}
# dic["State Name"] = state_name
# dic["x"] = state_x
# dic["y"] = state_y
#
# df = pandas.DataFrame(dic)
# df.to_csv("india_states_x_y_cor.csv")
# print(dic)
data = pandas.read_csv("india_states_x_y_cor.csv")

# def get_mouse_click_x(x, y):
#     print(x , y)

turtle = Turtle()
write_turtle = Turtle()
write_turtle.hideturtle()
write_turtle.color("red")
write_turtle.penup()
image = "India_Political_600.gif"
screen = Screen()
screen.title("India State Game")
screen.setup(width=600, height=600)
screen.addshape(image)
turtle.shape(image)


# Return x, y co-ordinates as tuple
def get_x_y(data_frame):
    x = int(data_frame.x)
    y = int(data_frame.y)
    return x, y


is_game_on = True
count = 0
all_states = data["State Name"].tolist()
while len(all_states) > 0:
    state_name = screen.textinput(title=f"{count}/28 correct states", prompt="What's another state name ?").title()
    df = data[data["State Name"] == state_name]
    if state_name == "Exit":
        break
    elif df.empty:
        pass
        # write_turtle.goto(-100, 0)
        # write_turtle.write(f"GAME OVER ", align="left", font=('Times New Roman', 20, 'bold'))
        # is_game_on = False
    else:
        # Keep record of states that are missed by removing guessed states from list
        if all_states.count(state_name) == 0:
            pass
        else:
            all_states.remove(state_name)
            count += 1
            name = df["State Name"].tolist()
            co_or = get_x_y(df)
            write_turtle.goto(co_or)
            write_turtle.write(f"{name[0]}", align="left", font=('Times New Roman', 12, 'bold'))

print(f"Guessed States: {count}")
missed_states = pandas.DataFrame(all_states)
missed_states.to_csv("missed_states.csv")

# screen.mainloop()

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# data = pandas.read_csv("india_data.csv")
# print(data["State Name"])






