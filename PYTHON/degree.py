from util import (
  read_file,
  MaxHeap
)
import time
import numpy
import sys

budget = 20
graph_type = int(sys.argv[1])

stats = [[] for _ in range(budget)]
ans = [[] for _ in range(budget)]

for i in range(1, 51):
    filename = "../DATA/mass_data/input" + `graph_type` + "-" + `i` + ".txt"
    G = read_file(filename)
    start_time = time.time()
    G.preprocess()
    PQ = MaxHeap()

    for i in range(G.N):
      PQ.update(i, G.N * G.N)

    S = set()
    cur_val = G.N * G.N

    used = set()

    for curr_budget in range(budget):
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
      total_time = end_time - start_time
      avg_dist = cur_val
      #print S
      print total_time, avg_dist
      stats[curr_budget].append(total_time)
      ans[curr_budget].append(avg_dist)


print '=' * 50
for i in range(budget):
    stats_list = stats[i]
    ans_list = ans[i]
    stats_std = numpy.std(stats_list)
    stats_mean = numpy.mean(stats_list)
    ans_std = numpy.std(ans_list)
    ans_mean = numpy.mean(ans_list)
    print stats_mean, stats_std, ans_mean, ans_std

