
class Graph:
    #Create a graph with V vertices and Construct an adjacency list
    def __init__(self, V):
        self.V = V
        self.l = [[] for _ in range(V)]
    
    #Add an edge
    def add_edge(self, u, v):
        self.l[u].append(v)
        self.l[v].append(u)
    
    #Is Cycle Detected using Depth First Search Traversal
    def is_cycle_undir_dfs(self, src, par, visited):
        visited[src] = True
        for v in self.l[src]:
            if not visited[v]:
                if self.is_cycle_undir_dfs(v, src, visited):
                    return True
            elif par != v:
                return True
        return False
    
    def is_cycle(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.is_cycle_undir_dfs(i, -1, visited):
                    return True
        return False
    
# Run the code            
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    print(g.is_cycle())
    