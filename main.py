# Import the turtle graphics and pandas library
import turtle
import pandas

# Create a turtle screen and set the title
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the image of the U.S. map as the background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV file containing U.S. states data. saved in var called data
data = pandas.read_csv("50_states.csv")
# Create a list of all the state names from the CSV file
all_states = data.state.to_list()
# Create an empty list to store guessed states
guessed_states = []

# Main game loop: continue until all 50 states are guessed
while len(guessed_states) < 50:
    # Get user input for the state name. for pop up boxes
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Check if the user wants to exit the game
    if answer_state == "Exit":
        # Create a list of states that were not guessed. using list comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #    if state not in guessed_states:
        #          missing_states.append(state)
        # Create a new DataFrame with the missing states
        new_data = pandas.DataFrame(missing_states)
        # Write the missing states to a CSV file named "states_to_learn.csv"
        new_data.to_csv("states_to_learn.csv")
        # Break out of the game loop
        break

    # Check if the guessed state is in the list of all states
    if answer_state in all_states:
        # Add the guessed state to the list of guessed states
        guessed_states.append(answer_state)

        # Create a turtle to display the guessed state's name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Get the coordinates of the guessed state from the DataFrame
        state_data = data[data.state == answer_state]
        # Move the turtle to the specified coordinates and write the state's name
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

