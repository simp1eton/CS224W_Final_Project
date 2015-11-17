import random 
from random import randint
import sys
num_nodes = int(sys.argv[1])
num_partition = float(sys.argv[2])
intra_prop = float(sys.argv[3])
inter_prop = float(sys.argv[4])
ans = []
for i  in range(num_nodes):
  ans.append([])
for i in range(num_nodes):
  for j in range(i + 1, num_nodes):
    first = i % num_partition
    second = j % num_partition
    rad = random.random()
    if first == second:
      if rad < intra_prop:
        if j not in ans[i]:
	  ans[i].append(j)
        if i not in ans[j]:
          ans[j].append(i)
    else:
      if rad < inter_prop:
        if j not in ans[i]:
          ans[i].append(j)
        if i not in ans[j]:
          ans[j].append(i)

for i in range(num_nodes):
  res =  str(len(ans[i])) + " "
  for v in ans[i]:
    res  = res + " " + str(v)
  print res

