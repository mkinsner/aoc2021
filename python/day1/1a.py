import operator

with open('input.txt') as f:
  lines = f.readlines()

ints = list(map(int, lines))

diffs = list(map(operator.sub, ints[1:], ints[:-1]))

positives = sum(x>0 for x in diffs)
print(positives)

