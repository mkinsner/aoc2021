import numpy as np
import string as s

with open("input.txt") as f:
  lines = f.readlines()

chars = [list(x.strip()) for x in lines]
oxy_arr = np.array(chars, dtype=int)
co2_arr = np.copy(oxy_arr)
num_cols = len(chars[0])

for i in range(num_cols):
  keep_val = int(np.median(oxy_arr[:,i]) + 0.5)  # +0.5 to round.  round() is to even
  keep_rows = oxy_arr[:,i] == keep_val
  oxy_arr = oxy_arr[keep_rows,:]
  if (oxy_arr.shape[0] < 2):
    break

for i in range(num_cols):
  keep_val = (int(np.median(co2_arr[:,i])+0.5)+1)%2  # +1 to invert, +.5 to round
  keep_rows = co2_arr[:,i] == keep_val
  co2_arr = co2_arr[keep_rows,:]
  if (co2_arr.shape[0] < 2):
    break

oxy = int(np.array2string(oxy_arr)[2:-2].replace(" ",""), base=2)
co2 = int(np.array2string(co2_arr)[2:-2].replace(" ",""), base=2)

print(oxy*co2)
