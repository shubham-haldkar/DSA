from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self,u,v):
        if(u in self.graph):
            self.graph[u].append(v)
        else:
            self.graph[u] =[v]
    
    def depth_first_search(self,node,visited):
        visited.add(node)
        print(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.depth_first_search(neighbour,visited)

    def DFS(self,node):
        visited = set()
        self.depth_first_search(node,visited)



# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 7)
g.addEdge(3, 5)
g.addEdge(5, 3)
g.addEdge(7, 5)

print(g.graph)

g.DFS(2)

