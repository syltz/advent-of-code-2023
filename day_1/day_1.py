# So the plan is as follows:
# 1. Read the input file
# 2. For each line, find the first and last digit
# 3. Join the first and last digit to form a new number
# 4. Add the new number to a list
# 5. Sum the list
# 6. Print the sum
import numpy as np

# Read the input file
with open('input', 'r') as f:
    input = f.readlines()

# Create an empty list to store the new numbers
new_numbers = []

# For each line in the input file
for line in input:
    # Strip the line of any whitespace
    line = line.strip()
    # Filter out the letters from the line
    line = [char for char in line if char.isdigit()]
    # Find the first and last digit
    first_digit = line[0]
    last_digit = line[-1]
    new_number = first_digit + last_digit
    # Join the first and last digit to form a new number
    # Add the new number to the list
    new_numbers.append(int(new_number))
new_numbers = np.array(new_numbers)
print( 'The sum of the new numbers is: ', np.sum(new_numbers) )