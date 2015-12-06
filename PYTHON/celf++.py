from util import (
  read_file,
  MaxHeap
)
G = read_file("../OLD/blah.txt")
G.preprocess()
budget = 10
seed = set()
PQ = MaxHeap()
last_seed = None
cur_best = None
cur_val = G.N * G.N
cur_best_mg1 = cur_val

# initialize
for i in range(G.N):
  prev_best = cur_best
  mg1, mg2 = G.mg1_mg2(seed, i, cur_best)
  flag = 0
  PQ.update(i, mg1, (mg2, prev_best, flag))
  if mg1 > cur_best_mg1:
    cur_best = i
    cur_best_mg1 = mg1
  
# update
while len(seed) < budget:
  u, mg1, aux = PQ.pop()
  mg2, prev_best, flag = aux[0], aux[1], aux[2]
  if flag == len(seed):
    seed = seed.union(set([u]))
    last_seed = u
    continue
  elif prev_best == last_seed:
    mg1 = mg2
  else:
    mg1, mg2 = G.mg1_mg2(seed, u, cur_best)
    prev_best = cur_best
  flag = len(seed)
  PQ.update(u, mg1, (mg2, prev_best, flag))

print seed
print G.avg_dist(seed) 
