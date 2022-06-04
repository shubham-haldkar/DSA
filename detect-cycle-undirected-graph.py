# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
# Detect cycle in an undirected graph


from collections import defaultdict


class Graph:
    def __init__(self,vertices) :
        self.V = vertices
        self.graph  = defaultdict(list)

    def addEdge(self,v,u):
        self.graph[v].append(u)
        self.graph[u].append(v) # since it is undirected graph so u points to v and v points to u

    def isCyclic(self)  :
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if(self.isCyclicCheck(i,visited,-1) ):
                    return True

        return False
    
    def isCyclicCheck(self, v, visited , parent ):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if(self.isCyclicCheck(i,visited, v) ):
                    return True
            elif parent!=i:
                return True

        return False






g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
if g.isCyclic():
    print ("Graph contains cycle")
else :
    print ("Graph does not contain cycle ")


g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
 
 
if g1.isCyclic():
    print ("Graph contains cycle")
else :
    print ("Graph does not contain cycle ")