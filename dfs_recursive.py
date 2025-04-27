import networkx as nx
import csv

class GraphDFS:
  def __init__(self):
    self.visual = []

  def add_edge(self, a,b):
    temp = [a,b]
    self.visual.append(temp)
  
  def dfs(self, start):
    visited = set()
    traversal_order = []

    grp = nx.Graph()
    grp.add_edges_from(self.visual)

    def dfs_recursive(node):
      if node not in visited:
        visited.add(node)
        traversal_order.append(node)
        for neighbor in grp[node]:
          dfs_recursive(neighbor)

    dfs_recursive(start)
    return traversal_order
      
def load_from_csv(filename, graphobject):
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:    
      graphobject.add_edge(row[0], row[1])
G = GraphDFS()
load_from_csv('graph_example.csv', G)

dfs_order = G.dfs('Delhi')
print(dfs_order)