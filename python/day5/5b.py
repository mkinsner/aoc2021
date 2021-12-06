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
  line_length = np.absolute(l[0:2] - l[2:4])
  # Only care about horiz/vert/diagonal lines.  Skip the rest
  if line_length[0] != line_length[1] and not (line_length[0] == 0 or line_length[1] == 0): continue

  num_points_to_mark = max(line_length)
  d = [l[2] - l[0], l[3] - l[1]] / num_points_to_mark
  x = l[0]; y = l[1]

  for t in range(0, max(line_length)+1):
    board[x+int(d[0])*t, y+int(d[1])*t] += 1

two_or_more = board >= 2
print(np.sum(two_or_more))
