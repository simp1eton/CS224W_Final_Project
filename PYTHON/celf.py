from util import (
  read_file,
  MaxHeap
)

G = read_file("../OLD/input.txt")

PQ = MaxHeap()

for i in range(G.N):
  PQ.update(i, float("+inf"))

for B in range(10):
  print B 
