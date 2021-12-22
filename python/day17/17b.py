import re

with open("input.txt") as f:
  lines = f.readlines()

in_data = re.split(": |, |\.\.|=", lines[0].strip())
bounds = [int(in_data[2]), int(in_data[3]), int(in_data[5]), int(in_data[6])]
assert bounds[0] > 0 and bounds[1] > 0 and bounds[2] < 0 and bounds[3] < 0  # Simplify math below

def attempt(h, v, bounds):
  x=0; y=0
  hv = h; vv=v
  while x <= bounds[1] and y >= bounds[2]:
    x += hv
    y += vv
    hv = max(hv-1, 0)
    vv -= 1
    if x >= bounds[0] and x <= bounds[1] and y <= bounds[3] and y >= bounds[2]:
      return True
    if (hv == 0 and x < bounds[0]) or (hv == 0 and x > bounds[1]):
      return False
    if y < bounds[2]:
      return False
  return False

hits = 0
for h in range(0,1000):
  print(h, hits)
  for v in range(bounds[2],10000):
    if attempt(h,v,bounds):
      hits += 1
print(hits)
