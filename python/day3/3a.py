import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

chars = [list(x.strip()) for x in lines]
ints = np.array(chars, dtype=int)

gamma_arr = np.median(ints, axis=0).astype(int)
epsilon_arr = (gamma_arr+1)%2

gamma = int(np.array2string(gamma_arr)[1:-1].replace(" ",""), base=2)
epsilon = int(np.array2string(epsilon_arr)[1:-1].replace(" ",""), base=2)

print(gamma*epsilon)

