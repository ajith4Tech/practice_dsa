## Graph Definition

Graph → It is a network of nodes (vertices) connected by edges.

### Example:

    Any Map-based application uses graph data structure

    Implementation of Neural networks is also based on graphs

### Types of Graphs
#### Based on Edges

    Unidirectional Graph (Directed Graph)
        Edges have direction at the end of the edge
    Ex: Address (one-way streets)

    Undirected / Bi-directed Graph
        Edges have no specific direction (bidirectional)

#### Based on Edge-Weight

    Weighted Graph
        Edges have weights/costs associated

    Unweighted Graph
        Edges have no weights

#### Other Types

    Disconnected Graph
        Graph with unreachable vertices

### Graph Representation
    Adjacency List
        Most space-efficient representation
        Store vertices as index and their neighbor details as values
        Structure: vertex → [neighbor1, neighbor2, ...]
    
        Example:
        0 → [1, 2]
        1 → [0, 3] 
        2 → [0, 4]
        3 → [1]
        4 → [2]
