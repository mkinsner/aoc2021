import numpy as np
import scipy.ndimage as npi
from operator import mul
from functools import reduce

with open("input.txt") as f:
  lines = f.readlines()
lines = [list(l.strip()) for l in lines]
a = np.array(lines, dtype=int)

labelled, num_feat = npi.label(a < 9)
sizes = [np.sum(labelled==i) for i in range(1,num_feat+1)]
print(reduce(mul, np.flip(np.sort(sizes))[0:3]))
