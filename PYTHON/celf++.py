from util import (
  read_file,
  MaxHeap
)
G = read_file("../OLD/input.txt")
G.preprocess()
budget = 10
seed = set()
PQ = MaxHeap()
last_seed = None
cur_best = None
cur_val = G.N
# initialize
for i in range(G.N):
  mg1 = G.avg_dist(set([i]))
  prev_best = cur_best  
  if cur_best is not None:
    mg2 = G.avg_dist(set([i]).union(set([cur_best])))
  else:
    mg2 = mg1
  flag = 0
  PQ.update((i, mg1, prev_best, mg2, flag), G.N * G.N)
  cur_best = min(cur_best, mg1)
# update
while len(seed) < budget:
  val, dist = PQ.pop()
  u = val[0]
  mg1 = val[1]
  prev_best = val[2]
  mg2 = val[3]
  flag = val[4]
  if val[4] == len(seed):
    seed = seed.union(set([u]))
    last_seed = u
    cur_val = mg1
    continue
  elif val[2] == last_seed:
    mg1 = val[3]
  else:
    mg1 = G.avg_dist(seed)
    prev_best = cur_best
    if cur_best is not None:
      mg2 = G.avg_dist(seed.union(set([cur_best])))
    else:
      mg2 = G.avg_dist(seed)
  flag  = len(seed)
  cur_best = min(cur_best, mg1)
  PQ.update((u, mg1, prev_best, mg2, flag), cur_val - mg1)

print seed
print G.avg_dist(seed) 
