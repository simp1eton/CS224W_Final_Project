import snap
import sys

num_nodes = int(sys.argv[1])
num_edges_per_node = int(sys.argv[2])
print num_nodes
Rnd = snap.TRnd()
g = snap.GenPrefAttach(num_nodes, num_edges_per_node, Rnd)
cnt = 0
for EI in g.Edges():
  cnt = cnt + 1
print cnt
