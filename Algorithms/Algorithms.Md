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

#### Cycle Detection
    - Exists both in directed and undirected graphs
    - In Undirected Graphs, We can use DFS, BFS and Disjoint Set Union to detect cycles.
    - In Directed Graphs, We can use DFS, BFS and Kahn;s Algorithm to detect cycles.
    - Usage of DFS because its simpler
    - Back Edge case: Where `u` connects to ancestor `v` which detects a cycle or loop.

#### Cycle Detection using DFS
```bash
dfs(src, visit[], par) {
visit[src] = true;
for (v:l[u]) {
if (!visit[v]) {
if (dfs(v, visit)) {
return true
}
}
else if (v!=par){
return true
}
}
return false
}
```

#### Cycle Detection using BFS
```bash
bfs(src, visit[]) {
queue Q[][]
Q.push(src, -1)
visit[src] = true
while Q.size > 0 {
u, par = Q.pop()
for v:l[u]{
if(!visit[v]){
Q.push(v)
vis[v] = true
}
else if(v!=par){
return true
}
return false
}
}
```

