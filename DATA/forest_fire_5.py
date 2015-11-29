import snap
import sys
import math
#  4000 0.34 0.35
num_nodes = 4000 
forward_prob = 0.349
backward_prob = 0.34
g = snap.GenForestFire(num_nodes, forward_prob,backward_prob)
print num_nodes

cnt = 0
for EI in g.Edges():
  cnt = cnt + 1
if abs(cnt - 24000) > 200:
  sys.exit("Edges number wrong!")
adj_list = []
for i in range(num_nodes):
  adj_list.append([])
for EI in g.Edges():
  source = EI.GetSrcNId()
  sink = EI.GetDstNId()
  if sink not in adj_list[source]:
    adj_list[source].append(sink)
  if source not in adj_list[sink]:
    adj_list[sink].append(source)
for i in range(num_nodes):
  ans =  str(len(adj_list[i])) + " " 
  for v in adj_list[i]:
    ans  = ans + " " + str(v)
  print ans
print "number of edges : " , cnt
