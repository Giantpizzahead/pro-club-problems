import math
def distance(c, c1):
  # Uses the distance formula. √((x1-x2)^2+(y1-y2)^2)
  return math.sqrt((int(c[0])-int(c1[0]))**2 + (int(c[1])-int(c1[1]))**2)
N = int(input())
cows = []
# N is how many cows to expect, so we stop looking afterward.
for i in range(0, N):
  # At the end, format is [x, y, D]
  cows.append(input().split())
smallestDistance = 10001
testCows = []
for cow1 in cows:
  for cow2 in cows:
    # the distance between a cow and itself is always 0.
    if cow1 == cow2:
      continue
    difference = distance(cow1, cow2)
    if difference <= smallestDistance:
      smallestDistance = difference
      testCows.append(cow1)
      testCows.append(cow2)
isolateThisCow = None
bestDistance = 0
for cow in testCows:
  D = 10001
  for cow1 in cows:
    if cow1 == cow:
      continue
    for cow2 in cows:
      if cow2 == cow or cow1 == cow2:
        continue
      separation = distance(cow1, cow2)
      if separation < D:
        D = separation
  cow.append(D)
  if D > bestDistance:
    bestDistance = D
    isolateThisCow = cow
print(cows.index(isolateThisCow)+1)