paths = []

def traverse (node, end, E, path=[], visited_small=False):
  path = path + [node]  # Grow this path
  #print("Into traverse for node: " + str(node) + " with path now: " + str(path))
  if node == end:
    paths.append(path)
    return
  if (node not in E):
    return

  for n in E[node]:
    if n not in path or n.isupper() or ((not visited_small) and (n != "start")):
      if n in path and n.islower() and not visited_small:
        traverse(n, end, E, path, True)
      else:
        traverse(n, end, E, path, visited_small)

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
