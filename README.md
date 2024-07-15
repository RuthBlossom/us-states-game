# U.S. States Game

## Overview
This Python script implements a simple game to help users learn the names of U.S. states. The game displays a blank map of the United States, and the user is prompted to enter the names of the states. As the user correctly guesses state names, they are displayed on the map. The game continues until all 50 states have been guessed or the user chooses to exit.

![states game](https://github.com/user-attachments/assets/eed74261-96a3-4485-9f3a-53f9805298a4)
![united states game](https://github.com/user-attachments/assets/da570a54-c9c4-40ca-bcc7-2c93ad68c384)


## Prerequisites
- Python 3.x
- pandas (`pip install pandas`)
- turtle graphics library (usually included in standard Python installations)

## Usage
1. Ensure that the script file (`us_states_game.py`) is in the same directory as the `50_states.csv` file and the `blank_states_img.gif` image file.
2. Run the Python script using your preferred Python interpreter.
3. Follow the prompts to enter the names of U.S. states.
4. To exit the game at any time, enter "Exit" when prompted for a state name.
5. Upon exiting the game, a CSV file named `states_to_learn.csv` will be generated in the same directory, containing the names of the states that were not guessed. This file can be used to review the missed states later.

## Customization
- You can customize the game by modifying the input data file (`50_states.csv`) to include additional information about the states or by using a different map image.
- To adjust the appearance of the map or text display, you can modify the turtle graphics settings in the script.

## Notes
- The game's main loop continues until all 50 states are guessed correctly or until the user chooses to exit.
- The game records the states that were not guessed correctly and saves them to a CSV file (`states_to_learn.csv`) for further review.
- Feel free to modify and expand upon the script to add more features or to customize it according to your preferences.

## Disclaimer
This game is for educational and entertainment purposes only. 
---

