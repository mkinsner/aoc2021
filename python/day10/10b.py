import numpy as np
import statistics as stat

with open("input.txt") as f:
  lines = f.readlines()

opening = {"(", "[", "{", "<"}
val = {'(':1, '[':2, '{':3, '<':4, ')':1, ']':2, '}':3, '>':4}

scores=[]
for l in lines:
  s = []
  line_valid=True
  for c in list(l.strip()):
    if c in opening:
      s.append(c)
    else:
      d=s.pop()
      if(val[c] != val[d]):
        line_valid=False
        break
  if line_valid:
    r=0
    while s:
      c=s.pop()
      r*=5
      r+=val[c]
    scores.append(r)

print(stat.median(np.flip(scores)))

