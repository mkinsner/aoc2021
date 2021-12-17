import time
import numpy as np

with open("input.txt") as f:
  lines = f.readlines()

S = lines.pop(0).strip()
lines.pop(0)
print(S)

rules = {}
for r in lines:
  s = r.strip().split(" -> ")
  rules[s[0]] = s[1]

t = time.process_time()

# For each rule, build out 20 iterations
iterated_rules = {}
for rule in rules.keys():
  E = rule
  print(E)
  for step in range(20):
    E = E[0] + "".join(list(map(lambda x,y: rules[x+y] + y, E[0:-1], E[1:])))
    iterated_rules[rule] = E
print ("Time to expand 20 iterations of each rule: ", time.process_time()  - t)

# Find all unique characters that need to be in histogram
chars = set()
for v in iterated_rules.values():
  chars.update(v)
hist_indices = {}
i=0
for c in chars:
  hist_indices[c] = i
  i += 1
num_bins = len(hist_indices)

# Create histogram vector for each 20-level expanded seed pair
# Don't count first character
iterated_histogram = {}
for key,val in iterated_rules.items():
  H = np.zeros(num_bins)
  for c,i in hist_indices.items():
    H[i] = val[1:].count(c)
  iterated_histogram[key] = H
print ("Time to histogram each 20-iterated rule: ", time.process_time()  - t)

final_histogram = np.zeros(num_bins)
final_histogram[hist_indices[iterated_rules[S[0:2]][0]]] += 1 #Iterated histograms omit first char to avoid doudle count
for i in range(len(S)-1):
  print(i)
  seed_pair = S[i:i+2]
  hip = iterated_rules[seed_pair]  # Half iterated pair
  for j in range(len(hip)-1):
    final_histogram += iterated_histogram[hip[j:j+2]]
print ("Time to sum 40-deep histograms:", time.process_time()  - t)

print(max(final_histogram) - min(final_histogram))
