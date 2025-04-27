from queue import PriorityQueue
from xml.etree.ElementTree import ProcessingInstruction
import networkx as nx
import csv

class GraphBFS():
  def __init__(self):
    self.visual = []
    self.graph = {}

  def add_edge(self, a,b, c):
    temp = [a,b,c]
    self.visual.append(temp)
    self.graph.setdefault(a, []).append(b)
 
  def cost(self, city1, city2):
      for edge in self.visual:
            if edge[0] == city1 and edge[1] == city2:
                return edge[2]
      return 9999

  def bfs(self, start, goal):
    visited = set()
    traversal_order = []
    parent = {}

    queue = PriorityQueue()
    queue.put((0, start))
    visited.add(start)

    while queue:
      curr_cost, vertex = queue.get()
      traversal_order.append(vertex)

      if vertex == goal:
        break
      
      for neighbor in self.graph.get(vertex, []):
        if neighbor not in visited:
          visited.add(neighbor)
          parent[neighbor] = vertex
          cost_to_goal = self.cost(neighbor, goal)
          queue.put((cost_to_goal, neighbor))

    return traversal_order, parent


def load_graph_from_csv(filename, graph_object):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            try:
                source, target, weight = row
                graph_object.add_edge(source, target, int(weight))
            except ValueError:
                print(f"Skipping invalid row: {row}")


G = GraphBFS()
load_graph_from_csv('graph_example2.csv', G)

start_node = input("Enter the source node: ")
goal_node = input("Enter the goal node: ")

bfs_order = G.bfs(start_node, goal_node)
print("BFS Traversal Order:", bfs_order)
