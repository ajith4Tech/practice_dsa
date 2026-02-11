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
    # if __name__ == "__main__":
    #     grid = [
    #   ["1","1","0","0","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","1","0","0"],
    #   ["1","0","0","1","1"]
    # ]
    #     g = Graph()
    #     print(g.numIslands(grid))


    #Rotting Oranges Leetcode Problem 994
    '''
    You are given an m x n grid where each cell can have one of three values:

        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.

    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    Example 1:

    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    Constraints:

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 10
        grid[i][j] is 0, 1, or 2.

    '''

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        queue = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j, 0))
                    visited[i][j] = True
                    print(queue)
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        while queue:
            i, j, time = queue.popleft()
            print(i, j, time)
            ans = max(ans, time)
            if (i-1 >= 0 and grid[i-1][j] == 1 and not visited[i-1][j]):
                visited[i-1][j] = True
                queue.append((i-1, j, time+1))
            if (i+1 < n and grid[i+1][j] == 1 and not visited[i+1][j]):
                visited[i+1][j] = True
                queue.append((i+1, j, time+1))
            if (j-1 >= 0 and grid[i][j-1] == 1 and not visited[i][j-1]):
                visited[i][j-1] = True
                queue.append((i, j-1, time+1))
            if (j+1 < m and grid[i][j+1] == 1 and not visited[i][j+1]):
                visited[i][j+1] = True
                queue.append((i, j+1, time+1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1
        return ans

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[2,1,1]]
    g = Graph()
    print(g.orangesRotting(grid))