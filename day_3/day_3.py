
def find_numbers(line):
    ''' Find all the numbers in a string and return tuples of the start and end index of each number. 
        param: line - the string to search for numbers
        return: a list of tuples containing the start and end index of each number
    '''
    numbers = "1234567890"
    found_numbers_indices = []
    found_number = False
    start_index = 0
    end_index = 0
    for i,char in enumerate(line):
        if char in numbers and not found_number:
            found_number = True
            start_index = i#line[end_index:].index(char)
        elif (char not in numbers and found_number):
            found_number = False
            end_index = i-1#line[start_index:].index(char)-1
            found_numbers_indices.append((start_index, end_index))
        elif (char in numbers and found_number and i == len(line)-1):
            end_index = i
            found_numbers_indices.append((start_index, end_index))

    return found_numbers_indices
    
def is_part_number(num_indices, line, line_above=None, line_below=None):
    irrelecvant_chars = "1234567890."
    start_index = num_indices[0]
    end_index = num_indices[1]
    # Check if the number is either at the start of end of the line
    ind_0 = False
    ind_end = False
    if start_index == 0:
        ind_0 = True
    if end_index == len(line)-1:
        ind_end = True
    
    # Just to make things easier we'll create an irrelevant line above or below if none is given
    if line_above == None:
        line_above = ["."] * len(line)
    if line_below == None:
        line_below = ["."] * len(line)
    # Case 1: The number is at the start of the line
    if ind_0: 
        if line[end_index+1] not in irrelecvant_chars:
            return True
        for i in range(start_index, end_index+2):
            if (line_above[i] not in irrelecvant_chars) or (line_below[i] not in irrelecvant_chars):
                return True
    # Case 2: The number is at the end of the line
    elif ind_end:
        if line[start_index-1] not in irrelecvant_chars:
            return True
        for i in range(start_index-1, end_index+1):
            if (line_above[i] not in irrelecvant_chars) or (line_below[i] not in irrelecvant_chars):
                return True
    # Case 3: The number is in the middle of the line
    else:
        if (line[start_index-1] not in irrelecvant_chars) or (line[end_index+1] not in irrelecvant_chars):
            return True
        for i in range(start_index-1, end_index+2):
            if (line_above[i] not in irrelecvant_chars) or (line_below[i] not in irrelecvant_chars):
                return True
    return False

input_fname = "input"
# Load the input file
with open(input_fname) as f:
    lines = f.readlines()

part_num_sum = 0

# First treat the first and last lines as special cases
line = lines[0].strip()
numbers = find_numbers(line)
for num in numbers:
    if is_part_number(num, line, line_below=lines[1].strip()):
        part_num_sum += int(line[num[0]:num[1]+1])
line = lines[-1].strip()
numbers = find_numbers(line)
for num in numbers:
    if is_part_number(num, line, line_above=lines[-2].strip()):
        part_num_sum += int(line[num[0]:num[1]+1])

for i in range(1, len(lines)-1):
    line = lines[i].strip()
    numbers = find_numbers(line)
    for num in numbers:
        if is_part_number(num, line, line_above=lines[i-1].strip(), line_below=lines[i+1].strip()):
            part_num_sum += int(line[num[0]:num[1]+1])

print(f"Part number sum: {part_num_sum}")

# 
def find_asterisk(line):
    ''' Find all the asterisks in a string and return the indices of them
        param: line - the string to search for asterisks
        return: a list of indices of asterisks
    '''
    asterisk_indices = []
    for i,char in enumerate(line):
        if char == "*":
            asterisk_indices.append(i)
    return asterisk_indices

def get_number_indices(num_ranges):
    ''' Unpack the number ranges into a list of indices
        param: num_ranges - a list of tuples containing the start and end index of each number
        return: a list of indices of numbers
    '''
    num_indices = []
    for num_range in num_ranges:
        for i in range(num_range[0], num_range[1]+1):
            num_indices.append(i)
    return num_indices

def num_numbers_surrounded(asterisk_idx, line, line_above=None, line_below=None):
    ''' Check how many numbers surround the asterisk
        param: asterisk_idx - index of the asterisk
        param: line - the string to search for numbers
        param: line_above - the string above the line to search for numbers
        param: line_below - the string below the line to search for numbers
        return: the number of numbers surrounding the asterisk, and the numbers themselves
    '''
    if line_above == None:
        line_above = ["."] * len(line)
    if line_below == None:
        line_below = ["."] * len(line)
    num_surrounding = 0
    surrounding_numbers = []
    # Being by checking the same line as the asterisk
    num_tuples = find_numbers(line)
    for num in num_tuples:
        if asterisk_idx -1 == num[1] or asterisk_idx +1 == num[0]:
            num_surrounding += 1
            surrounding_numbers.append(int(line[num[0]:num[1]+1]))
    # Check the line above
    num_tuples = find_numbers(line_above)
    for num in num_tuples:
        num_range = range(num[0], num[1]+1)
        hit_range = range(asterisk_idx-1, asterisk_idx+2)
        if any(num in hit_range for num in num_range):
            num_surrounding += 1
            surrounding_numbers.append(int(line_above[num[0]:num[1]+1]))
    # Check the line below
    num_tuples = find_numbers(line_below)
    for num in num_tuples:
        num_range = range(num[0], num[1]+1)
        hit_range = range(asterisk_idx-1, asterisk_idx+2)
        if any(num in hit_range for num in num_range):
            num_surrounding += 1
            surrounding_numbers.append(int(line_below[num[0]:num[1]+1]))
    return num_surrounding, surrounding_numbers

# First treat the first and last lines as special cases
line = lines[0].strip()
asterisks = find_asterisk(line)
gear_ratio_sum = 0
for asterisk in asterisks:
    num_surrounding, surrounding_numbers = num_numbers_surrounded(asterisk, line, line_below=lines[1].strip())
    if num_surrounding == 2:
        gear_ratio_sum += surrounding_numbers[0] * surrounding_numbers[1]
line = lines[-1].strip()
asterisks = find_asterisk(line)
for asterisk in asterisks:
    num_surrounding, surrounding_numbers = num_numbers_surrounded(asterisk, line, line_above=lines[-2].strip())
    if num_surrounding == 2:
        gear_ratio_sum += surrounding_numbers[0] * surrounding_numbers[1]

# Now do the rest of the lines
for i in range(1, len(lines)-1):
    line = lines[i].strip()
    asterisks = find_asterisk(line)
    for asterisk in asterisks:
        num_surrounding, surrounding_numbers = num_numbers_surrounded(asterisk, line, line_above=lines[i-1].strip(), line_below=lines[i+1].strip())
        if num_surrounding == 2:
            gear_ratio_sum += surrounding_numbers[0] * surrounding_numbers[1]

print(f"Gear ratio sum: {gear_ratio_sum}")
