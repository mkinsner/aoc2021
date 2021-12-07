import numpy as np

with open("input.txt") as f:
  lines = f.readlines()
in_data = lines[0].strip().split(",")

ages = np.zeros(9, int)  # index is age, content is number fish of that age
for f in in_data: ages[int(f)] += 1 

count = 0
for day in range(256):
  new_spawning = ages[0]
  ages[:-1] = ages[1:]
  ages[8] = new_spawning
  ages[6] += new_spawning

print(sum(ages))
