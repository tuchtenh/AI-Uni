graph = [None]*5

class Knoten:

  def __init__(self, key, kids):
    self.key = key
    self.kids = kids
    while key > len(graph):
      Knoten.bigger_graph()
    graph[key] = kids

  def add_Kinder(self, k):
    if isinstance(k, list):
      for i in k:
        self.kids.append(i)
    else:
        self.kids.append(k)
    graph[self.key] = None
    graph[self.key] = self.kids

  @staticmethod
  def bigger_graph():
    for i in range (0, 5):
      graph.append(None)

  @staticmethod
  def print_graph():
    print(graph)


k3 = Knoten(3, [])
k2 = Knoten(2, [])
k1 = Knoten(1, [k2, k3])
k3.add_Kinder([k1, k2])
k2.add_Kinder(k1)


Knoten.print_graph()

