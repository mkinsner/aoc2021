import numpy as np

with open("input.txt") as f:
  lines = f.readlines()
lines = [l.strip().split(" | ") for l in lines]

result = 0
for line in lines:
  input_line = line[0].split(" ")
  output_line = line[1].split(" ")
  line_set = [set(i) for i in input_line]
  set_len = [len(i) for i in line_set]
  
  # Find "1" (len 2)
  cf = line_set[set_len.index(2)]

  # Find seg a from "7" (len 3)
  a = line_set[set_len.index(3)] - cf

  # Find seg bd from "4" (len 4)
  bd = line_set[set_len.index(4)] - cf

  # Find dg from "3".  len 5 and contains cf and a
  for i in range(len(line_set)):
    if set_len[i] == 5 and (cf|a).issubset(line_set[i]): dg = line_set[i] - cf - a 

  # Find b from "0".  len 6 and contains a,cf,dg
  for i in range(len(line_set)):
    if set_len[i] == 6 and (a|cf|dg).issubset(line_set[i]): b = line_set[i] - a - cf - dg
    
  d = bd - b
  g = dg - d

  # Find f from "5".  len 5 and contains a,b,d,g
  for i in range(len(line_set)):
    if set_len[i] == 5 and (a|b|d|g).issubset(line_set[i]): f = line_set[i] - a - b - d - g
    
  c = cf - f

  # Find e from "8"
  e = line_set[set_len.index(7)] - a-b-c-d-f-g

  chars = [a|b|c|e|f|g, c|f, a|c|d|e|g, a|c|d|f|g, b|c|d|f, a|b|d|f|g, a|b|d|e|f|g, a|c|f, a|b|c|d|e|f|g, a|b|c|d|f|g]
  output_nums = [chars.index(set(d)) for d in output_line]
  this_output = int("".join(map(str,output_nums)))
  result += this_output

print(result)
