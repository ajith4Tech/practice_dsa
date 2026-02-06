## Graph Algorithms

### Traversal
    BFS Traversal
    DFS Traversal

#### BFS Traversal
    Travel the immediate neighbor first
    Time Complexity : O(Vertices+Edges)
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
#### DFS Traversal
    Keep going to the first unvisited neighbor
    Recursive Traversal - Uses Backtracking
    Time Complexity : O(Vertices+Edges)
```bash
dfs(v, vector<bool>&vis){
print(u)
vis[u] = true
for (v:l[u]) {
if(!vis[v]){
dfs(v, vis)
}
}
}
```
Note: For any disconnected graph, check the vertices length and then call the nexessary traversal algorithm