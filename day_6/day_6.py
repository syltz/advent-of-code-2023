import numpy as np
data_fname = "input"
with open(data_fname, "r") as df:
    data = df.readlines()

data[0] = data[0].strip().split(":")
times = data[0][1].strip().split()
times = [int(t) for t in times]
data[1] = data[1].strip().split(":")
distances = data[1][1].strip().split()
distances = [int(d) for d in distances]

indices = [i for i in range(len(times))]
ways_to_win_list = []

for i, t, d in zip(indices, times, distances):
    ways_to_win = 0
    for tprime in range(1, t):
        if tprime * (t-tprime) > d:
            ways_to_win += 1
    ways_to_win_list.append(ways_to_win)

print(np.prod(ways_to_win_list))