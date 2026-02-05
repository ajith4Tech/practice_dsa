## Graph Algorithms

### Traversal
    BFS Traversal
    DFS Traversal

#### BFS Traversal
    Travel the immediate neighbor first
```bash
while (Q.size() > 0) {
int u = Q.pop()
print(u)
for(all neigh of u){
if (!visited(v)){
visited[v] = true
Q.push(v)
}
}
}
```