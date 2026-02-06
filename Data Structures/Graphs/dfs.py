
class Graph:
    #Create a graph with V vertices and Construct an adjacency list
    def __init__(self, V):
        self.V = V
        self.l = [[] for _ in range(V)]
    
    #Add an edge
    def add_edge(self, u, v):
        self.l[u].append(v)
        self.l[v].append(u)
    
    #Depth First Search Traversal
    def dfs(self, u, visited):
        print(u, end=" ")
        visited[u] = True
        for v in self.l[u]:
            if not visited[v]:
                self.dfs(v, visited)
    #Traverse the graph
    def dfs_util(self):
        src = 0
        visited = [False] * self.V
        self.dfs(src, visited)
        print()
        
    
# Run the code            
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.dfs_util()
    
    