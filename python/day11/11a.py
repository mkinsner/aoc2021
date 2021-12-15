import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

lines = [list(l.strip()) for l in lines]
g_orig = np.array(lines, dtype=int)
g = np.zeros(np.array(g_orig.shape)+2, dtype=int)
g[1:-1,1:-1] = g_orig

flashes = 0
for step in range(1,101):
  print(step)
  g[1:-1,1:-1] += 1
  while(np.any(g>9)):
    for i in np.transpose(np.nonzero(g>9)):
      # Mark this octopus as flashed
      x,y = i
      g[x,y] = 0
      flashes += 1
      # Increment neighbours that haven't already flashed this step
      win = g[x-1:x+2, y-1:y+2]
      win[win>0] += 1

print(flashes)
