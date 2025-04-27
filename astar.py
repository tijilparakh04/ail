import csv
import heapq
import networkx as nx

class Astar:
  def __init__(self):
    self.visual = []
    self.graph = {}
    self.heuristic = {}

  def add_edge(self, a,b,c):
    temp = [a,b,c]
    self.visual.append(temp)
    self.graph.setdefault(a, []).append((b, c))

  def set_heuristic(self, heuristic_dict):
    self.heuristic = heuristic_dict

  def astar(self, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node:float('inf') for node in self.graph}
    g_score[start] = 0
    f_score = {node:float('inf') for node in self.graph}
    f_score[start] = self.heuristic.get(start, float('inf'))

    while open_set:
      _, current = heapq.heappop(open_set)

      if current == goal:
        path = []
        while current in came_from:
          path.append(current)
          current = came_from[current]
        path.append(start)
        return path[::-1], g_score[goal]

      for neighbor, cost in self.graph.get(current, []):
        tentative_g = g_score[current] + cost
        if tentative_g<g_score[neighbor]:
          came_from[neighbor] = current
          g_score[neighbor] = tentative_g
          f_score[neighbor] = tentative_g + self.heuristic.get(neighbor, float('inf'))
          heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None, float('inf')

  def visualize_graph(self, path):
        G = nx.DiGraph()
        for src, dest, cost in self.visual:
            G.add_edge(src, dest, weight=cost)

        pos = nx.spring_layout(G)
        edge_labels = {(src, dest): cost for src, dest, cost in self.visual}

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        if path:
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        plt.title("Graph Visualization with A* Optimal Path")
        plt.show()


def load_graph_from_csv(filename, graph_object):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            src, dest, cost = row[0], row[1], float(row[2])
            graph_object.add_edge(src, dest, cost)

def load_heuristic_from_csv(filename):
    heuristic = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            node, h_value = row[0], float(row[1])
            heuristic[node] = h_value
    return heuristic


if __name__ == "__main__":
    G = Astar()
    load_graph_from_csv('graph_example4.csv', G)
    heuristic = load_heuristic_from_csv('heuristic.csv')
    G.set_heuristic(heuristic)

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    path, cost = G.astar(start, goal)

    if path:
        print(f"Optimal Path: {' -> '.join(path)} with cost {cost}")
    else:
        print("No optimal path found.")

    G.visualize_graph(path)
