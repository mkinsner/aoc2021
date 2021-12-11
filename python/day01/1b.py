with open("input.txt") as f:
  lines = f.readlines()

ints = list(map(int, lines))
sums = [ints[i]+ints[i+1]+ints[i+2] for i in range(len(ints)-2)]

diffs = list(map(lambda a,b : a-b, sums[1:], sums[:-1]))

increased = sum(x>0 for x in diffs)
print(increased)
