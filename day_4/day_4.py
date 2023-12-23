import numpy as np
data_fname = "input"

total_points = 0
with open(data_fname, "r") as df:
    lines = df.readlines()

for i,line in enumerate(lines):
    winning_nums, my_nums = line.split(":")[1].split("|")
    winning_nums = winning_nums.strip().split()
    my_nums = my_nums.strip().split()
    no_of_winning_nums = 0
    # Check how many of my_nums are in winning_nums
    for num in my_nums:
        if num in winning_nums:
            no_of_winning_nums += 1
    if no_of_winning_nums > 0:
        total_points += 2 ** (no_of_winning_nums - 1)
print(f"Total points: {total_points}")

# Part 2, the multiplier
multiplier = np.ones(len(lines))
for i in range(len(lines)):
    line = lines[i]
    winning_nums, my_nums = line.split(":")[1].split("|")
    winning_nums = winning_nums.strip().split()
    my_nums = my_nums.strip().split()
    no_of_winning_nums = 0
    # Check how many of my_nums are in winning_nums
    for num in my_nums:
        if num in winning_nums:
            no_of_winning_nums += 1
    if i+no_of_winning_nums+1 < len(lines):
        for j in range(i+1, i+no_of_winning_nums+1):
            multiplier[j] += 1*multiplier[i]
    else:
        for j in range(i+1, len(lines)):
            multiplier[j] += 1*multiplier[i]
print(f"Total number of card: {int(np.sum(multiplier))}")

