with open("input.txt") as f:
  lines = f.readlines()

S = lines.pop(0).strip()
lines.pop(0)

rules = {}
for r in lines:
  s = r.strip().split(" -> ")
  rules[s[0]] = s[1]

for n in range(10):
  S = S[0] + "".join(list(map(lambda x,y: rules[x+y] + y, S[0:-1], S[1:])))
    
# Histogram
f = {}
for c in S:
  f[c] = f.get(c,0) + 1

print(max(f.values()) - min(f.values()))
