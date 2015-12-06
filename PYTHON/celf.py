from util import (
  read_file,
  MaxHeap
)

G = read_file("blah.txt")
G.preprocess()
PQ = MaxHeap()

for i in range(G.N):
  PQ.update(i, G.N * G.N)

S = set()
cur_val = G.N * G.N

budget = 20

for _ in range(budget):
  while True:
    cur, val, aux = PQ.pop()
    new_val = G.avg_dist(S.union(set([cur]))) 
    if cur_val - new_val == val:
      S.add(cur)
      cur_val = new_val
      break
    PQ.update(cur, cur_val - new_val)

print S
print G.avg_dist(S)
