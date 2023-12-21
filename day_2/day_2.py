import pandas as pd
import numpy as np

# So the format of the input is:
# Game x: a red b gree, c blue; a red b green; a red b green c blue 
# Where a, b, and c are numbers
# And each draw is separated by a semicolon
# But not all games have all three colors and the order is not consistent

# So the plan is to read in the input line by line
# Find the game number and then split the line into a list of draws
# Find the maximum number of each color for each game

running_index_sum = 0
max_red = 12
max_green = 13
max_blue = 14
# Read in the input
with open('input', 'r') as f:
    for line in f:
        # Split the line into a list
        line = line.split(":")
        # Remove the commas separating the colors
        line[1] = line[1].replace(",", "")
        # Remove the newlines at the end of the line
        line[1] = line[1].replace("\n", "")
        # Get the game number
        game = int(line[0].split(" ")[1])
        # Get the draws
        draws = line[1].split(";")
        # Initialize the number of each color
        reds = np.zeros(len(draws))
        greens = np.zeros_like(reds)
        blues = np.zeros_like(reds)
        # For each draw
        for i,draw in enumerate(draws):
            # Split the draw into a list
            draw = draw.split(" ")
            # If the draw has a red
            if "red" in draw:
                # Get the number of red
                reds[i] = (int(draw[draw.index("red") - 1]))
            # If the draw has a green
            if "green" in draw:
                # Get the number of green
                greens[i] = (int(draw[draw.index("green") - 1]))
            # If the draw has a blue
            if "blue" in draw:
                # Get the number of blue
                blues[i] = (int(draw[draw.index("blue") - 1]))
                
        # If the max(color) is greater than the max allowed for that color
        # Then the game is invalid and we don't add the index to the sum
        if max(reds) <= max_red and max(greens) <= max_green and max(blues) <= max_blue:
            running_index_sum += game

print(running_index_sum)