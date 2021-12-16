import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

coords = []
directions = []
stage = 0
for l in lines:
  l = l.strip()
  if l:
    if stage == 0:
      coords.append(l.split(","))
    else:
      directions.append(l.split(" ")[2].split("="))
  else: # Newline separator in input
    stage=1

coords = np.array(coords, dtype=int)
bounds = coords.max(axis=0)
M = np.zeros(np.flip(bounds)+1, dtype=int)

for c in coords:
  M[c[1], c[0]] = 1

for f in directions:
  val = int(f[1])
  if f[0] == "x":
    left_rows = val
    right_rows = M.shape[1]-left_rows-1
    siz = max(left_rows, right_rows)
    new_M = np.empty((M.shape[0], siz), dtype=int)
    new_M[:, siz-left_rows:siz] = M[:, 0:left_rows]
    new_M[:, siz-right_rows:siz] += M[:, -1:-right_rows-1:-1]
    M = new_M
    print(np.sum(M>0))
    break
  else:
    print("up")
    top_rows = val
    bot_rows = M.shape[0]-top_rows-1
    siz = max(top_rows, bot_rows)
    new_M = np.empty((siz, M.shape[1]), dtype=int)
    new_M[siz-top_rows:siz, :] = M[0:top_rows, :]
    new_M[siz-bot_rows:siz, :] += M[-1:-bot_rows-1:-1, :]
    M = new_M
    print(np.sum(M>0))
    break

