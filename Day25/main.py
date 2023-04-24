import turtle
import pandas

#add image to game and add us map
screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#import states data and create new turtle object(instance?)
states_data = pandas.read_csv("50_states.csv")
state_list = states_data['state'].to_list()

#create new turtle to write states
new_state = turtle.Turtle()
new_state.hideturtle()
new_state.penup()
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in correct_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        correct_states.append(answer_state)
        state = states_data[states_data.state == answer_state]
        new_state.goto(int(state.x),int(state.y))
        new_state.write(answer_state)

turtle.mainloop()

#this is what I originally wrote outside of the while loop to transfer data to csv
# learn_states = []
#
# for x in state_list:
#     if x not in correct_states:
#         learn_states.append(x)
#
# data_dict = {
#     "Unlearned_states": learn_states,
# }
# Remaining_states = pandas.DataFrame(data_dict)
# Remaining_states.to_csv("unlearned_states")


#this is what I originally wrote for the while loop
#correct_states = 0

# continue_guessing = True
# while continue_guessing:
#     answer_state = screen.textinput(title= f"{correct_states}/50 States Correct", prompt="What's another state's name?")
#     user_answer = answer_state.title()
#     if user_answer in state_list:
#         correct_states += 1
#         state = states_data[states_data.state == user_answer]
#         state_x = int(state.x)
#         state_y = int(state.y)
#         new_state.goto(state_x,state_y)
#         new_state.write(user_answer)
#     elif user_answer == 'Quit':
#         continue_guessing = False
#     elif user_answer != state_list:
#         continue_guessing = True

#get x,y coordinates for mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)