with open("input.txt") as f:
  lines = f.readlines()
split_lines = [x.split() for x in lines]

horiz = map(lambda x: int(x[1]) if x[0][0] == 'f' else -int(x[1]) if x[0][0] == 'b' else 0, split_lines)
vert = map(lambda x: int(x[1]) if x[0][0] == 'd' else -int(x[1]) if x[0][0] == 'u' else 0, split_lines)

print(sum(horiz)*sum(vert))
