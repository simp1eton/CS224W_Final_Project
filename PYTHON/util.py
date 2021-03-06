import numpy as np
from Queue import PriorityQueue
import Queue
import numpy as np

class Graph(object):
  def __init__(self, G):
    self.G = G
    self.N = len(G)
    self.dist = [[-1 for x in range(self.N)] for y in range(self.N)]
    self.processed = False

  def is_connected(self, i, j):
    """
      checks if i and j are connected
    """
    if i >= self.N or j >= self.N: return False
    else: return j in self.G[i]

  def preprocess(self):
    """
    Preprocess distance between points
    """
    self.processed = True
    for i in range(self.N):
      q = [i]
      self.dist[i][i] = 0
      while len(q) > 0:
        x = q.pop(0)
        for j in self.G[x]:
          if self.dist[i][j] == -1:
            self.dist[i][j] = self.dist[i][x] + 1
            q.append(j)

  def avg_dist(self, S):
    """
      outputs the average distance to the list of S nodes
    """
    if not self.processed:
      dist = [-1 for x in range(self.N)]
      for s in S: dist[s] = 0
      q = [s for s in S]
      while len(q) > 0:
        x = q.pop(0)
        for y in self.G[x]:
          if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)
      return np.mean(dist)
    else: return 1.0 * sum(min(self.dist[x][y] for y in S) for x in range(self.N)) / self.N

  def mg1_mg2(self, S, u, v):
    # return (S) - (S+u), (S+v) - (S+v+u)
    s, su, sv, suv = 0, 0, 0, 0
    for x in range(self.N):
      cur = self.N
      if len(S) > 0:
        cur = min(cur, min(self.dist[x][y] for y in S))
      s += cur
      su += min(cur, self.dist[x][u] if u is not None else self.N)
      sv += min(cur, self.dist[x][v] if v is not None else self.N)
      suv += min(cur, self.dist[x][u] if u is not None else self.N, self.dist[x][v] if v is not None else self.N)
    return 1.0 * (s - su) / self.N, 1.0 * (sv - suv) / self.N

def read_file(filename):
  """
    given a filename, returns a Graph instance of the input graph
  """
  f = open(filename, "r")
  N = int(f.readline()[:-1])
  G = [[] for y in range(N)]
  for i in range(N):
    arr = f.readline()[:-1].split()
    k = int(arr[0])
    for j in range(1,k+1):
      G[i].append(int(arr[j]))
  return Graph(G)

class MaxHeap(object):
  """
    Max Heap for the greedy algorithms
  """
  def __init__(self):
    self.popped = set()
    self.pq = PriorityQueue()

  def pop(self):
    """
      returns next item and its priority on the priority queue and removes item from the priority queue. 
      Returns (-1, 0) if queue is empty
    """
    while not self.pq.empty():
      a = self.pq.get()
      if a[1] not in self.popped:
        self.popped.add(a[1])
        return a[1], -a[0], a[2]
    return (-1, 0, None)

  def update(self, x, v, aux = None):
    """
      updates key x with value v. If x is currently not in the priority queue, x is inserted
    """
    if x in self.popped:
      self.popped.remove(x)
    self.pq.put((-v, x, aux))
    



