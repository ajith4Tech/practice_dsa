#Number of Islands Leetcode Problem 200
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''
from typing import List
from collections import deque

class Graph:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i, j, visited, grid, m, n)
                    islands += 1   
        return islands 
    #DFS approach
    def dfs(self, i, j, visited, grid, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] != '1':
            return
        visited[i][j] = True
        self.dfs(i-1, j, visited, grid, m, n)
        self.dfs(i+1, j, visited, grid, m, n)
        self.dfs(i, j-1, visited, grid, m, n)
        self.dfs(i, j+1, visited, grid, m, n)
    
    #BFS approach
    def bfs(self, i, j, m, n, visited, grid):
        Queue = deque([(i, j)])
        grid[i][j] = '0'

        while(Queue):
            x, y = Queue.popleft()
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                nx, ny = x + dx, y+ dy
                if(0 <= nx<m and 0 <= ny <n and grid[nx][ny] == '1'):
                    grid[nx][ny] = '0'
                    Queue.append((nx, ny))
# Both Time Complexity and Space Complexity are O(m*n) where m is the number of rows and n is the number of columns in the grid. This is because in the worst case, we may have to visit every cell in the grid once.
if __name__ == "__main__":
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["1","0","0","1","1"]
]
    g = Graph()
    print(g.numIslands(grid))