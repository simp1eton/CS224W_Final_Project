from util import (
  read_file,
  MaxHeap
)
import time

G = read_file("input.txt")
G.preprocess()
PQ = MaxHeap()

for i in range(G.N):
  PQ.update(i, G.N * G.N)

S = set()
cur_val = G.N

budget = 20

start_time = time.time()
for _ in range(budget):
  while True:
    cur, val = PQ.pop()
    new_val = G.avg_dist(S.union(set([cur]))) 
    if cur_val - new_val == val:
      S.add(cur)
      cur_val = new_val
      break
    PQ.update(cur, cur_val - new_val)
  end_time = time.time()
  #print S
  print end_time - start_time, G.avg_dist(S)
