import functools
import operator

with open("input.txt") as f:
  lines = f.readlines()

B = bytearray.fromhex(lines[0].strip())
b = ''.join(format(i, '08b') for i in B)

version_sum=0

def reduce(op, operands):
  if op == 0:
    f = operator.add
  elif op == 1:
    f = operator.mul
  elif op == 2:
    f = min
  elif op == 3:
    f = max
  elif op == 5:
    f = operator.gt
  elif op == 6:
    f = operator.lt
  elif op == 7:
    f = operator.eq

  if op < 4:
    return functools.reduce(f, operands)
  else:
    return int(functools.reduce(f, operands))
  

def parse_packet(b):
  global version_sum
  version = b[0:3]
  typeID = b[3:6]
  version_sum += int(version, 2)

  op = int(typeID,2)
  if op == 4: # Literal value packet
    i = 0
    temp_b = []
    while True:
      five_b = b[6+i*5 : 6+i*5+5]
      i += 1
      temp_b += five_b[1:6]
      if five_b[0] == '0':
        break # Terminating quad
    literal_val = int(''.join(temp_b), 2)
    print("Literal value:", literal_val)
    return literal_val, b[6+i*5:]
      
  else: # Operator packet
    operands = []
    if b[6:7] == '0':  # Next 15b are total length
      temp_b = b[7:7+15]
      tot_len = int(''.join(temp_b), 2)
      print("Total length:", tot_len)
      val, ret = parse_packet(b[22:22+tot_len])
      operands.append(val)
      while ret:
        val, ret = parse_packet(ret)
        operands.append(val)
      print(int(typeID,2),operands)
      return reduce(op, operands), b[22+tot_len:]

    else:  # Next 11b are num sub-packets
      temp_b = b[7:7+11]
      num_sub = int(''.join(temp_b), 2)
      print("Number sub-packets:", num_sub)
      ret = b[18:]
      for p in range(num_sub):
        val, ret = parse_packet(ret)
        operands.append(val)
      print(int(typeID,2),operands)
      return reduce(op, operands),ret 
    
answer, r = parse_packet(b)
print("Answer:", answer)
