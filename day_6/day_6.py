import numpy as np
data_fname = "input"
with open(data_fname, "r") as df:
    data = df.readlines()

data[0] = data[0].strip().split(":")
data[1] = data[1].strip().split(":")
times = data[0][1].strip().split()
distances = data[1][1].strip().split()
time_p2 = ''
distance_p2 = ''
for t, d in zip(times, distances):
    time_p2 += t
    distance_p2 += d
time_p2 = int(time_p2)
distance_p2 = int(distance_p2)
times = [int(t) for t in times]
distances = [int(d) for d in distances]

indices = [i for i in range(len(times))]
ways_to_win_list = []

for i, t, d in zip(indices, times, distances):
    ways_to_win = 0
    for tprime in range(1, t):
        if tprime * (t-tprime) > d:
            ways_to_win += 1
    ways_to_win_list.append(ways_to_win)

print(f"Part one number of ways to win: {np.prod(ways_to_win_list)}")


print(f"Time for part two: {time_p2}")
print(f"Distance for part two: {distance_p2}")

ways_to_win = 0
for tprime in range(1, time_p2):
    if tprime * (time_p2-tprime) > distance_p2:
        ways_to_win += 1
print(f"Part two number of ways to win: {ways_to_win}")