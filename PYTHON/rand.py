from util import read_file
import random
import time

budget = 21
G = read_file("input.txt")
G.preprocess()
for i in range(1,budget):
  start_nodes = random.sample(range(G.N), i)
  res = G.avg_dist(start_nodes)
  print res
