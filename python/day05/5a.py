import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

lines = [l.strip().split(" -> ") for l in lines]
coords = [sl.split(",") for l in lines for sl in l]
coords = np.array(coords, dtype=int)
board_size = np.max(coords, axis=0)+1  # +1 since zero-based indices
coords = coords.reshape(-1,4)  # both endpoints on same row

board = np.zeros(board_size, dtype=int)

for l in coords:
  if l[0] != l[2] and l[1] != l[3]:  # Skip non-horiz/vert lines
    continue
  if l[0] > l[2]: l[0],l[2] = l[2],l[0] # always increasing coords
  if l[1] > l[3]: l[1],l[3] = l[3],l[1] # always increasing coords
  for x in range(l[0], l[2]+1):
    for y in range(l[1], l[3]+1):
      board[x,y] += 1

two_or_more = board >= 2
print(np.sum(two_or_more))
