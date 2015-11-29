import snap
import sys
num_nodes = int(sys.argv[1])
forward_prob = float(sys.argv[2])
backward_prob = float(sys.argv[3])
g = snap.GenForestFire(num_nodes, forward_prob,backward_prob)
print num_nodes
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
