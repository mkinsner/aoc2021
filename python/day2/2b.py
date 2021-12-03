from itertools import accumulate

with open("input.txt") as f:
  lines = f.readlines()
split_lines = [x.split() for x in lines]

horiz = list(map(lambda x: int(x[1]) if x[0][0] == 'f' else -int(x[1]) if x[0][0] == 'b' else 0, split_lines))
aim_deltas = map(lambda x: int(x[1]) if x[0][0] == 'd' else -int(x[1]) if x[0][0] == 'u' else 0, split_lines)
aim = accumulate(aim_deltas)
vert = [x*y for x,y in zip(horiz,aim)]

print(sum(horiz)*sum(vert))
