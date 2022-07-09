import itertools

cr = .0789
cd = .0789
em = .1053
hp = .1053

occurance = 0.0

for a, b, c, d in itertools.permutations((cr, cd, em, hp), 4):
  step = a * (b/(1-a)) * (c/(1-a-b)) * (d/(1-a-b-c))
  occurance += step
  print("step: " + str(step))

print("probability to get this artifact: " + str(occurance))
print("number of artifacts to get:" + str(1/occurance))