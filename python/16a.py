with open("input.txt") as f:
  lines = f.readlines()

B = bytearray.fromhex(lines[0].strip())
b = ''.join(format(i, '08b') for i in B)

version_sum=0

def parse_packet(b):
  global version_sum
  version = b[0:3]
  typeID = b[3:6]
  version_sum += int(version, 2)

  if (int(typeID,2) == 4): # Literal value packet
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
    return b[6+i*5:]
      
  else: # Operator packet
    if b[6:7] == '0':  # Next 15b are total length
      temp_b = b[7:7+15]
      tot_len = int(''.join(temp_b), 2)
      print("Total length:", tot_len)
      ret = parse_packet(b[22:22+tot_len])
      while ret:
        ret = parse_packet(ret)
      return b[22+tot_len:]

    else:  # Next 11b are num sub-packets
      temp_b = b[7:7+11]
      num_sub = int(''.join(temp_b), 2)
      print("Number sub-packets:", num_sub)
      ret = b[18:]
      for p in range(num_sub):
        print("Calling sub-packet iteration:", p)
        ret = parse_packet(ret)
      return ret 
    
parse_packet(b)
print("Sum of version numbers:", version_sum)
