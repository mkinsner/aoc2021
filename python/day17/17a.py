import re

with open("input.txt") as f:
  lines = f.readlines()

in_data = re.split(": |, |\.\.|=", lines[0].strip())
bounds = [int(in_data[2]), int(in_data[3]), int(in_data[5]), int(in_data[6])]
assert bounds[0] > 0 and bounds[1] > 0 and bounds[2] < 0 and bounds[3] < 0  # Simplify math below

def attempt(h, v, bounds):
  x=0; y=0
  hv = h; vv=v
  maxY = 0
  while x <= bounds[1] and y >= bounds[2]:
    x += hv
    y += vv
    hv = max(hv-1, 0)
    vv -= 1
    if y > maxY:
      maxY = y
    
    if x >= bounds[0] and x <= bounds[1] and y <= bounds[3] and y >= bounds[2]:
      return True, maxY
  
  return False, 0


maxY = 0
for h in range(1,1000):
  for v in range(1,1000):
    hit, max_val = attempt(h,v,bounds)
    if hit and max_val > maxY:
      maxY = max_val

print(maxY)
