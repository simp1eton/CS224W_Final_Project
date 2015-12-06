import snap
import sys
num_nodes = 1000
num_edges = 5000
Rnd = snap.TRnd(0)
print num_nodes
g_original = snap.GenRndGnm(snap.PUNGraph, num_nodes, num_edges,
        False, Rnd)
g = snap.GenConfModel(g_original)
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
