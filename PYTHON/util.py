import numpy as np
from Queue import PriorityQueue

class Graph(object):
  def __init__(self, G):
    self.G = G
    self.N = len(G)

  def is_connected(i, j):
    """
      checks if i and j are connected
    """
    if i >= N or j >= N: return False
    else: return j in G[i]

  def max_dist(S):
    """
      given a list of nodes S, outputs the maximum distance of a node from S
    """
    pass


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
    self.popped = {}
    self.pq = PriorityQueue()

  def pop():
    """
      returns next item on the priority queue. Returns -1 if queue is empty
    """
    while not self.pq.empty():
      a = self.pq.get()
      if a[1] not in self.popped:
        self.popped[a[1]] = 1
        return a[1]
    return -1

  def update(x, v):
    """
      updates key x with value v. If x is currently not in the priority queue, x is inserted
    """
    if x in self.popped:
      del self.popped[x]
    self.pq.put((-v, x))
    



