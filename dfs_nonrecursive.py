import networkx as nx
import matplotlib.pyplot as plt
import csv

class GraphDFS:
  def __init__(self):
    self.visual = []
  
  def add_edge(self, a,b):
    temp = [a,b]
    self.visual.append(temp)

  def dfs(self, start):
    visited = set()
    traversal_order=[]
    stack = [start]

    grp = nx.Graph()
    grp.add_edges_from(self.visual)

    while stack:
      vertex = stack.pop()
      if vertex not in visited:
        visited.add(vertex)
        traversal_order.append(vertex)
        stack.extend([neighbor for neighbor in grp[vertex] if neighbor not in visited])
      
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