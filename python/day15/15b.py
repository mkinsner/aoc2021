import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

inlist = [list(l.strip()) for l in lines]
A = np.array(inlist, dtype=int)
assert A.shape[0] == A.shape[1]
bound = A.shape[0]

# Repeat input incrementing values block-wise
A = np.tile(A,(5,5))
for x,y in np.ndindex(5,5):
  A[bound*x:bound*(x+1), bound*y:bound*(y+1)] += x+y
A[A > 9] -= 9
bound = A.shape[0]
print(A.shape)

# Modified Dijkstra's algorithm - only track intermediate vals that have been visited
source = (0,0)
dest = (bound-1, bound-1)
dist = {}
visited = set()

dist[source] = 0

while dist:
  min_dist_key = min(dist, key=dist.get)
  min_dist_val = dist.pop(min_dist_key)
  visited.add(min_dist_key)
  print(len(dist))
  
  if min_dist_key == dest:
    print("DONE")
    print(min_dist_val)
    break

  # For unvisited neighbours of current location
  newC = np.repeat([min_dist_key],4,axis=0) + np.array([[1,0], [-1,0], [0,1], [0,-1]])
  for i in newC:
    if any(i<0) or any(i>=bound):
      continue
    i = tuple(i)
    cand_dist = min_dist_val + A[i]
    if i in visited:
      continue
    if i not in dist:
      dist[i] = cand_dist
    else:
      if cand_dist < dist[i]:
        dist[i] = cand_dist

