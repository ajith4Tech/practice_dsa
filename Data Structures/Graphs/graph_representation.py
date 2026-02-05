
class Graph:
    #Create a graph with V vertices and Construct an adjacency list
    def __init__(self, V):
        self.V = V
        self.l = [[] for _ in range(V)]
    
    #Add an edge
    def add_edge(self, u, v):
        self.l[u].append(v)
        self.l[v].append(u)
    
    #Print the graph
    def print_graph(self):
        for i in range(self.V):
            print(f"{i} : ", end="")
            for neigh in self.l[i]:
                print(f"{neigh} ", end="")
            print()
# Run the code            
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.print_graph()
    