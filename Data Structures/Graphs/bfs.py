
class Graph:
    #Create a graph with V vertices and Construct an adjacency list
    def __init__(self, V):
        self.V = V
        self.l = [[] for _ in range(V)]
    
    #Add an edge
    def add_edge(self, u, v):
        self.l[u].append(v)
        self.l[v].append(u)
    
    #Breadth First Search Traversal
    def bfs(self):
        queue = []
        visited = [False] * self.V
        queue.append(1)
        visited[1] = True
        print("BFS Traversal: ", end="")
        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            for v in self.l[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        print()

    
# Run the code            
if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.bfs()
    
    