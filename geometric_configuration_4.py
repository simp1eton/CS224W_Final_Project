import snap
import sys
num_nodes = int(sys.argv[1])
num_edges_per_node = int(sys.argv[2])
beta = float(sys.argv[3])
Rnd = snap.TRnd()
g = snap.GenGeoPrefAttach(num_nodes, num_edges_per_node, beta, Rnd)
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
