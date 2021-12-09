import numpy as np

with open("input.txt") as f:
  lines = f.readlines()
lines = [l.strip().split(" | ") for l in lines]

outputs = [i[1].split(" ") for i in lines]
outputs = [l for sl in outputs for l in sl]

lengths = np.array(list(map(len, outputs)))
print(sum((lengths == 2) | (lengths == 4) | (lengths == 3) | (lengths == 7)))
