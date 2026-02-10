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
`````
Time Complexity: O(nm)
Space Complexity: O(nm)
