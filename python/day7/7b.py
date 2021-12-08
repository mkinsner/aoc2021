import numpy as np

with open("input.txt") as f:
  in_data = f.readline().strip().split(",")
in_data = list(map(int,in_data))

p = np.zeros((max(in_data)+1), dtype=int) # Index = position, content = number with that position
for i in in_data: p[i] += 1
costs = np.ndarray((p.size, p.size), dtype=int)

for b in range(p.size):
  for i in range(p.size):
    dist = abs(i-b)
    costs[b,i] = dist*(dist+1)/2*p[i]  # series 1+2+...+n is n(n+1)/2

costs = np.sum(costs,axis=1)
print(min(costs))

