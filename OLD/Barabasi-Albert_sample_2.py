import snap
import sys

num_nodes = int(sys.argv[1])
num_edges_per_node = int(sys.argv[2])
print num_nodes
Rnd = snap.TRnd()
g = snap.GenPrefAttach(num_nodes, num_edges_per_node, Rnd)
adj_list = []
for i in range(num_nodes):
  adj_list.append([])
for EI in g.Edges():
  source = EI.GetSrcNId()
  sink = EI.GetDstNId()
  if sink not in adj_list[source]:
    adj_list[source].append(sink)
for i in range(num_nodes):
  ans =  str(len(adj_list[i])) + " " 
  for v in adj_list[i]:
    ans  = ans + " " + str(v)
  print ans
