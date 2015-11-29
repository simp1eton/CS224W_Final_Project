import numpy as np
from Queue import PriorityQueue

def read_file(filename):
  """
    given a filename, returns the (0-indexed) graph stored in the file as an adjacency list
  """
  f = open(filename, "r")
  N = int(f.readline()[:-1])
  G = [[] for y in range(N)]
  for i in range(N):
    arr = f.readline()[:-1].split()
    k = int(arr[0])
    for j in range(1,k+1):
      G[i].append(int(arr[j]))
  return G


class PQ(object):
  """
    Priority queue used for the greedy algorithms
  """
  def __init__(self, G):

  def pop():

  def insert():
    
    
