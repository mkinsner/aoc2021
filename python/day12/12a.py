paths = []

def traverse (node, end, E, path=[]):
  path = path + [node]  # Grow this path
#  print("Into traverse for node: " + str(node) + " with path now: " + str(new_path))
  if node == end:
    paths.append(path)
  if (node not in E):
    return

  for n in E[node]:
    if n not in path or n.isupper():
      traverse(n, end, E, path)

with open("input.txt") as f:
  lines = f.readlines()
lines = [l.strip().split("-") for l in lines]

E = {}
for l in lines:
  k,v = l
  E.setdefault(k,[]).append(v)
  E.setdefault(v,[]).append(k)

traverse("start", "end", E)
print(len(paths))
