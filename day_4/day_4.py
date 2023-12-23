
data_fname = "input"

total_points = 0
with open(data_fname, "r") as df:
    line = df.readline()
    while line:
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
        line = df.readline()
print(f"Total points: {total_points}")
