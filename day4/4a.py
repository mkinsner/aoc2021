import numpy as np

with open("input.txt") as f:
  draw_seq = f.readline().split(',')
  lines = f.readlines()

lines = [l.strip().split() for l in lines]
board_raw_vals = [i for sl in lines for i in sl]
num_boards = int(len(board_raw_vals) / 25)

A = np.array(board_raw_vals, dtype=int)
A = A.reshape(num_boards,5,5)

mask = np.zeros(A.shape)

for draw in draw_seq:
  print (draw)
  mask = np.logical_or(mask, A==int(draw))
  won = mask.all(axis=1).any(axis=1) | mask.all(axis=2).any(axis=1)
  if (won.any()):
    break

winning_board_num = np.where(won)
win_board_vals = A[winning_board_num,:,:]
unmarked_win_board_vals = win_board_vals[mask[winning_board_num,:,:] == False]
print(np.sum(unmarked_win_board_vals)*int(draw))

