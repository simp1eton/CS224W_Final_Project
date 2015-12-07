import random 
from random import randint
import sys
#4000 4 0.005 0.0025
num_nodes = 1000
num_partition = 4
print num_nodes
intra_prop = 0.01
inter_prop = 0.01
ans = []
cnt = 0
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
          cnt = cnt + 1
	  ans[i].append(j)
        if i not in ans[j]:
          ans[j].append(i)
    else:
      if rad < inter_prop:
        if j not in ans[i]:
          cnt = cnt + 1
          ans[i].append(j)
        if i not in ans[j]:
          ans[j].append(i)
for i in range(num_nodes):
  res =  str(len(ans[i])) + " "
  for v in ans[i]:
    res  = res + " " + str(v)
  print res
