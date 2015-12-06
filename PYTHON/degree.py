from util import (
  read_file,
  MaxHeap
)
import time

G = read_file("blah.txt")
G.preprocess()
PQ = MaxHeap()

for i in range(G.N):
  PQ.update(i, G.N * G.N)

S = set()
cur_val = G.N * G.N

budget = 20

used = set()

start_time = time.time()
for _ in range(budget):
  while True:
    cur, val, aux = PQ.pop()
    if cur == -1: break
    if cur in used: continue
    new_val = G.avg_dist(S.union(set([cur]))) 
    if cur_val - new_val == val:
      S.add(cur)
      cur_val = new_val
      used.add(cur)
      for y in G.G[cur]: used.add(y)
      break
    PQ.update(cur, cur_val - new_val)
  end_time = time.time()
  #print S
  print end_time - start_time, cur_val
