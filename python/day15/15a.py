import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

inlist = [list(l.strip()) for l in lines]
A = np.array(inlist, dtype=int)
assert A.shape[0] == A.shape[1]
bound = A.shape[0]
print(A.shape)

# Dijkstra's algorithm
source = (0,0)
dest = (bound-1, bound-1)
dist = {}

for x,y in np.ndindex(bound,bound):
  dist[(x,y)] = 1E10
dist[source] = 0

while dist:
  min_dist_key = min(dist, key=dist.get)
  min_dist_val = dist.pop(min_dist_key)
  print(len(dist))
  
  if min_dist_key == dest:
    print("DONE")
    print(min_dist_val)
    break

  # For unvisited neighbours of current location
  newC = np.repeat([min_dist_key],4,axis=0) + np.array([[1,0], [-1,0], [0,1], [0,-1]])
  for i in newC:
    i = tuple(i)
    if i in dist:  # If in unvisited set
      cand_dist = min_dist_val + A[i]
      if cand_dist < dist[i]:
        dist[i] = cand_dist

