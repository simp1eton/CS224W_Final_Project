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
cur_val = G.N * G.N

INIT_VAL = G.N * G.N

# initialize
for i in range(G.N):
  mg1 = G.avg_dist(set([i]))
  prev_best = cur_best  
  if cur_best is not None:
    mg2 = G.avg_dist(set([i]).union(set([cur_best])))
  else:
    mg2 = mg1
  flag = 0
  PQ.update((i, mg1, prev_best, mg2, flag), mg1)
  if mg1 < cur_val:
    cur_val = mg1
    cur_best = i 

# update
while len(seed) < budget:
  val, dist = PQ.pop()
  u = val[0]
  mg1 = val[1]
  prev_best = val[2]
  mg2 = val[3]
  flag = val[4]
  if flag == len(seed):
    seed = seed.union(set([u]))
    last_seed = u
    if cur_val != mg1:
      print "ouch",u, len(seed) 
    continue
  elif prev_best == last_seed:
    mg1 = mg2
  else:
    withU = seed | set([u])
    mg1 = G.avg_dist(seed) - G.avg_dist(withU)
    prev_best = cur_best
    withU2 = seed | set([u]) | set([cur_best])
    withoutU = seed | set([cur_best])
    print withoutU
    mg2 = G.avg_dist(withoutU) - G.avg_dist(withU2)
  flag  = len(seed)
  if mg1 < cur_val:
    cur_val = mg1
    cur_best = u
 #   print "current best:", cur_best, "u:", u
#  cur_best = min(cur_best, mg1)
  PQ.update((u, mg1, prev_best, mg2, flag), mg1)

print seed
print G.avg_dist(seed) 
