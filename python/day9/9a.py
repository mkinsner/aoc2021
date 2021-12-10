import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

lines = [list(l.strip()) for l in lines]
a = np.array(lines, dtype=int)
orig = a[:]
  
# Create replicated halo that's larger
a = np.c_[a[:,0]+1, a, a[:,-1]+1]
a = np.r_[[a[0,:]+1], a, [a[-1,:]+1]]

local_min = (a[1:-1,1:-1] < a[1:-1,0:-2]) & \
            (a[1:-1,1:-1] < a[1:-1,2:]) & \
            (a[1:-1,1:-1] < a[0:-2,1:-1]) & \
            (a[1:-1,1:-1] < a[2:,1:-1])
print(np.sum(orig[local_min]+1))
