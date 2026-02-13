#### Number of Islands
In this problem, we need to find out how many components are there. Each component represents an island.
In Order to find that out:
Step 1: Consider 1 as the land and 0 as water
Step 2: For each 1, Find out the neighbors
Step 3: Apply traversal algorithm to find out the visited.
Step 4: if for a node, there are neighbors and visited node is also 1, dont increment the component. if visited node is 0, increment the component.

if using dfs:
```bash
dfs(i,j, visited[][], grid[][]){
    if (i<0 || j<0 || i>=n || j>=m || visited[i][j] || grid[i][j]!=1)
    return

    visited[i][j] = true
    dfs(i-1, j, visited, grid) -> Top
    dfs(i+1, j, visited, grid) -> Bottom
    dfs(i, j-1, visited, grid) -> Left
    dfs(i, j+1, visited, grid) -> Right
}
```
Time Complexity: O(nm)
Space Complexity: O(nm)

if using bfs:
```bash
bfs(i, j, visited[][], grid[][]){
    queue = deque([(i,j)])
    grid[i][j] = 0
    while queue:
        x, y = queue.popleft()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and grid[nx][ny]=='1':
                grid[nx][ny] = '0'
                queue.append((nx, ny))
}
```
Time Complexity: O(nm)
Space Complexity: O(nm)

#### Rotten Oranges
If a cell contains 0, then its an empty cell, if it contains 1, its a fresh cell and if it contains 2, its a rotten cell.
If a rotten orange shares an edge with fresh orange, the fresh oranges become rotten. the idea is to calculate time period for making each fresh orange rotten.
If an orange stays fresh after all the iterations, then the total time period is -1 and if there are no fresh oranges, then the time period is 0.

Step1: Start with the node with value 2, check its edges. possible edges will be up, down, left and right
Step2: if edge contains 1, make it rot and check its neighbours, if neighbors contain 1, make it rotten.
Step3: until possible edges are 0 or all the edges visited, continue the loop
Step4: add time for each node or traversal

Edge case: there can also be multiple rotten oranges. so the time will change based on the multiple sources. if multiple sources are used. 
Intution, if graph is disconnected, then it will always return -1 because one or more orranges remain fresh.
looks like bfs traversal but there need to be multiple source to start with, since starting point can be taken from any where. and less recursion is better

if using multi-source bfs:
```bash
queue = deque([(i,j,0)])

for i in range(n):
    for j in range(m):
        if grid[i][j]==2:
            q.append((i,j))

while queue:
    i,j, time = queue.popleft()
    ans = max(ans, time)
    
    if i-1>=0 and not visited[i-1][j] and grid[i-1][j]==1:
        queue.append((i-1, j, time+1))
        visited[i-1][j] = True
    if i+1<n and not visited[i+1][j] and grid[i+1][j]==1:
        queue.append((i+1, j, time+1))
        visited[i+1][j] = True
    if j-1>=0 and not visited[i][j-1] and grid[i][j-1]==1:
        queue.append((i, j-1, time+1))
        visited[i][j-1] = True
    if j+1<m and not visited[i][j+1] and grid[i][j+1]==1:
        queue.append((i, j+1, time+1))
        visited[i][j+1] = True
```
Time Complexity: O(nm)
Space Complexity: O(nm)

#### Clone Graph - Leetcode 133
We need to clone the graph, without actually returning the same graph. It needs to be a deep copy. it cannot be a simple or shallow copy of a graph.
When we try to copy a from original graph, we will encounter 2 issues:
1. Infinite Loop : A -> B and B -> A, then again A -> B and B -> A
2. Maintaining correct references: cloned nodes need to be pointing to other cloned nodes not the original nodes.

Solution:
using dfs with hash table.
```bash
dfs(current_node)
if current_node is None:
    return None
if current_node in visited_to_cloned:
    return visited_to_cloned[current_node]

cloned_node = Node(current_node.val)

visited_to_cloned[current_node] = cloned_node

for neighbor in current_node.neighbors:
    cloned_node.neighbors.append(dfs(neighbor))

return cloned_node
```
Time Complexity: O(n)
Space Complexity: O(n)