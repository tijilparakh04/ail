import networkx as nx
import csv
import itertools

class graphBFS:
  def __init__(self):
    self.visual = []

  def add_edge(self, a, b):
    temp = [a,b]
    self.visual.append(temp)

  def bfs(self, start):
    visited = set()
    queue = [start]
    visited.add(start)
    traversal_order = []
    traversal_order.append(start)
    grp = nx.Graph()
    grp.add_edges_from(self.visual)

    while queue:
      vertex = queue.pop(0)
      for neighbors in grp[vertex]:
        if neighbors not in visited:
          visited.add(neighbors)
          traversal_order.append(neighbors)
          queue.append(neighbors)
      
    return traversal_order

def load_from_csv(filename, graphobject):
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      graphobject.add_edge(row[0], row[1])

G = graphBFS()
load_from_csv('graph_example.csv', G)

bfs_order = G.bfs('Delhi')
print(bfs_order)