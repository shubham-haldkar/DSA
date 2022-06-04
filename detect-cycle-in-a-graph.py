# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

from collections import defaultdict

class Graph:
    def __init__(self ,  vertices) :
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def printGraph(self):
        for i in self.graph:
            print(i , "->" , self.graph[i])

    def isCyclic(self):
        visited = [False] * (self.V +1)
        stack = [False] * (self.V +1)
        for node in range(self.V):
            if visited[node] == False : 
                if self.isCyclicCheck(node,visited,stack):
                    return True

        return False

    def isCyclicCheck(self, v , visited , stack):
        visited[v] = True
        stack[v] = True

        for sub_node in self.graph[v]:
            if   visited[sub_node] == False :
                if self.isCyclicCheck(sub_node,visited,stack):
                    return True
            elif stack[sub_node] :
                True
        # The node needs to be popped from
        # recursion stack before function ends
        stack[v] = False
        return False






g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


g.printGraph()

print(g.isCyclic())