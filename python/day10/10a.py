import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

opening = {"(", "[", "{", "<"}
val = {'(':3, '[':57, '{':1197, '<':25137, ')':3, ']':57, '}':1197, '>':25137}

a = 0
for l in lines:
  s = []
  for c in list(l.strip()):
    if c in opening:
      s.append(c)
    else:
      d=s.pop()
      if(val[c] != val[d]):
        a += val[c]
        break
print(a)

